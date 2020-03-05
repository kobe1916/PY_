#计算集合的并、交、差
from sympy import*

x = symbols('x')  #将x定义为符号变量
X = solve(x**2-5*x+6,x)   #通过solve求解
print("一元二次方程根为：",X)

#定义集合
A = set('12345')
B = set('23')
print("集合AB的并：",A|B)
print("集合AB的交：",A&B)
print("集合AB的差：",A-B)



#判断数列是否收敛   limit(表达式，自变量，趋向，左右极限（+为右））
n = Symbol('n')
s = n/(n+1)
print('数列的极限为:',limit(s,n,oo))

#常函数求导   sympy.diff(表达式，自变量，求导阶数（默认为1））
from sympy import*
x = Symbol('x')
C = 2
y = C
print(diff(y,x))


#幂函数求导
x = Symbol('x')
mu = Symbol("mu")
y = x**mu
init_printing()  #使公式输出更美观
print(diff(y,x))

#指数函数求导、
x = Symbol('x')
a = Symbol('a')
y = a**x
print(diff(y,x))

#函数和的导数
x = Symbol('x')
u = log(x,2)
v = x**2+1
y = u+v
diff(y,x)

#函数差的导数
y = u-v
diff(y,x)

#函数积的导数
y = u*v
diff(y,x)

#函数商的导数
y = u/v
diff(y,x)

#复合函数求导
x = Symbol('x')
u = Symbol('u')
u = x**2
y = sin(u)
diff(y,x)


y = sin(x**2)
diff(y,x)

x = Symbol('x')
u = Symbol('u')
v = Symbol('v')
u = exp(x)
v = cos(u)
y = log(v)
diff(y,x)


y = log(cos(exp(x)))
diff(y,x)

#求微分同样用diff   只是少了dx   不影响理解
x = Symbol('x')
y = sin(2*x+1)
diff(y,x)

#微分在近似运算应用
#sin29
import numpy as np
x = (29/360)*2*np.pi   #设x=29
y = np.sin(x)
print(y)

#拐点  最值
from sympy import*
x = Symbol('x')
y = 2*x**3-12*x**2+18*x-2
df1 = diff(y,x,1)
df1    #一阶导

df2 = diff(y,x,2)
df2   #二阶导

print("令二阶导为0的x为",solve(df2,x))
print('函数拐点处值为:',y.subs(x,2))      #subs(x,2)赋值计算    给x赋值为2

#计算题5.
from sympy import*
x = Symbol('x')
y = 5*x**3+2*x**2-3*x
df1 = diff(y,x)
df2 = diff(y,x,2)
print(solve(df1,x))
print(solve(df2,x))

a = 1
b = 2
print("xxxx",a)
print("xxx%d"%a)
print("xxx {} xxxx {} ".format(a,b))

#不定积分
#  sympy.integrate(表达式，（自变量，上下限）)    通常结果少常数C  不影响理解
x = Symbol('x')
f= cos(x)
integrate(f,x)

x = Symbol('x')
f = 1/(1+x**2)
integrate(f,x)

#定积分
x = Symbol('x')
f = 1/(1+x**2)
integrate(f,x)

x = Symbol('x')
f = log(x)
integrate(f,(x,0,5))
