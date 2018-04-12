# coding=gbk

import matplotlib.pyplot as plt  # �ṩ��matlab���ͼ���
import numpy as np
import pandas as pd
import tushare as ts

# ��ȡ����
s_qjd = '002186'  # ȫ�۵�
s_gm = '600597'  # ������ҵ
sdate = '2016-01-01'  # ��ֹ����
edate = '2016-12-31'
df_qjd = ts.get_h_data(s_qjd, start=sdate, end=edate).sort_index(axis=0, ascending=True)  # ��ȡ��ʷ����
df_gm = ts.get_h_data(s_gm, start=sdate, end=edate).sort_index(axis=0, ascending=True)
df = pd.concat([df_qjd.close, df_gm.close], axis=1, keys=['qjd_close', 'gm_close'])  # �ϲ�
df.ffill(axis=0, inplace=True)  # ���ȱʧ����
df.to_csv('qjd_gm.csv')

# pearson�������������
corr = df.corr(method='pearson', min_periods=1)
print(corr)

# ��ӡͼ��
df.plot(figsize=(20, 12))
plt.savefig('qjd_gm.png')
plt.close()

# ��һ�������ӡͼ��
df['qjd_one'] = df.qjd_close / float(df.qjd_close[0]) * 100
df['gm_one'] = df.gm_close / float(df.gm_close[0]) * 100
df.qjd_one.plot(figsize=(20, 12))
df.gm_one.plot(figsize=(20, 12))
plt.savefig('qjd_gm_one.png')