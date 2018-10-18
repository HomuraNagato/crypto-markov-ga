# wallet.py
# determine net worth of cryptocurrencies

import numpy as np
import pandas as pd

class wallet(object):

    def __init__(self, ):
        self.usd = 0
        self.gross = 0
        self.volume = 0
        self.price = 0
        self.price_array = []

    def purchase(self, volume, price):
        self.volume = self.volume + volume
        self.price_array.append(price)
        self.gross = self.gross + (volume * price)

    def sell(self, volume, price):
        self.volume = self.volume - volume
        self.gross = self.gross - (volume * price)

    def __str__(self):
        return 'volume: ' + str(self.volume) + ' Average buy price: ' + \
               str(np.mean(self.price_array)) + ' for a net work of ' + str(self.gross)

class btc(wallet):

    def __init__(self):

        wallet.__init__(self)

class bch(wallet):

    def __init__(self):

        wallet.__init__(self)
        self.bch_volume = 0
        self.bch_price = 0


if __name__ == "__main__":

    S2 = pd.read_csv('logs.csv', header=0)

    print("head of S2\n", S2)

    #star_btc = btc()
    #star_bch = bch()
    star_btc = wallet()
    star_bch = wallet()

    for index, row in S2.iterrows():

        if row['currency'] == 'bch':
            if row['transcation'] == 'buy':
                star_bch.purchase(row['volume'], row['price'])
            else:
                star_bch.sell(row['volume'], row['price'])

    print("BTC wallet", star_btc)
    print("BCH wallet", star_bch)
