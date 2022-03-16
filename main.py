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

ticker = 'AAPL'

df = Data(ticker)
df.init_data()
time, share_price = df.get_data()
Plot.show_company_shares_value_diagram(Plot(), time, share_price, df.get_name())

macd = MACD(share_price)
macd.print()
Plot.show_macd_signal_diagram(Plot(), time[26::], macd.getMacd(26), macd.getSignal(), df.get_name())
Plot.show_macd_signal_collapse_diagram(Plot(), time[26::], macd.getMacd(26), macd.getSignal(), macd.getCollapse(),
                                       df.get_name())
