import numpy as np
from matplotlib import pyplot as plt

x=np.arange(0,2*np.pi,0.2)

y1=np.sin(x)
y2=np.cos(x)

plt.plot(x,y1,'r--',label='Sin(x)')
plt.plot(x,y2,'g+',label='Cos(x)')

plt.xlabel('X values(rads)')
plt.ylabel('sin(x) or cos(x)')

plt.legend()  #this add line details box

plt.title('Trig Functions')
plt.savefig('sin(x) and cos(x).png')    #save graph as .png file in our code directory

plt.show()

