import numpy as np
from matplotlib import pyplot as plt

x=np.arange(-10,11,1)
x=x[:,np.newaxis]
y=2*(x**2)+3*x

plt.plot(x,y,'r')

ye=[]

for i in y:
    ye.append(i+np.random.randint(-5,5))

ye=np.array(ye)


#plt.plot(x,y)
plt.scatter(x,ye)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

clsfr=LinearRegression()
poly=PolynomialFeatures(degree=2,include_bias=False)

xnew=poly.fit_transform(x)

results=clsfr.fit(xnew,ye)
#clsfr.fit([x],[ye])

m=clsfr.coef_[0]
c=clsfr.intercept_

print(m,c)

x_vals=np.arange(-10,11,1)
y_vals=m[0]*x_vals + m[1]*(x_vals**2)
plt.plot(x_vals,y_vals,'g')

plt.show()
