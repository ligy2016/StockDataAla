# 导入相关第三方库
import numpy as np
import statsmodels.tsa.stattools as sts
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm

#生成X、Y两个随机序列，展示随机序列分布
X = np.random.randn(1500)
Y = np.random.randn(1500)

#画出坐标点
plt.scatter(X,Y)
plt.show()
print("correlation of X and Y is ")
np.corrcoef(X,Y)[0,1]