## Data:

Crypto data is obtained from: http://api.bitcoincharts.com/v1/csv/
Current data for BTC / USD exchange rate we use data from CoinBaseUSD, from December 1st 2014 - November 8th 2018
And for the BTC / JPY exchange rate we use CoinCheckJPY, from 

Following [Investopedia](https://www.investopedia.com/trading/factors-influence-exchange-rates/) we want to include the following 6 variables, that are thought to move the currencies that we use today.  It will be interesting to see if these have any predictive power for cryptocurrencies. 

Exchange Rate Data: from FRED St. Luis Fed
  1) Differentials in Inflation: 10-Year Breakeven Inflation Rate (T10YIE)
      * To create differential, we should collect a basket of interest rates and measure the difference with this.
  2) Differentials in Interest rates: Effective Federal Funds Rate (DFF)
      * Again, need to collect a basket
  3) Current Account Deficits: I couldn't get a good measure
  4) Public Debt: Can find daily data at [TreasuryDirect - The Daily History of the Debt Results](https://www.treasurydirect.gov/NP/debt/search?startMonth=12&startDay=01&startYear=2014&endMonth=10&endDay=31&endYear=2018)
      * Can we scrape this data Matt?
  5) Terms of Trade: Need current accounts data for this ..
  6) Political Stability and Economic Performance: Need to find some literature on what measures of this are
