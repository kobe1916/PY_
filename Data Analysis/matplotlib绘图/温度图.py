
#问题  列表a表示10—12点每一分钟温度，如何绘制折线图观察每一分钟气温变化情况
a = [random.randint(20,35) for i in range(120)
from matplotlib import pyplot as plt
import random

x = range(0,120)
y = [random.randint(20,35)for i in range(120)]

plt.figure(figsize(20,8),dpi = 80)
plt.plot(x,y)
plt.show()

    
     
     
from matplotlib import pyplot as plt
import random
import matplotlib

#windows和linux设置字体方法
font = {'family':'MicroSoft YaHei;,
        'weight':'bold',
        'size':'larger'}
matplotlib.rc("font",**font)
matplotlib.rc("font",family = 'MicroSoft YaHei',weight = "bold")
x = range(0,120)
y = [random.randint(20,35)for i in range(120)]

plt.figure(figsize(20,8),dpi = 80)
plt.plot(x,y)
#设置x轴刻度  列表才能取步长
_xtick_lables = ["10d点{}分".format(i) for i in range(60)]
_xtick_lables += ["11点{}分".format(i60) for i in range(60)]
#双步长，数字和字符串一一对应，数据长度一样
plt.xticks(list(x)[::3],_xtick_lables[::3],rotation=90,fontproperties = my_font)#rotation旋转的度数

plt.show()

'''
#matplotlib默认支持英文  不支持中文
查看Linux支持字体
fc-list  查看支持字体
fc-list :lang=zh  查看支持的中文

如何修改matplotlib的默认字体
matplotlib.rc  可以修改
matplotlib下的font_manager可以解决
'''
     
     
