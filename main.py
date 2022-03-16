import csv
from Macd import MACD
from Data import Data
from Plot import Plot


import pandas as pd
import numpy as np
from datetime import datetime
import tushare as ts
from matplotlib import pyplot as plt
import pyEX as p
import yfinance as yf
from dateutil import parser

if __name__ == "__main__":
    # company ticker
    ticker = 'AAPL'

    # data initialization
    df = Data(ticker)
    df.init_data()
    time, share_price = df.get_data()
    # draw raw company shares value
    Plot.show_company_shares_value_diagram(Plot(), time,
                                           share_price,
                                           df.get_name())

    # initialize and calculate MACD
    macd = MACD(share_price)
    macd.print()
    # draw a plot with MACD index and SIGNAL
    Plot.show_macd_signal_diagram(Plot(), time[26::],
                                  macd.getMacd(26),
                                  macd.getSignal(),
                                  df.get_name())
    # draw a plot with MACD index, SIGNAL and points to sell/buy
    Plot.show_macd_signal_collapse_diagram(Plot(), time[26::],
                                           macd.getMacd(26),
                                           macd.getSignal(),
                                           macd.getCollapse(),
                                           df.get_name())
