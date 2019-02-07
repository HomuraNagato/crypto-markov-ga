## Data:

Crypto data is obtained from: http://api.bitcoincharts.com/v1/csv/
Current data for BTC / USD exchange rate we use data from CoinBaseUSD, from December 1st 2014 - December 31st, 2018
And for the BTC / JPY exchange rate we use CoinCheckJPY, from Halloween 2014 - December 31st, 2018

Following [Investopedia](https://www.investopedia.com/trading/factors-influence-exchange-rates/) we want to include the following 6 variables, that are thought to move the currencies that we use today.  It will be interesting to see if these have any predictive power for cryptocurrencies. 

Exchange Rate Data: from FRED St. Luis Fed
  1) Differentials in Intererst Rates: 3-Month London Interbank Offered Rate (LIBOR), based on a basket of currencies:
      * :ballot_box_with_check: Japanese Yen (JPY3MTD156N), US Dollar (USD3MTD156N), Euro (EUR3MTD156N), and British Pound (GBP3MTD156N)
      * :ballot_box_with_check: To create differential, we take the mean across these four item, then difference each respective rate against this mean
lets pass on the rest ... as found better in another paper, "Forecasting cryptocurrencies under model and parameter instability" by Cataniaa, Grassib, and Ravazzolo
  2) Differentials in Interest rates: Effective Federal Funds Rate (DFF)
      * Again, need to collect a basket
  3) Current Account Deficits: I couldn't get a good measure
  4) Public Debt: Can find daily data at [TreasuryDirect - The Daily History of the Debt Results](https://www.treasurydirect.gov/NP/debt/search?startMonth=12&startDay=01&startYear=2014&endMonth=10&endDay=31&endYear=2018)
      * Can we scrape this data Matt?
  5) Terms of Trade: Need current accounts data for this ..
  6) Political Stability and Economic Performance: Need to find some literature on what measures of this are

Following, "Forecasting cryptocurrencies under model and parameter instability" by Cataniaa, Grassib, and Ravazzolo use:
  1) Cryptocurrency time series - in first difference of logs
      * :ballot_box_with_check: BTC / USD, BTC / JPY, BTC / EUR, BTC / GBP
  2) Additional crypto–explicative time series
      * Log high - log low of each Cryptocurrency, 
      * lags of each
  3) Additional financial and macro time series
      * Europe credit default swap index 5 years
      * Stoxx Europe 600 - Price Index
      * :ballot_box_with_check: Gold Bullion LBM (GOLDAMGBD228NLBM)
      * :ballot_box_with_check: Nikkei 225 Stock Average - Price Index (NIKKEI225)
      * :ballot_box_with_check: S&P 500 Composite - Price Index (SP500)
      * :ballot_box_with_check:ish - Silver Handy & Harman Base Price (same as Silver Fixing Price 12:00 noon (London time) in London Bullion Market, based in U.S. Dollars (SLVPRUSD)?)
      * :ballot_box_with_check: 1-Month US Treasury Constant Maturity Rate (DGS1)
      * :ballot_box_with_check: 10-Year US Treasury Constant Maturity Rate (DGS10)
      * :ballot_box_with_check: VIX closing price (OVXCLS)
