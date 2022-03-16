import csv

import pandas as pd
import numpy as np
from datetime import datetime
import tushare as ts
from matplotlib import pyplot as plt
import pyEX as p
import yfinance as yf
from dateutil import parser

ticker = 'AAPL'

class MACD:
    __macd = []
    __signal = []
    __colapse = []

    def __init__(self, exchange_rate):
        self.__macd = []
        self.__colapse = []
        for i in range(len(exchange_rate)):
            if i >= 26:
                self.calc_macd(exchange_rate, i)
            else:
                self.__macd.append(float(0))
        self.calc_signal()
        for i in range(len(exchange_rate)):
            if i >= 26:
                self.isCollapse(i)

    def print(self):
        print(self.__macd)
        print(self.__signal)
        print(self.__colapse)

    def calc_ema(self, period, data, day):
        alpha = 2 / (period + 1)
        counter = float(0.0)
        denominator = float(0.0)
        samples = data[day - period: day + 1:]  # zbiór próbek
        samples.reverse()

        base = 1 - alpha
        for i in range(period):
            if day - i >= 0:
                counter += base ** i * samples[i]
                denominator += base ** i
        return counter / denominator

    def calc_macd(self, exchange_rate, i):
        temp_ema12 = self.calc_ema(12, exchange_rate, i)
        temp_ema26 = self.calc_ema(26, exchange_rate, i)

        self.__macd.append(temp_ema12 - temp_ema26)

    def calc_signal(self):
        self.__signal = []
        for i in range(26, len(self.__macd)):
            self.__signal.append(self.calc_ema(9, self.__macd, i))

    def getMacd(self, n=0):
        return self.__macd[n::]

    def getSignal(self, n=0):
        return self.__signal[n::]

    def isCollapse(self, i):
        if self.__macd[i - 1] > self.__signal[i - 26 - 1] and self.__macd[i] < self.__signal[i - 26]:
            self.__colapse.append(self.__signal[i - 26])
        elif self.__macd[i - 1] < self.__signal[i - 26 - 1] and self.__macd[i] > self.__signal[i - 26]:
            self.__colapse.append(self.__signal[i - 26-1])
        else:
            self.__colapse.append(float(0))


    def getCollapse(self, n=0):
        return self.__colapse[n::]


class Data:
    __name = ''

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_data(self):
        file = "./data/" + str(self.__name) + '.csv'
        f = open(file, 'r')
        data = list(csv.reader(f))
        data = data[1::]
        # data.reverse()

        time = [parser.parse(t[0]) for t in data]
        exchange_rate = [float(ex[1]) for ex in data]

        return time, exchange_rate

    def init_data(self):
        # Request historic pricing data via finance.yahoo.com API
        # start = "2017-03-07"
        # end = datetime.today()
        # hist = yf.download(self.__name, start=start, end=end)
        df = yf.Ticker(self.__name).history(period='1y')[['Close']]
        # Save our data
        df.to_csv('./data/' + ticker + '.csv')
        # hist.to_csv('./data/' + ticker + '.csv')
        # View our data
        print(df)
        # print(hist)


class Plot:
    def show_macd_signal_diagram(self, time, macd, signal, name):
        plt.plot(time, macd, label="macd", color='blue')
        plt.plot(time, signal, label="signal", color='red')
        plt.ylabel('Wartość składowych (' + name + ')')
        plt.xlabel('Data (yyyy-mm)')
        plt.title('Wskaźnik MACD')
        plt.legend()
        plt.grid(True)
        plt.savefig('./images/' + name + '_macd' + '.png')
        plt.show()

    def show_macd_signal_collapse_diagram(self, time, macd, signal, collapse, name):
        plt.plot(time, macd, label="macd", color='blue')
        plt.plot(time, signal, label="signal", color='red')
        plt.plot(time, collapse, label="collapse", color='pink')
        plt.ylabel('Wartość składowych (' + name + ')')
        plt.xlabel('Data (yyyy-mm)')
        plt.title('Wskaźnik MACD')
        plt.legend()
        plt.grid(True)
        plt.savefig('./images/' + name + '_macd&collapse' + '.png')
        plt.show()

    def show_company_shares_value_diagram(self, time, data, name):
        plt.plot(time, data, label="Akcja", color='blue')
        plt.ylabel('Akcja (' + name + '/PLN)')
        plt.xlabel('Data (yyyy-mm)')
        plt.title('Akcja ' + name)
        plt.legend()
        plt.grid(True)
        plt.savefig('./images/' + name + '_shares' + '.png')
        plt.show()


df = Data(ticker)
df.init_data()
time, share_price = df.get_data()
Plot.show_company_shares_value_diagram(Plot(), time, share_price, df.get_name())

macd = MACD(share_price)
macd.print()
Plot.show_macd_signal_diagram(Plot(), time[26::], macd.getMacd(26), macd.getSignal(), df.get_name())
Plot.show_macd_signal_collapse_diagram(Plot(), time[26::], macd.getMacd(26), macd.getSignal(), macd.getCollapse(),
                                       df.get_name())
