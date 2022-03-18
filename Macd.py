

class MACD:
    __macd = []
    __signal = []
    __money = 0
    # TODO delete __collapse
    __collapse = []

    # TODO more comments in macd & sell/buy
    def __init__(self, share_price):
        self.__macd = []
        self.__collapse = []
        for i in range(len(share_price)):
            if i >= 26:
                self.calc_macd(share_price, i)
            else:
                self.__macd.append(float(0))
        self.calc_signal()
        for i in range(len(share_price)):
            if i >= 26:
                self.isCollapse(i)

    def print(self):
        print(self.__macd)
        print(self.__signal)
        print(self.__collapse)

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

    def calc_macd(self, share_price, i):
        temp_ema12 = self.calc_ema(12, share_price, i)
        temp_ema26 = self.calc_ema(26, share_price, i)

        self.__macd.append(temp_ema12 - temp_ema26)

    def calc_signal(self):
        self.__signal = []
        for i in range(26, len(self.__macd)):
            self.__signal.append(self.calc_ema(9, self.__macd, i))

    def getMacd(self, n=0):
        return self.__macd[n::]

    def getSignal(self, n=0):
        return self.__signal[n::]

    # funkcja pomocnicza ktora pokazuje kiedy musimy kupic/sprzedac akcji
    def isCollapse(self, i):
        if self.__macd[i - 1] > self.__signal[i - 26 - 1] and self.__macd[i] < self.__signal[i - 26]:
            # sell
            self.__collapse.append(self.__signal[i - 26])
        elif self.__macd[i - 1] < self.__signal[i - 26 - 1] and self.__macd[i] > self.__signal[i - 26]:
            # buy
            self.__collapse.append(self.__signal[i - 26 - 1])
        else:
            self.__collapse.append(float(0))

    def getCollapse(self, n=0):
        return self.__collapse[n::]

    def lazyMoney(self, share_price, money):
        self.__money = money
        currency = 0
        for i in range(len(share_price)):
            if i >= 26:
                if self.__macd[i - 1] > self.__signal[i - 26 - 1] and self.__macd[i] < self.__signal[i - 26]:
                    # sell
                    if self.__money != 0:
                        currency = float(self.__money / share_price[i])
                        self.__money = 0
                elif self.__macd[i - 1] < self.__signal[i - 26 - 1] and self.__macd[i] > self.__signal[i - 26]:
                    # buy
                    if currency != 0:
                        self.__money = currency * share_price[i]
                        currency = 0
        # jesli sprzedalismy akcji to musimy ich kupic zeby zdobyc zysk
        if self.__money == 0:
            return float(currency * share_price[len(share_price)-1])
        else:
            return self.__money

