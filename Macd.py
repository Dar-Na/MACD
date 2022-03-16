

class MACD:
    __macd = []
    __signal = []
    # TODO delete __collapse
    __collapse = []

    # TODO more comments in macd & sell/buy
    def __init__(self, exchange_rate):
        self.__macd = []
        self.__collapse = []
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
            self.__collapse.append(self.__signal[i - 26])
        elif self.__macd[i - 1] < self.__signal[i - 26 - 1] and self.__macd[i] > self.__signal[i - 26]:
            self.__collapse.append(self.__signal[i - 26 - 1])
        else:
            self.__collapse.append(float(0))


    def getCollapse(self, n=0):
        return self.__collapse[n::]
