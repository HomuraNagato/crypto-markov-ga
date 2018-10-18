# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Factor Analysis of BTC, using exchange rates
# Mark McAvoy
# Spring 2018
# notes: 
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

library(tidyverse)
library(DescTools) # needed for THielU function (in EMW_forecast_btc)
library(bbmle) # needed for mle2 function (in EMW_forecast_btc)
library(tictoc)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                   try BTC exchange rate factor analysis
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# data from: https://spreadstreet.io

# be sure to change wd to data-BTC folder 
btc.usd <- read.csv("Bitcoin Markets (localbtcUSD).csv") # may have reason to remove usd, for supervised/unspupervised reasons, idk
btc.cad <- read.csv("Bitcoin Markets (localbtcCAD).csv")
btc.sgd <- read.csv("Bitcoin Markets (localbtcSGD).csv")
btc.hkd <- read.csv("Bitcoin Markets (localbtcHKD).csv")
btc.mxn <- read.csv("Bitcoin Markets (localbtcMXN).csv") 
btc.nxd <- read.csv("Bitcoin Markets (localbtcNZD).csv")
btc.pln <- read.csv("Bitcoin Markets (localbtcPLN).csv")
btc.rub <- read.csv("Bitcoin Markets (localbtcRUB).csv")
btc.thb <- read.csv("Bitcoin Markets (localbtcTHB).csv")
btc.ars <- read.csv("Bitcoin Markets (localbtcARS).csv")
btc.zar <- read.csv("Bitcoin Markets (localbtcZAR).csv")
btc.sek <- read.csv("Bitcoin Markets (localbtcSEK).csv")
# btc.vnd <- read.csv("Bitcoin Markets (localbtcVND).csv") # removed bc too small
btc.dkk <- read.csv("Bitcoin Markets (localbtcDKK).csv")
btc.czk <- read.csv("Bitcoin Markets (localbtcCZK).csv")
btc.inr <- read.csv("Bitcoin Markets (localbtcINR).csv")
btc.ils <- read.csv("Bitcoin Markets (localbtcILS).csv")
btc.aud <- read.csv("Bitcoin Markets (localbtcAUD).csv")
btc.nok <- read.csv("Bitcoin Markets (localbtcNOK).csv")
btc.jpy <- read.csv("Bitcoin Markets (coincheckJPY).csv")
btc.krw <- read.csv("Bitcoin Markets (korbitKRW).csv") 
# chinese data doesnt ends much too soon, so didn't include this either unfortunately
# btc.cny <- read.csv("Bitcoin Markets (btcnCNY).csv") # winner but not all :( 
# btc.cny2 <- read.csv("Bitcoin Markets (okcoinCNY).csv") # close second
btc.gbp <- read.csv("Bitcoin Markets (coinfloorGBP).csv")
btc.eur <- read.csv("Bitcoin Markets (krakenEUR).csv") # winner (most recent)
#btc.eur2 <- read.csv("Bitcoin Markets (btceEUR).csv") # has most
#btc.eur3 <- read.csv("Bitcoin Markets (bitcurexEUR).csv") # alot too

m <- 939 # temporary set based on korean won having smallest dataset
df.btc_0 <- cbind(btc.usd[1:m,"Weighted.Price"], btc.cad[1:m,"Weighted.Price"], btc.sgd[1:m,"Weighted.Price"],
                  btc.hkd[1:m,"Weighted.Price"], btc.mxn[1:m,"Weighted.Price"], btc.nxd[1:m,"Weighted.Price"],
                  btc.pln[1:m,"Weighted.Price"], btc.rub[1:m,"Weighted.Price"], btc.thb[1:m,"Weighted.Price"],
                  btc.ars[1:m,"Weighted.Price"], btc.zar[1:m,"Weighted.Price"], btc.sek[1:m,"Weighted.Price"], 
                  btc.dkk[1:m,"Weighted.Price"], btc.czk[1:m,"Weighted.Price"], btc.inr[1:m,"Weighted.Price"], 
                  btc.ils[1:m,"Weighted.Price"], btc.aud[1:m,"Weighted.Price"], btc.nok[1:m,"Weighted.Price"], 
                  btc.jpy[1:m,"Weighted.Price"], btc.krw[1:m,"Weighted.Price"],
                  btc.gbp[1:m,"Weighted.Price"], btc.eur[1:m,"Weighted.Price"]) # full 22 exchange rates

df.btc1 <- as.data.frame(df.btc_0)
df.btc1[df.btc1 == 0] <- NA # set 0's to NA (therwise when take logs will be infinity)
df.btc1 <- na.omit(df.btc1) # remove rows with missing data
df.btc1 <- log(df.btc1) # take logs to map data to clearer values
names <- c("usd","cad", "sgd", "hkd", "mxn", "nxd", "pln", "rub", "thb", "ars", "zar", "sek", "dkk", "czk", "inr", "ils", "aud", "nok", "jpy", "krw", "gbp", "eur")
colnames(df.btc1) <- names
m <- dim(df.btc1)[1] # end with 235 / or 340 huh values of 21 different exchange rates

X <- scale(df.btc1, scale=FALSE)

f <- factanal(X,factors = 3, rotation = "varimax", lower = 0.01) # try 3 factors at first, even with rotation doesnt change .. hmm
f_hat1 = X%*%f[["loadings"]]/3 # im not why equation this way, just saw some code that used this

time <- 1:m # for plotting
df_time <- as.tibble(cbind(time, f_hat1))

f[["loadings"]] # lets see loadings
ggplot(df_time, aes(time,Factor1)) + geom_line() # and see factors
ggplot(df_time, aes(time,Factor2)) + geom_line()
ggplot(df_time, aes(time,Factor3)) + geom_line() # they are pretty much the same ... only 1 factor then? hmm odd

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                                                Forecast
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# method options: OLS or MLE
tic() # 503 sec. for OLS; 1837.57 sec. for MLE
EMW_forecast_btc(df.btc_0, method="OLS")
toc()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                                                Appendix
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# no go ...
# df.v <- read.csv("bitcoinity_data.csv")
# df.v.cad.0 <- read.csv("bitcoinity_data_cad.csv")
# 
# end <- 1811; begin <- 123
# df.v.cad <- df.v.cad.0[begin:end,]



