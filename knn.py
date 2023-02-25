#-------------------------------------------------------------------------
# AUTHOR: Makarius Salib
# FILENAME: knn.py
# SPECIFICATION: Finds the error rate of a leave-one-out cross-validation 1NN model
# FOR: CS 4210- Assignment #2
# TIME SPENT: 15 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

errors = 0

#loop your data to allow each instance to be your test set
for test in db:

    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    #--> add your Python code here
    # X =
    X = []
    for i in range(len(db)):
       if db[i] != test:
          row = []
          for j in range(len(db[i][:-1])):
             row.append(int(db[i][:-1][j]))
          X.append(row)
    

    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    #--> add your Python code here
    # Y =
    Y  = []
    for i in range(len(db)):
       if db[i] != test:
          if db[i][-1] == '-':
             Y.append(0)
          else:
             Y.append(1)

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    #testSample =
    testSample = []
    for i in range(len(test[:-1])):
       testSample.append(int(test[i]))

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    class_predicted = clf.predict([testSample])[0]

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    if class_predicted != (0 if test[-1] == '-' else 1):
       errors += 1

#print the error rate
#--> add your Python code here
print("Error rate:", errors/len(db))






