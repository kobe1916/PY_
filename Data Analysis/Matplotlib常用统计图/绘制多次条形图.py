'''
绘制多次条形图
a = ["猩球崛起","敦刻尔克","蜘蛛侠","战狼2"]
b_16 = [15746,312,4497,319]
b_15=[12357,156,2045,158]
b_14=[2358,399,2348,362]
'''


from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font=font_manager

a = ["猩球崛起","敦刻尔克","蜘蛛侠","战狼2"]
b_16 = [15746,312,4497,319]
b_15=[12357,156,2045,158]
b_14=[2358,399,2348,362]

bar_width = 0.2

x_14=list(range(len(a)))
x_15=[i+bar_width for i in x_14]
x_16=[i+bar_width*2 for i in x_14]

plt.figure(figsize(20,8),dpi=80)

plt.bar(range(len(a)),b_14,width=bar_width,label="9.14")
plt.bar(x_15,b_15,width=bar_width,label="9.15")
plt.bar(x_16,b_16,width=bar_width,label="9.16")

#设置图例
plt.legend(prop=my_font)

#设置x轴刻度
plt.xticks(x_15,a,fontproperties=my_font)


#条形图用途：数量统计  频率统计
