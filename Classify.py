import pickle
import numpy as np
from knn import KNN

knn = KNN()

def Load_Pickle(filename):
    with open(filename, 'r') as dataFile:
        data = pickle.load(dataFile)
    return(data)

def ReduceData(X):
    X = np.delete(X,1,1)
    X = np.delete(X,1,1)
    return(X)

def ReshapeData(set1, set2):

    X = np.zeros((2000, 5*4*6), dtype='f')
    for row in range(1000):
        col = 0
        for finger in range(5):
            for bone in range(2):
                for joint in range(6):
                    X[row, col] = set1[finger,bone,joint,row]
                    X[row+1000, col] = set2[finger,bone,joint,row]
                    col = col + 1
                    
    Y = np.zeros(2000)
    Y[:1000] = 4
    Y[1000:] = 5
    
    return(X, Y)
    

train_4 = Load_Pickle(ReduceData("gesture_4_train.p"))
test_4 = Load_Pickle(ReduceData("gesture_4_test.p"))

train_5 = Load_Pickle(ReduceData("gesture_5_train.p"))
test_5 = Load_Pickle(ReduceData("gesture_5_test.p"))
    
trainX, trainY = ReshapeData(train_4, train_5)
testX, testY = ReshapeData(test_4, test_5)

K = 15

knn.Use_K_Of(15)
knn.Fit(trainX, trainY)


accuracy = 0
for row in range(2000):

    prediction = int(knn.Predict(testX[row,:]))
    if prediction == testY[row]:
        accuracy += 1
        
accuracy /= 2000.0
print(accuracy)


