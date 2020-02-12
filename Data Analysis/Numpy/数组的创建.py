import numpy as np

#使用numpy生成数组，得到ndarry的类型
t1 = np.array([1,2,3])
print(t1)
print(type（t1))

t2 = np.array(range(10))
print(t2)
print(type(t2))

t3 = np.arange(4,10,2)
print(t3)
print(type(t3))

print(t3.dtype)

#numpy中数据类型
t4 = np.array(range(1,4),dtype=float)
print(t4)

t5 = np.array([1,1,0,1,0,0],dtype=bool)
print(t5)
print(t5.dtype)


#调整数据类型
t6 = t5.astype("int8")
print(t6)
print(t6.dtype)

#numpy中的小数

np.round(传入的数组，保留位数)
np.round(b,3)
