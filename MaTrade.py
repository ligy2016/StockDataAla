import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import talib

df=ts.get_hist_data('600848',start='2017-01-01',end='2017-12-31')
df=df.sort_index()
df.index=pd.to_datetime(df.index,format='%Y-%m-%d')
#收市股价
close= df.close
#每天的股价变动百分率
ret=df.p_change/100
# 10日的移动均线为目标
df['SMA_10'] = talib.MA(np.array(close), timeperiod=10)
close10=df.SMA_10

#处理信号
SmaSignal=pd.Series(0,index=close.index)
tmp = 0
for i in range(10,len(close)):

    if all([close[i]>close10[i],close[i-1]<close10[i-1]]):
        tmp= 1
    elif all([close[i]<close10[i],close[i-1]>close10[i-1]]):
        tmp=0
    SmaSignal[i] = tmp

SmaTrade=SmaSignal.shift(1).dropna()

# SmaBuy=SmaTrade[SmaTrade==1]
#
# SmaSell=SmaTrade[SmaTrade==-1]

SmaRet=ret*SmaTrade.dropna()

#累积收益表现
#股票累积收益率
# print(ret[SmaRet.index[0]:])

# cumStock=np.cumprod(1+ret[SmaRet.index[0]:])-1
cumStock=np.cumprod(1+ret[::])-1
#策略累积收益率
print(SmaRet.index[0])
cumTrade=np.cumprod(1+SmaRet)-1
plt.rcParams['font.sans-serif']=['SimHei']
plt.plot(cumStock,label="cumStock",color='k')
plt.plot(cumTrade,label="cumTrade",color='r',linestyle=':')
plt.title("股票累积收益率与10日平均策略收益率")
plt.legend()
plt.show()