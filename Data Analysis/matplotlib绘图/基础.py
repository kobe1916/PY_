from matplotlib import pyplot as plt

x = range(2,26,2)#数据在x轴的位置，是一个可迭代对象
y = [15,13,14,5,17,20,25,26,26,24,22,28,25]#数据在y轴的位置，是一个可迭代对象

plt.plot(x,y)  #传入x和y，通过plot绘制折线图
plt.show()#在执行程序时展示图形




import matplotlib.pyplot as plt

#设置图片大小
fig = plt.figure(figsize= (20,8),dpi = 80)   #dpi参数可以让图片更清晰
x = range(2,26,2)#数据在x轴的位置，是一个可迭代对象
y = [15,13,14,5,17,20,25,26,26,24,22,28,25]#数据在y轴的位置，是一个可迭代对象

plt.plot(x,y)  #传入x和y，通过plot绘制折线图
#设置x轴y轴刻度
_xtick_lables = [i/2 for i in range(4,49)]
plt.xticks(range(_xtick_lables[::3]))
plt.yticks(range(min(y),max(y)+1)

#保存
plt.savefig("./sig_size.png")

plt.show()#在执行程序时展示图形
