# blockchain.info luxembourg s.a.r.i

import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_single(S2, x, y, label):


    fig, axes = plt.subplots(figsize=(20,12), nrows=1, ncols=1)

    axes.plot(S2[x], S2[y],'k',label=label)

    #plt.show()


if __name__ == '__main__':

    url = 'https://api.blockchain.info/charts/n-transactions?format=json'
    #url =  'https://api.blockchain.info/charts/transactions-per-second?timespan=5weeks&rollingAverage=8hours&format=json'

    response = requests.get(url=url)
    data = response.json()

    for d in data:
        print(d, ":", data[d])
    x = [ d['x'] for d in data['values'] ]
    y = [ d['y'] for d in data['values'] ]
    #print("x and y\n", x, "\n", y)
    S2 = pd.DataFrame({'x': x, 'y': y})
    print("Head of S2\n", S2.head())
    plot_single(S2, 'x', 'y', 'insert_label')
