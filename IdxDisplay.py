import matplotlib.pyplot as plt
import numpy as np
import talib as ta
import tushare as ts

def Idx():
    df = ts.get_hist_data('601228', start='2017-04-08', end='2018-04-07')
    close = np.array(df['close'][::-1].astype(float))
    fig, axes = plt.subplots(2, 1, sharex=True)
    ax1, ax2 = axes[0], axes[1]

    macd, macdsignal, macdhist = ta.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
    axes[0].plot(close, 'r-')
    axes[1].plot(macd, 'g-')
    plt.show()

if __name__ == '__main__':
    Idx()
