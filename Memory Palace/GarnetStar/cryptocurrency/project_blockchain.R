# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Project Blockchain 
# Mark McAvoy
# Origin: April 1, 2018
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

library(tidyverse)

setwd("C:/Users/homur/OneDrive/Memory\ Palace/GarnetStar/cryptocurrency")
S2 <- read.csv("S2.csv")
# ggplot(S2, aes(x_, market_price)) + geom_point()

# turn prices into returns as (p_t - p_t-1)/p_t-1

# make covariance stationary
# returns
date_2 <- as.data.frame(S2[-1,"x_"]) # subset date by removing first value to match returns
returns <- as.data.frame((S2[-1,"market_price"] - S2[-nrow(S2),"market_price"])/ S2[-nrow(S2),"market_price"])
bind_1 <- cbind(date_2, returns)
names(bind_1) <- c("x", "y")
ggplot(bind_1, aes(x,y)) + geom_point()

# tidyverse way
S2 <- S2 %>% mutate(returns = (market_price - lag(market_price))/lag(market_price))
ggplot(data=S2, aes(x=x_,y=returns)) + geom_point()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                       try exchange rate factor analysis
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# data from: https://spreadstreet.io

setwd("C:/Users/homur/OneDrive/Memory\ Palace/GarnetStar/cryptocurrency/btc\ data/")
btc_usd <- read.csv("Bitcoin Markets (localbtcUSD).csv") # actually lets not include usd, as pca should be unsupervised learning rt?
btc_cad <- read.csv("Bitcoin Markets (localbtcCAD).csv")
btc_sgd <- read.csv("Bitcoin Markets (localbtcSGD).csv")
btc_hkd <- read.csv("Bitcoin Markets (localbtcHKD).csv")
btc_mxn <- read.csv("Bitcoin Markets (localbtcMXN).csv") 
btc_nxd <- read.csv("Bitcoin Markets (localbtcNZD).csv")
btc_pln <- read.csv("Bitcoin Markets (localbtcPLN).csv")
btc_rub <- read.csv("Bitcoin Markets (localbtcRUB).csv")
btc_thb <- read.csv("Bitcoin Markets (localbtcTHB).csv")
btc_ars <- read.csv("Bitcoin Markets (localbtcARS).csv")
btc_zar <- read.csv("Bitcoin Markets (localbtcZAR).csv")
btc_sek <- read.csv("Bitcoin Markets (localbtcSEK).csv")
# btc_vnd <- read.csv("Bitcoin Markets (localbtcVND).csv") # removed bc too small
btc_dkk <- read.csv("Bitcoin Markets (localbtcDKK).csv")
btc_czk <- read.csv("Bitcoin Markets (localbtcCZK).csv")
btc_inr <- read.csv("Bitcoin Markets (localbtcINR).csv")
btc_ils <- read.csv("Bitcoin Markets (localbtcILS).csv")
btc_aud <- read.csv("Bitcoin Markets (localbtcAUD).csv")
btc_nok <- read.csv("Bitcoin Markets (localbtcNOK).csv")
btc_jpy <- read.csv("Bitcoin Markets (coincheckJPY).csv")
btc_krw <- read.csv("Bitcoin Markets (korbitKRW).csv") 
# chinese data doesnt ends much too soon, so didn't include this either unfortunately
# btc_cny <- read.csv("Bitcoin Markets (btcnCNY).csv") # winner but not all :( 
# btc_cny2 <- read.csv("Bitcoin Markets (okcoinCNY).csv") # close second
btc_gbp <- read.csv("Bitcoin Markets (coinfloorGBP).csv")
btc_eur <- read.csv("Bitcoin Markets (krakenEUR).csv") # winner (most recent)
btc_eur2 <- read.csv("Bitcoin Markets (btceEUR).csv") # has most
btc_eur3 <- read.csv("Bitcoin Markets (bitcurexEUR).csv") # alot too

df <- cbind(btc_usd$Weighted.Price, btc_aud$Weighted.Price) # same size so OK, test data
m <- 939 # temporary set based on korean won having smallest dataset
df2 <- cbind(btc_cad[1:m,"Weighted.Price"], btc_sgd[1:m,"Weighted.Price"],
             btc_hkd[1:m,"Weighted.Price"], btc_mxn[1:m,"Weighted.Price"], btc_nxd[1:m,"Weighted.Price"],
             btc_pln[1:m,"Weighted.Price"], btc_rub[1:m,"Weighted.Price"], btc_thb[1:m,"Weighted.Price"],
             btc_ars[1:m,"Weighted.Price"], btc_zar[1:m,"Weighted.Price"], btc_sek[1:m,"Weighted.Price"], 
             btc_dkk[1:m,"Weighted.Price"], btc_czk[1:m,"Weighted.Price"], btc_inr[1:m,"Weighted.Price"], 
             btc_ils[1:m,"Weighted.Price"], btc_aud[1:m,"Weighted.Price"], btc_nok[1:m,"Weighted.Price"], 
             btc_jpy[1:m,"Weighted.Price"], btc_krw[1:m,"Weighted.Price"],
             btc_gbp[1:m,"Weighted.Price"], btc_eur[1:m,"Weighted.Price"]) # full 22 exchange rates
# df3 <- ldply(c("btc_usd", "btc_aud")) .. is there an easier way to do above line?

# There is perhaps an R way to iterate and add files to a dataframe. There definitely is using python

df2.stored <- as.data.frame(df2)
df2[df2 == 0] <- NA # set 0's to NA (therwise when take logs will be infinity)
df3 <- na.omit(df2) # remove rows with missing data
df4 <- log(df3) # take logs to map data to clearer values
m <- dim(df4)[1] # end with 235 values

# tidyverse way
# previous solution is more readable. Only provided to show additional ways to use tidyr
df4.tidyr <- df2.stored %>% mutate_at(vars(contains("V")), funs(replace(., . == 0, NA))) %>% 
			drop_na() %>% mutate_if(., is.numeric, log))
m.tidyr <- dim(df4.tidyr)[1]
paste("df4 and df4.tidyr have", m, m.tidyr, "rows respectfully, thus equivalent functions", sep=" ")

means = t(as.matrix(apply(df4,2,mean)))
X <- as.matrix(df4 - kronecker(matrix(1,m,1),means))

# tidyverse doesn't do well with matricies, alternatives not clear.

f <- factanal(X,factors = 3, rotation = "varimax", lower = 0.01) # try 3 factors at first
f_hat1 = X%*%f[["loadings"]]/3 # im not why equation this way, just saw some code that used this
# I think %*% is matrix multiplication of X (235 x 21) and f (21 x 3) = (235 x 3)
time <- 1:m # for plotting
df_time <- as.tibble(cbind(time, f_hat1))

f[["loadings"]] # lets see loadings
ggplot(df_time, aes(time,Factor1)) + geom_line() # and see factors
ggplot(df_time, aes(time,Factor2)) + geom_line()
ggplot(df_time, aes(time,Factor3)) + geom_line() # they are pretty much the same ... only 1 factor then? hmm odd

# next part is to see how well the factor forecasts btc/usd exchange rate