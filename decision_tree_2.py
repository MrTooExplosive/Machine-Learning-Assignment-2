#-------------------------------------------------------------------------
# AUTHOR: Makarius Salib
# FILENAME: decision_tree_2.py
# SPECIFICATION: Create and test three different decision tree models
# FOR: CS 4210- Assignment #2
# TIME SPENT: 20 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:
    
    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =

    for i in range(len(dbTraining)):
        instance = []
        if dbTraining[i][0] == "Young":
            instance.append(1)
        elif dbTraining[i][0] == "Prepresbyopic":
            instance.append(2)
        elif dbTraining[i][0] == "Presbyopic":
            instance.append(3)
        
        if dbTraining[i][1] == "Myope":
            instance.append(1)
        elif dbTraining[i][1] == "Hypermetrope":
            instance.append(2)

        if dbTraining[i][2] == "No":
            instance.append(1)
        elif dbTraining[i][2] == "Yes":
            instance.append(2)

        if dbTraining[i][3] == "Reduced":
            instance.append(1)
        elif dbTraining[i][3] == "Normal":
            instance.append(2)

        X.append(instance)
    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =
    for i in range(len(dbTraining)):
        if dbTraining[i][4] == "No":
            Y.append(2)
        elif dbTraining[i][4] == "Yes":
            Y.append(1)

    totalAcc = 0
    #loop your training and test tasks 10 times here
    for i in range (10):

        #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       #--> add your Python code here
       # dbTest =

           #reading the training data in a csv file
        with open('contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0: #skipping the header
                    dbTraining.append (row)

        dbTest = []
        for i in range(len(dbTraining)):
            instance = []
            if dbTraining[i][0] == "Young":
                instance.append(1)
            elif dbTraining[i][0] == "Prepresbyopic":
                instance.append(2)
            elif dbTraining[i][0] == "Presbyopic":
                instance.append(3)
            
            if dbTraining[i][1] == "Myope":
                instance.append(1)
            elif dbTraining[i][1] == "Hypermetrope":
                instance.append(2)

            if dbTraining[i][2] == "No":
                instance.append(1)
            elif dbTraining[i][2] == "Yes":
                instance.append(2)

            if dbTraining[i][3] == "Reduced":
                instance.append(1)
            elif dbTraining[i][3] == "Normal":
                instance.append(2)

            if dbTraining[i][4] == "No":
                instance.append(2)
            elif dbTraining[i][4] == "Yes":
                instance.append(1)

            dbTest.append(instance)

        count = 0
        for data in dbTest:
           #transform the features of the test instances to numbers following the same strategy done during training,
           #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
           #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here
            prediction = clf.predict([data[:-1]])[0]

           #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
           #--> add your Python code here
            if prediction == data[-1]:
                count += 1

        totalAcc += count / len(dbTest)

    #find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here
    avg = totalAcc / 10

    #print the average accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    print("final accuracy when training on " + ds + ':', avg)




