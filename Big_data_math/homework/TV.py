import pandas as pd
import numpy as np
from scipy import stats as sts

data = pd.read_csv("./tv.csv")
#print(data)
#print(type(data))

#data = np.loadtxt("./tv.csv")   np读取csv文件

# 集中趋势度量
print('众数为：',sts.mode(data,axis=None))
print('中位数为：',np.median(data))
print('下四分位数为：',sts.scoreatpercentile(data,25,interpolation_method='lower'))
print('上四分位数为：',sts.scoreatpercentile(data,75,interpolation_method='lower'))
print('简单算术平均数为：',sts.tmean(data))
# 离散趋势度量
print('样本方差为：',sts.tvar(data))
print('样本标准差为：',sts.tstd(data))
print('变异系数为：',sts.tstd(data)/sts.tmean(data))
# 偏度峰度的度量
print('偏度为：',sts.skew(data))
print('峰度为：',sts.kurtosis(data))
