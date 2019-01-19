from sklearn import datasets #importing sckit learn datasets (toy dataset)

iris=datasets.load_iris()   #import the iris data set(table) into iris
data=iris.data              #spliting the data
target=iris.target          #spliting the targets

#print setosa row 1
print(data[0])  
print(target[0])

import numpy as np

test_smpls=[0,50,100]

#call delete function in numpy
train_data=np.delete(data,test_smpls,axis=0)
train_target=np.delete(target,test_smpls)

from sklearn import neighbors       #import scikit learn neighbors 

clsfr=neighbors.KNeighborsClassifier()      #load the K.neighbors classifier
clsfr.fit(train_data,train_target)          #training the classifier

test_data=data[test_smpls]      #test removed three data(get removed data)

results=clsfr.predict(test_data)
print("Predicted results:",results)     #print predicted results

test_target=target[test_smpls]  #test actual results according to removed three data(get removed data)

results=clsfr.predict(test_data)
print("Actual data:",results)       #print actual results
