from sympy import*
x = Symbol('x')
y = (x*83-x**2+x/2)**exp(1/x)-sqrt(x**6+1)
limit(y,x,oo)


x = Symbol('x')
y = sin(x)**tan(x)
limit(y,x,pi/2,dir='-')

x = Symbol('x')
y = ((4*x+3)/(4*x+1))**(2*x+5)
limit(y,x,oo)

x = Symbol('x')
y = ((1-1/2*x**2)**(2/3)-1)/x*log(1+x)
limit(y,x,0)
