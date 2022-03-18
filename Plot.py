import matplotlib.pyplot as plt

class Plot:
    # TODO more comments in plot & change functions
    def show_macd_signal_diagram(self, time, macd, signal, name):
        plt.plot(time, macd, label="macd", color='blue', linewidth=0.4)
        plt.plot(time, signal, label="signal", color='red', linewidth=0.4)
        plt.ylabel('Wartość składowych (' + name + ')')
        plt.xlabel('Data (yyyy-mm)')
        plt.title('Wskaźnik MACD')
        plt.legend()
        plt.minorticks_on()
        plt.grid(which='major')
        plt.grid(which='minor', linestyle=':')
        plt.savefig('./images/' + name + '_macd' + '.png', dpi=300)
        plt.show()

    def show_macd_signal_collapse_diagram(self, time, macd, signal, collapse, name):
        plt.plot(time, macd, label="macd", color='blue', linewidth=0.5)
        plt.plot(time, signal, label="signal", color='red', linewidth=0.5)
        plt.plot(time, collapse, label="collapse", color='pink', linewidth=0.5)
        plt.ylabel('Wartość składowych (' + name + ')')
        plt.xlabel('Data (yyyy-mm)')
        plt.title('Wskaźnik MACD')
        plt.legend()
        plt.minorticks_on()
        plt.grid(which='major')
        plt.grid(which='minor', linestyle=':')
        plt.savefig('./images/' + name + '_macd&collapse' + '.png', dpi=300)
        plt.show()

    def show_company_shares_value_diagram(self, time, data, name):
        plt.plot(time, data, label="Akcja", color='blue', linewidth=0.5)
        plt.ylabel('Akcja (' + name + '/PLN)')
        plt.xlabel('Data (yyyy-mm)')
        plt.title('Akcja ' + name)
        plt.legend()
        plt.minorticks_on()
        plt.grid(which='major')
        plt.grid(which='minor', linestyle=':')
        plt.savefig('./images/' + name + '_shares' + '.png', dpi=300)
        plt.show()