# Twitter sentiment analysis
# following https://dev.to/rodolfoferro/sentiment-analysis-on-trumpss-tweets-using-python-

# general imports
import numpy as np
import pandas as pd
import tweepy

# plotting and visualization
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline  # for jupyter notebook

print(matplotlib.get_backend())

from credentials import *   # import API key and access key and token without being seen by the app


def twitter_setup():
    """
    Utility function to setup the Twitter's API with our
    access keys provided
    """
    # authentication and access using keys
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # return API with authentication
    api = tweepy.API(auth)
    return api

if __name__ == "__main__":

    # create an extractor object to get quantity of tweets from screen_name
    extractor = twitter_setup()

    # create a tweet list
    tweets = extractor.user_timeline(screen_name="realDonaldTrump", count=200)
    print("Number of tweets extracted: {}.\n".format(len(tweets)))

    # print the most recent five tweets
    [ print(tweet.text) for tweet in tweets[:5] ]
    print()

    # create a pandas df from tweets
    S2 = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

    # display the first 10 elements of the df
    #print(S2.head(10))

    # internal methods of a single tweet object
    #print(dir(tweets[0]))

    # adding tweet metadata
    S2['len'] = np.array([len(tweet.text) for tweet in tweets])
    S2['ID'] = np.array([tweet.id for tweet in tweets])
    S2['Date'] = np.array([tweet.created_at for tweet in tweets])
    S2['Source'] = np.array([tweet.source for tweet in tweets])
    S2['Likes'] = np.array([tweet.favorite_count for tweet in tweets])
    S2['RTs'] = np.array([tweet.retweet_count for tweet in tweets])

    print(S2.head(10))

    # mean of lengths
    mean = np.mean(S2['len'])
    print("The average length in tweets: {}".format(mean))

    # max favorites and Retweets
    fav_max = np.max(S2['Likes'])
    rt_max = np.max(S2['RTs'])

    fav = S2[S2['Likes'] == fav_max].index[0]
    rt = S2[S2['RTs'] == rt_max].index[0]

    print("The tweet with the most ({}) likes is: {}".format(fav_max, S2['Tweets'][fav]))

    print("The tweet with the most ({}) retweets is: {}".format(rt_max, S2['Tweets'][rt]))

    # create time series data

    tlen = pd.Series(data=S2['len'].values, index=S2['Date'])
    tfav = pd.Series(data=S2['Likes'].values, index=S2['Date'])
    tret = pd.Series(data=S2['RTs'].values, index=S2['Date'])

    # plot lengths of tweets
    tlen.plot(figsize=(16,4), color='r')
    plt.show()

    # plot likes and retweets
    tfav.plot(figsize=(16,4), label="Likes", legend=True)
    tret.plot(figsize=(16,4), label="Retweets", legend=True)
    plt.show()
    """
    # plot sources in a pie chart
    sources = []
    for source in S2['Source']:
        if source not in sources:
            sources.append(source)

    print("create of content sources:")
    [ print("* {}").format(source) for source in sources ]

    # count number of sources
    percent = np.zeroes(len(sources))

    for source in S2['Source']:
        for index in range(len(sources)):
            if source == sources[index]:
                percent[index] += 1
                pass

    percent /= 100

    pie_chart = pd.Series(percent, index=sources, name='Sources')
    pie_chart.plot.pie(fontsize=11, autopct='%.2f', figsize=(6,6))
    plt.show()
    """

    
