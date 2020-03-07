from sympy import *
x = Symbol('x')
f = log(x)
integrate(f,x)

x = Symbol('x')
f = x*exp(-x)
integrate(f,x)

x = Symbol('x')
f = x*atan(x)
integrate(f,x)

x = Symbol('x')
f = x*cos(x/2)
integrate(f,x)

x = Symbol('x')
f = tan(x)
integrate(f,(x,0,pi/4))

x = Symbol('x')
f = sqrt(x)*(1-sqrt(x))
integrate(f,(x,0,1))

x = Symbol('x')
f = x**4*asin(x)
integrate(f,(x,-1,1))

x = Symbol('x')
f = exp(x)*(exp(x)-1)
integrate(f,(x,0,log(2)))

x = Symbol('x')
y = 5*x**3+2*x**2-3*x
df1 = diff(y,x)
df2 = diff(y,x,2)
print("曲线的极值点为：",solve(df1,x))
X = solve(df2,x)
print("曲线的拐点为：",X,y.subs(x,-2/15))

x = Symbol('x')
f = sin(x)/(1+sin(x)+cos(x))
integrate(f,x)

x = Symbol('x')
f = (1/x)*sqrt((1+x)/x)
integrate(f,x)

x = Symbol('x')
f = 
integrate(f,x)

x = Symbol('x')
f = exp(2*x)*sin(3*x)
integrate(f,x)

x = Symbol('x')
f = 1-(sin(x)**3)
integrate(f,(x,0,pi))

x = Symbol('x')
f = (x+2)/(x**2+2*x+2)
integrate(f,(x,-2,0))

x = Symbol('x')
f =sin(log(x))
integrate(f,(x,1,exp(1)))

x = Symbol('x')
f = exp(sqrt(x))
integrate(f,(x,0,1))

from matplotlib import pyplot as plt
import numpy as np
from sympy import*
fig = plt.figure(figsize=(20,8),dpi = 80) #设置图片大小

x=np.linspace(-5,5,1000)  #这个表示在-5到5之间生成1000个x值
y=[-2*i**3+6*i for i in x] 
plt.plot(x,y)  #用上述生成的1000个xy值对生成1000个点
plt.grid()


x = np.linspace(-5,5,100)
y = [sin(i)for i in x]
plt.plot(x,y)
plt.grid()
