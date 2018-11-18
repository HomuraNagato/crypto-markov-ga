# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# BTC Data Cleaning
# Mark McAvoy
# Autumn 2018
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Clear enviroment before starting
remove(list = ls())

# Install packages as required
if(!require(tidyverse)) install.packages("tidyverse", repos = "http://cran.us.r-project.org") # run this the first time (only need to once)
library(tidyverse) # includes ggplot2 and many more useful libraries
# if(!require(knitr)) install.packages("knitr", repos = "http://cran.us.r-project.org")
# library(knitr)
if(!require(anytime)) install.packages("anytime", repos = "http://cran.us.r-project.org")
library(anytime)
if(!require(zoo)) install.packages("zoo", repos = "http://cran.us.r-project.org")
library(zoo)
# Change working directory
#getwd()
setwd("/Users/markmcavoy/Documents/Research")
# setwd("/Users/mattmcavoy/)

# Read in BTC data
btc_usd <- read.csv("Data/coinbaseUSD.csv")
# btc_jpn <- read.csv("Data/coinbaseJPN.csv") just using USD data for now

## ----- Read in S3_pivot = Sentiment data + other variables
S3 <- read.csv("S3_df.csv")
names(S3) <- c("timestamp", "SA-1", "SA0", "SA1")
write.csv(S3, "S3_df.csv")

inflation <- read.csv("Data/inflation-10Ybreak.csv")

## ------ Create daily data
# BTC Daily
names(btc_usd) <- c("timestamp", "price", "volume")
btc_day_temp <- btc_usd %>% mutate(date = anytime(timestamp),
                               fdate = factor(format(date, '%Y-%m-%d')))

# get daily closing price
# october 11th
# 51682386, 1539316798, 6189.99, 0.04746211, 2018-10-11 23:59:58, 2018-10-11 2
btc_day <- btc_day_temp %>% group_by(fdate) %>% slice(c(n()))
tail(btc_day) # it worked as inteded :)
#write.csv(daily_btc, "daily_btc.csv")

# Sentiment Daily
S3_day_temp <- S3 %>% mutate(date = anytime(timestamp),
                             fdate = factor(format(date, '%Y-%m-%d %H')))
S3_day <- S3_day_temp %>% group_by(fdate) %>% slice(c(n()))

# Inflation Daily
head(inflation)
inflation <- mutate(fdate = factor(format(DATE, '%Y-%m-%d')))


## --- Now merge btc_usd and Sentiment + other variables


# And merge by date (this keeps only dates in fdate that are the same)
temp <- merge(btc_day, S3_day, by = c("fdate"))
# and keep only columns of interest
keep <- c("fdate", "price", "SA-1", "SA0", "SA1")
df_day <- temp %>% select(keep)
write.csv(df_day, "btc_S3_day.csv")

"""
##### ---- Archives ---- #####
## ------ Get prices at 3 hr intervals
# lets start with simply average price per hour
# subset to a manageable dataframe size
df_sub <- df %>% filter(timestamp >= 1539316790)
head(df_sub, 10)
df_sub <- df_sub %>% mutate(fdate = factor(format(date,'%Y-%m-%d')),
                            fhr = factor(format(date,'%H')))
df_sub
df_sub <- df_sub %>% group_by(fdate) %>% mutate(avg_p = mean(price))

# do for large df later
# btc_usd <- btc_usd %>% mutate(date = anytime(timestamp))
# btc_usd <- btc_usd %>% mutate(fdate = factor(format(df2$date,'%Y-%m-%d %H')))
# btc_usd <- btc_usd %>% group_by(fdate) %>% mutate(avg_p = mean(price))
# head(btc_usd, 1000)

# now lets try to get closing prices at the 3 hr intervals
# set row 1539316801 as start of group 0
# 1539316801 6189.99 0.02480446 2018-10-12 00:00:01
# three_hr <- cut(df$date, breaks = "hour")
# Means <- ddply(df, .(hosts, three_hour), getmeans)
# df_3hr <- df %>% mutate(interval = ifelse(grepl(04, fdate), "group 4", "not")

temp <- df_sub
#temp <- temp %>% mutate(interval = ifelse(grepl("*00", fdate), 0,
#                                   ifelse(grepl("*07", fdate), 7, NA)))
temp <- temp %>% mutate(interval = ifelse(fhr == "00", "g0",
                                   ifelse(fhr == "03", "g3",
                                   ifelse(fhr == "06", "g6",
                                   ifelse(fhr == "09", "g9",
                                   ifelse(fhr == "12", "g12",
                                   ifelse(fhr == "15", "g15",
                                   ifelse(fhr == "18", "g18",
                                   ifelse(fhr == "21", "21", "first_group")))))))))
# fill in NA's with group above
temp$interval <- na.locf(temp$interval)
head(temp)
"""
