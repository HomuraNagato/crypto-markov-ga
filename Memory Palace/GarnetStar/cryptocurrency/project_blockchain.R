# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Project Blockchain 
# Mark McAvoy
# Origin: April 1, 2018
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

library(tidyverse)
library(pracma)
library(dlm)

S2 <- read.csv("S2.csv")
# ggplot(S2, aes(x_, market_price)) + geom_point()

# turn prices into returns as (p_t - p_t-1)/p_t-1

# make covariance stationary
# first difference
date_dif <- as.data.frame(S2[-1,"x_"])
r_dif <- as.data.frame((S2[-1,"market_price"] - S2[-nrow(S2),"market_price"])/ S2[-nrow(S2),"market_price"])
dif <- cbind(date_dif, mp_dif)
names(dif) <- c("x", "y")
ggplot(dif, aes(x,y)) + geom_point()

# linear detrend
mp_trend <- as.data.frame(detrend(S2$market_price, tt='linear'))
trend <- cbind(S2$x_, mp_trend)
names(trend) <- c("x", "y")
ggplot(trend, aes(x,y)) + geom_point()

# kalman filter detrend (help)
mod <- dlmModReg(S2$market_price)
k_trend <- dlmFilter(S2$market_price, mod)
k_trend2 <- as.data.frame(cbind(S2$x_, k_trend[1]$y))
ggplot(k_trend2, aes(V1, V2)) + geom_point()
