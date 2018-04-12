import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import talib

df=ts.get_hist_data('600848',start='2017-01-01',end='2018-04-10')
df=df.sort_index()
df.index=pd.to_datetime(df.index,format='%Y-%m-%d')
#收市股价
close= df.close
#每天的股价变动百分率
ret=df.p_change/100
 # 调用talib计算MACD指标
df['DIFF'],df['DEA'],df['MACD'] = talib.MACD(np.array(close),
                            fastperiod=12, slowperiod=26, signalperiod=9)


diff=df.DIFF
dea=df.DEA

#处理信号
macdSignal=pd.Series(0,index=close.index)

for i in range(10,len(close)):
    #if all([diff[i]>dea[i]>0,diff[i-1]<dea[i-1]]):
    if all([diff[i]>dea[i]]):
        macdSignal[i]=1
    #elif all([diff[i]<dea[i]<0,diff[i-1]>dea[i-1]]):
        #macdSignal[i]=-1


macdTrade=macdSignal.shift(1).dropna()
macdRet=ret*macdTrade.dropna()

#累积收益表现
#股票累积收益率
cumStock=np.cumprod(1+ret[macdRet.index[0]:])-1
#策略累积收益率
cumTrade=np.cumprod(1+macdRet)-1
plt.rcParams['font.sans-serif']=['SimHei']
plt.plot(cumStock,label="cumStock",color='k')
plt.plot(cumTrade,label="cumTrade",color='r',linestyle=':')
plt.title("股票累积收益率与macd策略收益率")
plt.legend()
plt.show()