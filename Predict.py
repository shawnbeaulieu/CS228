import numpy as np
import matplotlib.pyplot as plt
from knn import KNN

knn = KNN()

knn.Load_Dataset('iris.csv')

x = knn.data[:,0]
y = knn.data[:,1]

trainX = knn.data[::2, 1:3]
trainy = knn.target[::2]

testX = knn.data[1::2, 1:3]
testy = knn.target[1::2]

colors = np.zeros((3,3), dtype='f')
colors[0,:] = [1,0.5,0.5]
colors[1,:] = [0.5, 1, 0.5]
colors[2,:] = [0.5, 0.5, 1]

#plt.scatter(trainX[:,0], trainX[:,1], c=trainy)
#plt.show()

#plt.scatter(testX[:,0], testX[:,1], c=testy)
#plt.show()

knn.Use_K_Of(15)
knn.Fit(trainX, trainy)

actualClass = testy[70]
prediction = knn.Predict(testX[70, 1:3])
print(actualClass, prediction)

[numItems, numFeatures] = knn.data.shape

for i in range(0, numItems/2):
    itemClass = int(trainy[i])
    currColor = colors[itemClass,:]
    plt.scatter(trainX[i,0], trainX[i,1], facecolor=currColor, s=50, lw=2)


counter = 0
for i in range(0, numItems/2):
    itemClass = int(testy[i])
    currColor = colors[itemClass,:]
    prediction = int(knn.Predict(testX[i,1:3]))
    if prediction == int(testy[i]):
        counter += 1
    edgeColor = colors[prediction,:]
    plt.scatter(testX[i,0], testX[i,1], facecolor=currColor, s=50, lw=2, edgecolor=edgeColor)

plt.show()
print(counter/float(75))
