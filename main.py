# by Dzianis Dziurdz 187726 in 2022
from math import floor

from Macd import MACD
from Data import Data
from Plot import Plot

starting_money = 1000 # kapital poczatkowy

# main function
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
    #TODO money simulation
    money_lazy = macd.lazyMoney(share_price, starting_money)

    print(ticker + ", poczatkowy kapital: " + str(starting_money)
          + ", koncowy kapital: " + str(money_lazy))
