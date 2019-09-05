## Data:

Crypto data is obtained from: http://api.bitcoincharts.com/v1/csv/
Current data for BTC / USD exchange rate we use data from CoinBaseUSD, from December 1st 2014 - December 31st, 2018
And for the BTC / JPY exchange rate we use CoinCheckJPY, from Halloween 2014 - December 31st, 2018

Following [Investopedia](https://www.investopedia.com/trading/factors-influence-exchange-rates/) we want to include the following 6 variables, that are thought to move the currencies that we use today.  It will be interesting to see if these have any predictive power for cryptocurrencies. 

# Exchange Rate Data: from FRED St. Luis Fed
  1) Differentials in Intererst Rates: 3-Month London Interbank Offered Rate (LIBOR), based on a basket of currencies:
      * :ballot_box_with_check: Japanese Yen (JPY3MTD156N), US Dollar (USD3MTD156N), Euro (EUR3MTD156N), and British Pound (GBP3MTD156N)
      * :ballot_box_with_check: To create differential, we take the mean across these four item, then difference each respective rate against this mean

# IRP and UIRP models
Collect interest rates on these currencies to model these popular exchange rates
use for comparison: the top currencies to buy BTC, from [Coinhills](https://www.coinhills.com/market/currency/)
at time of writing: USD 70.39%, JPY 20.03%, KRW 6.07%, EUR 1.39%, GBP 0.88%, and CNY .01% (included as back in 2014, 2015 it was in the first position [Investopedia](https://www.investopedia.com/tech/top-fiat-currencies-used-trade-bitcoin/))
Then take the average of these as the foreign interest rate, and USA as the base

Following, "Forecasting cryptocurrencies under model and parameter instability" by Cataniaa, Grassib, and Ravazzolo use:

  2) Cryptocurrency time series - in first difference of logs
      * :ballot_box_with_check: BTC / USD, BTC / JPY, BTC / EUR, BTC / GBP
  2) Additional crypto–explicative time series
      * Log high - log low of each Cryptocurrency, 
      * lags of each
  3) Additional financial and macro time series
      * Europe credit default swap index 5 years (can't find, so omit)
      * :ballot_box_with_check: Stoxx Europe 600 - Price Index ([Investopedia](https://www.investing.com/indices/stoxx-600-historical-data))
      * :ballot_box_with_check: Gold Bullion LBM ([GOLDAMGBD228NLBM](https://fred.stlouisfed.org/series/GOLDAMGBD228NLBM))
      * :ballot_box_with_check: Nikkei 225 Stock Average - Price Index ([NIKKEI225](https://fred.stlouisfed.org/series/NIKKEI225)
      * :ballot_box_with_check: S&P 500 Composite - Price Index ([SP500](https://fred.stlouisfed.org/series/SP500))
      * - Silver Handy & Harman Base Price (check bloomberg later)
      * :ballot_box_with_check: 1-Month US Treasury Constant Maturity Rate ([DGS1](https://fred.stlouisfed.org/series/DGS1))
      * :ballot_box_with_check: 10-Year US Treasury Constant Maturity Rate ([DGS10](https://fred.stlouisfed.org/series/DGS10))
      * :ballot_box_with_check: VIX closing price ([VIXCLS](https://fred.stlouisfed.org/series/VIXCLS))

Other crypto Data

  * Ethereum downloaded from: ([Yahoo](https://finance.yahoo.com/quote/ETH-USD/history?period1=1438833600&period2=1546232400&interval=1d&filter=history&frequency=1d))
  * Litecoin downloaded from: ([Yahoo](https://finance.yahoo.com/quote/LTC-USD/history?period1=1438833600&period2=1546232400&interval=1d&filter=history&frequency=1d))
  * Ripple downloaded from ([Yahoo](https://finance.yahoo.com/quote/XRP-USD/history?period1=1438833600&period2=1546232400&interval=1d&filter=history&frequency=1d))
  * Bitcoin downloaded from ([Yahoo](https://finance.yahoo.com/quote/BTC-USD/history?period1=1438920000&period2=1546232400&interval=1d&filter=history&frequency=1d))
