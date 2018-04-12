#import Tkinter as tk
#from Tkinter import *
#import ttk
#import matplotlib.pyplot as plt

import numpy as np
import talib as ta
import sys,os
import tushare as ts
#def ma():
# close = np.array([[5, 10, 15],                  [20, 25, 30],                  [35, 40, 45]])[:,0]
# sma = ta.SMA(close,3)
# print (sma[0])
def zw_stk_down_base():
    rss="d:\\tmp\\"
    fss=rss+'stk_base.csv';print(fss)
    dat = ts.get_stock_basics()
    dat.to_csv(fss,encoding='gbk')
    c20=['code','name','industry','area']
    d20=dat.loc[:,c20]
    d20['code']=d20.index
    fss=rss+'stk_code.csv';print(fss)
    d20.to_csv(fss,index=False,encoding='gbk')

def zw_stk_down_50():
    #上证50成份股，上证规模大、流动性好的50只股票，优质大盘企业
    #上证50，指数代码000016
    rss = "d:\\tmp\\"
    fss = rss+'stk_sz50.csv'
    print(fss)
    dat = ts.get_sz50s()
    dat.to_csv(fss, index=False, encoding='gbk')
def get_one():
    rss = "d:\\tmp\\"
    fss = rss + '000008_60.csv'
    df = ts.get_hist_data('000008',ktype= '60')
    # print (df)
    # sma = ta.SMA(df['close'], 3)
    # rsi = ta.RSI(df['close'])
    df.to_csv(fss, index=False, encoding='gbk')
    # print(rsi)
if __name__ == '__main__':
    get_one()

