# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# EMW forecast function for BTC data
# Mark M
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# clean the btc and z data in replication folder first


EMW_forecast_btc <- function(df.btc, df.z = NULL, model = "plain", method = "OLS") {
  
  # model options are  : plain (default), Taylor, Monetary, PPP
  # sample options are : long (default), early, late
  # method options are : OLS (default), MLE
  
  df.btc <- as.data.frame(df.btc_0)
  df.btc[df.btc == 0] <- NA # set 0's to NA (therwise when take logs will be infinity)
  df.btc <- na.omit(df.btc) # remove rows with missing data
  df.btc <- log(df.btc) # take logs to map data to clearer values
  names <- c("usd", "cad", "sgd", "hkd", "mxn", "nxd", "pln", "rub", "thb", "ars", "zar", "sek", "dkk", "czk", "inr", "ils", "aud", "nok", "jpy", "krw", "gbp", "eur")
  colnames(df.btc) <- names
  #colnames(df.z) <- names
  m <- dim(df.btc)[1] # end with 235 / or 340 huh values of 22 different exchange rates
  colsize <- dim(df.btc)[2]
  
  
  df.btc <- na.omit(df.btc)
  #df.z <- na.omit(df.z)
  
  # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  #                                                                 Options
  # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  
  bound.train <- 100; bound.test = m-100
  
  # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  #                                                               Forecast
  # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
  
  U.median <- as.data.frame(matrix(nrow=1, ncol=4))
  t_values <- as.data.frame(matrix(nrow=1, ncol=4))
  U_stats <- as.data.frame(matrix(nrow=4, ncol=colsize)); colnames(U_stats) <- names
  t_tests <- as.data.frame(matrix(nrow=4, ncol=colsize)); colnames(U_stats) <- names
  
  for (horizon in 1:4) {
    h = c(1,4,8,12)
    h = h[horizon]
    # h=1; # for trial purposes
    forecasts <- as.data.frame(matrix(nrow=bound.test, ncol=colsize)); colnames(forecasts) <- names # keep in loop, as may need reset each horizon
    SS.P <- as.data.frame(matrix(nrow=bound.test, ncol=colsize)); colnames(SS.P) <- names
    SS.A <- as.data.frame(matrix(nrow=bound.test, ncol=colsize)); colnames(SS.A) <- names
    #compare <- as.data.frame(matrix(nrow=84, ncol=9))
    
    for (j in 1:bound.test) {
      # restimate factors for 1973Q1-1986Q4 (1:56)
      df_fc <- df.btc[1:(bound.train+j-1),]; # eqn(4.1), expand train data used for factor analysis by 1 each iteration
      X_fc <- scale(df_fc, scale= FALSE); # scale demeans the data, column by column
      
      # means = t(as.matrix(apply(df_fc[[1]],2,mean)))
      f_fc <- factanal(X_fc,factors = 2, lower = 0.01) # this is the entire factor analysis function, choose r=2
      
      f_hat_fc = X_fc%*%f_fc[["loadings"]]/2
      
      train <- (bound.train-1)+j-h # starts at 99 (for h=1)
      s <- df_fc[, c(names)] # s_t
      
      # initialize some dfs
      SS <- as.data.frame(matrix(nrow=train, ncol=colsize)); colnames(SS) <- names
      
      for (t in 1:(train)) {
        SS[t,] <- s[t+h,] - s[t,] # want -0.05023416 for first, the LHS of eqn (4.2)
      }
      # SS <- na.omit(SS); train = dim(SS)[1] # 1 less as difference removed one
      
      # only factors
      FS <- f_hat_fc[1:train,] - s[1:train,] # cut last observation to match dimensions with y is RHS of (4.2)
      FS.P <- f_hat_fc[(train+h),] - s[(train+h),] # predict next, is RHS of (4.3)
      
       # if (model == "plain") { omitted z in this part
       #   z <- 0
       #   zP <- 0
       # } else if (model == "volume") {
       #   z <- df.CPI[1:train, c(names)] - df.CPI[1:train, "United.States"] # - s[1:train,] # should be just z or z-s??
       #   zP <- df.CPI[(train+h), c(names)] - df.CPI[(train+h), "United.States"] # - s[(train+h),]
       # } else 
       #   stop("not a valid model")

      m2 <- list();
      
#      method = "OLS"; model="plain" # for testing use
      
      if (method == "OLS")  {
        for (n in 1:colsize) {
          if (model == "plain") {
            m2[[n]] <- lm(SS[,n] ~ FS[,n]) # compare with OLS
            SS.P[j,n] <- m2[[n]]$coefficients[1] + m2[[n]]$coefficients[2]*FS.P[n] # eqn (4.3)
          } else { # any other model has a z-term
            m[[n]] <- lm(SS[,n] ~ FS[,n] + z[,n]) # compare with OLS
            SS.P[j,n] <- m[[n]]$coefficients[1] + m[[n]]$coefficients[2]*FS.P[n] + m[[n]]$coefficients[3]*zP[n] # eqn (4.3)
          }
        }
      } else if (method == "MLE") { # is there a better mle method ...?
        for (n in 1:colsize) {
          set.seed(10)
          param = runif(4)
          
          if (model == "plain") {
            m2[[n]] <- mle2(LL, data = list(y=SS, x=FS, n=n), start = list(alpha = param[1], beta  = param[2], sigma = param[3]), method = "BFGS")
            alpha = coef(m2[[n]])[1]
            beta = coef(m2[[n]])[2]
            SS.P[j,n] <- alpha + beta*FS.P[n]
          } else if (model != "plain") {
            m[[n]] <- mle2(LL.z, data = list(y=SS, x = FS, z = z, n=n), start = list(alpha = param[1], beta  = param[2], gamma = param[3], sigma = param[4]), method = "BFGS")
            alpha = coef(m[[n]])[1]
            beta = coef(m[[n]])[2]
            gamma = coef(m[[n]])[3]
            SS.P[j,n] <- alpha + beta*FS.P[n] + gamma*zP[n]
          } else
            stop("not a valid method")
        }
      }
    }
    
    
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #                                          Construct Theil's U-statistics
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    for (t in 1:bound.test) {
      SS.A[t,] <- df.btc[(bound.train+t+h),names] - df.btc[(bound.train+t),names] # find actual returns, the LHS of eqn (4.2)
    }
    
    SS.A <- na.omit(SS.A); SS.P <- SS.P[1:dim(SS.A)[1],] # drop to match size
    U.stats <- as.data.frame(matrix(nrow=1, ncol=colsize)); colnames(U.stats) <- names
    
    for (n in 1:colsize) {
      U.stats[,n] <- TheilU(SS.A[,n],SS.P[,n]) # TheilU is in the DescTools package
    }
    
    # save U-stats
    U_stats[horizon,] <- U.stats
    U.median[horizon] <- median(as.numeric(U.stats))
    
    # t-test
    t_tests <- t.test(U_stats[horizon,], mu=1, alternative="less")
    
    t_values[horizon] <- t_tests$statistic
  }
  
  EMW_forecast_list = list("sample" = sample, "model" = model, "U-stats" = U_stats, "U-median" = U.median, "t-values" = t_values)
  return(EMW_forecast_list)
}
