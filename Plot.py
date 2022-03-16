from matplotlib import pyplot as plt

class Plot:
    # TODO more comments in plot & change functions
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