# 课后习题2
from sympy import*
x = Symbol('x')
y = sqrt(x+sqrt(x+sqrt(x)))
diff(y,x)

x = Symbol('x')
y = sqrt((x-2)/(x-3))
diff(y,x)

x = Symbol('x')
y = (x/(1+x))**x
diff(y,x)

x = Symbol('x')
y = asin((1-x**2))
diff(y,x)
