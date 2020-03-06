import numpy as np
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-5,5,0.01)
y = np.sqrt(x)
plt.plot(x,y)
plt.legend("Power function",loc = "upper left")

x = np.arange(-5,5,0.01)
y = 2**x
plt.plot(x,y)

x = np.linspace(0,10,100)
fig = plt.figure()
plt.plot(x,np.sin(x),color="orange")
plt.plot(x,np.cos(x),color="red")
plt.xlabel("x")
plt.ylabel("sinx&cosx")
#plt.plot(x,np.tan(x))

x = np.arange(-0.49*np.pi,0.49*np.pi,0.01)
y = np.tan(x)
plt.plot(x,y)

x = np.linspace(-5,5,100)
y = [np.arctan(i) for i in x]
plt.plot(x,y)
plt.grid()

x = np.linspace(-1,1,100)
y1 = [np.arcsin(i) for i in x]

plt.plot(x,y1)
plt.grid()

y2 = [np.arccos(i) for i in x]
plt.plot(x,y2)
plt.grid()

