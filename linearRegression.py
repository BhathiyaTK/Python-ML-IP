train_data=[[78],[76],[45],[63],[75],[80],[80],[75],[59],[52],[45],[88],[50],[58],[45],[50],[42],[70],[65],[69],[60],[72]]
train_target=[[180],[175],[165],[172],[174],[170],[172],[170],[170],[160],[150],[175],[160],[150],[160],[146],[162],[165],[158],[175],[160],[163]]

from matplotlib import pyplot as plt

plt.scatter(train_data,train_target,label='Train data vs. Train target')
plt.xlabel('weight(kg)')
plt.ylabel('height(cm)')

from sklearn.linear_model import LinearRegression

clsfr=LinearRegression()        #loading a linear regression model
clsfr.fit(train_data,train_target)      #it needs to pass data & target in 2d arrays

result=clsfr.predict([[84],[78],[60]])

m=clsfr.coef_[0]       #gradient
c=clsfr.intercept_  #intercept

import numpy as np

x=np.arange(40,90,2)
y=m*x+c

plt.plot(x,y,'r',label='Best-Fit-Line')
#plt.scatter(84,84*m+c)

from sklearn.metrics import r2_score

accuracy=r2_score([[182],[178],[165]],result)
print(accuracy)

plt.legend()

print(m,c)
#result(result)

plt.show()
