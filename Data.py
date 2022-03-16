import csv
import yfinance as yf
from dateutil import parser

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
        df.to_csv('./data/' + self.__name + '.csv')
        # hist.to_csv('./data/' + ticker + '.csv')
        # View our data
        print(df)
        # print(hist)