
#问题  列表a表示10—12点每一分钟温度，如何绘制折线图观察每一分钟气温变化情况
a = [random.randint(20,35) for i in range(120)
from matplotlib import pyplot as plt
import random

x = range(0,120)
y = [random.randint(20,35)for i in range(120)]

plt.figure(figsize(20,8),dpi = 80)
plt.plot(x,y)
plt.show()
