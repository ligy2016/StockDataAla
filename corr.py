# coding=gbk

import matplotlib.pyplot as plt  # 提供类matlab里绘图框架
import numpy as np
import pandas as pd
import tushare as ts

# 获取数据
s_qjd = '002186'  # 全聚德
s_gm = '600597'  # 光明乳业
sdate = '2016-01-01'  # 起止日期
edate = '2016-12-31'
df_qjd = ts.get_h_data(s_qjd, start=sdate, end=edate).sort_index(axis=0, ascending=True)  # 获取历史数据
df_gm = ts.get_h_data(s_gm, start=sdate, end=edate).sort_index(axis=0, ascending=True)
df = pd.concat([df_qjd.close, df_gm.close], axis=1, keys=['qjd_close', 'gm_close'])  # 合并
df.ffill(axis=0, inplace=True)  # 填充缺失数据
df.to_csv('qjd_gm.csv')

# pearson方法计算相关性
corr = df.corr(method='pearson', min_periods=1)
print(corr)

# 打印图像
df.plot(figsize=(20, 12))
plt.savefig('qjd_gm.png')
plt.close()

# 归一化处理打印图像
df['qjd_one'] = df.qjd_close / float(df.qjd_close[0]) * 100
df['gm_one'] = df.gm_close / float(df.gm_close[0]) * 100
df.qjd_one.plot(figsize=(20, 12))
df.gm_one.plot(figsize=(20, 12))
plt.savefig('qjd_gm_one.png')