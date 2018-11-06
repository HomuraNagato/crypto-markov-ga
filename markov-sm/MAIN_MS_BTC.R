# translate Davide's Matlab MS code into R code
library(tidyverse)
rm(list = ls())

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Parameters controlling sample size
date_est_start  = '2018-09-17'
date_forc_start = '2018-09-19'
date_forc_end   = '2018-09-30'
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Parameters controlling estimation, including lag length choices
p_Y      = 4  # number of lags of dependent variable (when present)
q_X      = 1  # number of lags of exogenous variable (when present)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Parameters controlling MS and CP estimation (dictating max number of
# breaks/regimes tested)
M = 2;

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# MCMC parameters
I           = 1000  #  this is how many draws I want to keep
burn        = 100   # this is how many draws I want to burn at the beginning of the chain
thin_factor = 1     # this is how often I am going to retain draws
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Priors
# Hyperparameters on linear regression coefficients and volatility (when
# constant)
psi_mat     = 10    #
v0_mat      = 0.01  #

# Hyperparameters on MS transition prob matrix elements
ekk  = 2            # this is for the elements of the main diagonal
ekkp = 1            # this is for the off-diagonal elements

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Parameters pertaining to predictive density simulations
forc_rep    = 10     # number of forecasts computed for each draw of Gibbs sampler

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Parameters controlling forecast horizons
forc_h = 1
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Load the data

df <- read.csv('btc_S3_day.csv')
head(df)

df <- df %>% mutate(P = price,
                    Pl = lag(price, 1),
                    Y = log(P / Pl),
                    Yl = lag(Y,1))
Y = df %>% select(Y)
Yl <- rbind(NA, df[(1+1):end,"Yl"])

# construct additional lags
  lagit4me <- function(serie,lag){
  n = length(serie);
  pad = rep(NA,lag);
  return(c(pad,serie)[1:n]);
  }

  VectorLagNtimes <- function(V, N, letter) {
      df.lags <- data.frame(matrix(NA, nrow = end, ncol = N))

      for (l in 1:N) {
        df.lags[l] = lagit4me(V, l)
      }
      colnames(df.lags) <- paste(letter, "l", 1:N, sep = "")
      return(df.lags)
  }

AllLagY <- VectorLagNtimes(df$Y, 4, "Y")
head(AllLagY)

# we don't need to lag X?
AllX <- df %>% select(SA.1, SA1)

# Start estimation
cat('****** Psi = ', psi_mat, ', v_0 = ', v0_mat, ' *******')

nExoReg = dim(X)[2]*q_X
n_reg   = 1+p_Y+nExoReg

# Define sample
this_tb = min(which((as.POSIXct(df$fdate) >= as.POSIXct(date_est_start))))
this_te = max(which((as.POSIXct(df$fdate) <= as.POSIXct(date_forc_end)))) - 8 # -8 due to data being 8 collections per day, later change to -10
t = this_te+1

# Bayesian estimation starts here
cat('Bayesian MS estimation for M = ', M)

Est_Y    = as.matrix(Y[this_tb:(t-forc_h), ])
Est_X    = AllX[(this_tb-forc_h):(t-2*forc_h), ]
Est_LagY = AllLagY[(this_tb-forc_h):(t-2*forc_h), ]

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % Fix to deal with cases where NaNs are showing up
# nan_indx = sum(isnan([Est_Y,Est_X,Est_LagY]),2) > 0;
# if ~isempty(find(nan_indx == 1))
#     indx_drop = find(nan_indx == 1);
#     t_fix2 = max(indx_drop)+1;
#     disp(['Reduced estimation window from ',num2str(length(Est_Y)), ' obs. to ',num2str(length(Est_Y)-t_fix2+1),' by dropping obs. ',num2str(indx_drop')]);
#     Est_Y    = Est_Y(t_fix2:end);
#     Est_X    = Est_X(t_fix2:end,:);
#     Est_LagY = Est_LagY(t_fix2:end,:);
# end
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % Priors

# Combine constant, lagged Y and lagged exogenous regressors
RHS     = cbind(matrix(1,dim(Est_LagY)[1],1), Est_LagY, Est_X)

# Priors on regression coefficients depends on what the benchmark is in
# the different cases
RHS = as.matrix(RHS); dim(RHS)
prior = list()
head(prior$b0)
prior$b0 = matrix(0, dim(RHS)[2], 1) # this implies that the best forecast for inflation this period is the h-period before inflation (no change model)
prior$s02 = (t(Est_Y - (RHS %*% prior$b0))) %*% (Est_Y - (RHS%*%prior$b0))
head(prior$s02)
RHS %*% prior$b0
