# use csv to save/rewrite data file
# use yfinance(yahoo finance) to get data via actions
# use parser to parse our data
import csv
import yfinance as yf
from dateutil import parser

# data class
class Data:
    # name = ticket
    __name = ''

    #TODO more comments in data

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_data(self):
        # open file
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
        df = yf.Ticker(self.__name).history(period='1y')[['Close']]
        # Save our data
        df.to_csv('./data/' + self.__name + '.csv')
        # View our data
        print(df)
