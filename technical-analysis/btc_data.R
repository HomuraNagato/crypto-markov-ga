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
setwd(getwd())
# setwd("/Users/mattmcavoy/)

# Read in BTC data
btc_usd <- read.csv("technical-analysis/Data/btc/coinbaseUSD.csv")  # goes back to Dec 1st, 2014
# btc_jpy <- read.csv("btc/coincheckJPY.csv") # goes back to Halloween 2014
# btc_eur <- read.csv("btc/coinbaseEUR.csv") # goes back to April 23, 2015
# btc_gbp <- read.csv("btc/coinbaseGBP.csv") # goes back to April 22, 2015

## -----------------------------------------------------------------------------------------
# ------ Create daily BTC / USD data
names(btc_usd) <- c("timestamp", "price", "volume")
btc_usd_day_temp <- btc_usd %>% mutate(date = anytime(timestamp),
                               fdate = factor(format(date, '%Y-%m-%d')))

btc_usd_day <- btc_usd_day_temp %>% group_by(fdate) %>% slice(c(n())) # take the last value for the day, as the "closing" day price
# 1417416612 is usd's first timestamp on 2014-12-01 
# 1541044791 is usd's last timestamp on 2018-10-31
# following for Dec 2014 - Dec 2018
# btc_usd_day <- btc_usd_day %>% filter(timestamp <= 1541044791)
# following for 2018 only
btc_usd_day <- btc_usd_day %>% filter(timestamp <= 1541044791 & timestamp >= 1514869199)
# write.csv(btc_usd_day, "btc_usd_day.csv")

# ------ Create daily BTC / JPY data
names(btc_jpy) <- c("timestamp", "price", "volume")
# note to get the following to run I had to use:
# Sys.setenv('R_MAX_VSIZE'=64000000000)
# to increase memory size, as well as rm() all other datasets, 
# to clear space for the following large dataset \(^.^)\
btc_jpy_day_temp <- btc_jpy %>% mutate(date = anytime(timestamp),
                                       fdate = factor(format(date, '%Y-%m-%d')))

btc_jpy_day_temp <- btc_jpy_day_temp %>% group_by(fdate) %>% slice(c(n())) # take the last value for the day, as the "closing" day price
# 1417418343 is jpy's first time-stamp on 2014-12-01
# 1541044783 is jpy's last time-stamp on 2018-10-31
# following for Dec 2014 - Dec 2018
# btc_jpy_day_temp <- btc_jpy_day_temp %>% filter(timestamp >= 1417418343 && timestamp <= 1541044783) 
# following for year 2018 only
# write.csv(btc_jpy_day, "btc_jpy_day.csv")

# ------ Create daily BTC / EUR data
names(btc_eur) <- c("timestamp", "price", "volume")
btc_eur_day_temp <- btc_eur %>% mutate(date = anytime(timestamp),
                                       fdate = factor(format(date, '%Y-%m-%d')))
btc_eur_day_temp <- btc_eur_day_temp %>% group_by(fdate) %>% slice(c(n())) 

# ------ Create daily BTC / GBP data
names(btc_gbp) <- c("timestamp", "price", "volume")
btc_gbp_day_temp <- btc_gbp %>% mutate(date = anytime(timestamp),
                                       fdate = factor(format(date, '%Y-%m-%d')))
btc_gbp_day_temp <- btc_gbp_day_temp %>% group_by(fdate) %>% slice(c(n())) 
## -----------------------------------------------------------------------------------------
# ------ Sentiment Daily
S3 <- read.csv("twitter-sentiment/complete_tweets/complete_tweets_2018_trim.csv")
names(S3) <- c("timestamp", "SA-1", "SA0", "SA1")


S3_day_temp <- S3 %>% mutate(date = anytime(timestamp),
                             fdate = factor(format(date, '%Y-%m-%d %H')))
S3_day <- S3_day_temp %>% group_by(fdate) %>% slice(c(n()))
# write.csv(S3_day, "S3_day.csv")

## -----------------------------------------------------------------------------------------
# ------ Inflation
inflation <- read.csv("Data/inflation-10Ybreak.csv")
head(inflation)
inflation <- mutate(fdate = factor(format(DATE, '%Y-%m-%d')))


## --- Now merge btc_usd and Sentiment + other variables


# And merge by date (this keeps only dates in fdate that are the same)
temp <- merge(btc_day, S3_day, by = c("fdate"))
# and keep only columns of interest
keep <- c("fdate", "price", "SA-1", "SA0", "SA1")
df_day <- temp %>% select(keep)
write.csv(df_day, "btc_S3_day.csv")

## -----------------------------------------------------------------------------------------
# ------ Merge all variables together

"""
## -----------------------------------------------------------------------------------------
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
