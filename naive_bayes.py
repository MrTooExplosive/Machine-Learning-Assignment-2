#-------------------------------------------------------------------------
# AUTHOR: Makarius Salib
# FILENAME: naive_bayes.py
# SPECIFICATION: Makes and tests a naive bayes model
# FOR: CS 4210- Assignment #2
# TIME SPENT: 30 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB

#reading the training data in a csv file
#--> add your Python code here
file = open("weather_training.csv", 'r')
data = file.readlines()
data = data[1:]
for i in range(len(data)):
    data[i] = data[i].rstrip('\n')
    data[i] = data[i].split(',')
    print(data[i])
file.close()

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =
X = []
for instance in data:
    sample = []
    if instance[1] == "Sunny":
        sample.append(1)
    elif instance[1] == "Overcast":
        sample.append(2)
    elif instance[1] == "Rain":
        sample.append(3)

    if instance[2] == "Cool":
        sample.append(1)
    elif instance[2] == "Mild":
        sample.append(2)
    elif instance[2] == "Hot":
        sample.append(3)

    if instance[3] == "Normal":
        sample.append(1)
    elif instance[3] == "High":
        sample.append(2)

    if instance[4] == "Weak":
        sample.append(1)
    elif instance[4] == "Strong":
        sample.append(2)
    X.append(sample)

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =
Y = []
for instance in data:
    if instance[5] == "No":
        Y.append(0)
    else:
        Y.append(1)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
#--> add your Python code here
file = open("weather_test.csv", 'r')
tests = file.readlines()
tests = tests[1:]
for i in range(len(tests)):
    tests[i] = tests[i].rstrip('\n')
    tests[i] = tests[i].split(',')
    print(tests[i])
file.close()

#printing the header os the solution
#--> add your Python code here
print("Day", "Outlook", "\tTemperature", "Humidity", "Wind", "PlayTennis", "Confidence", sep='\t')

#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here
for instance in tests:
    sample = []

    if instance[1] == "Sunny":
        sample.append(1)
    elif instance[1] == "Overcast":
        sample.append(2)
    elif instance[1] == "Rain":
        sample.append(3)

    if instance[2] == "Cool":
        sample.append(1)
    elif instance[2] == "Mild":
        sample.append(2)
    elif instance[2] == "Hot":
        sample.append(3)

    if instance[3] == "Normal":
        sample.append(1)
    elif instance[3] == "High":
        sample.append(2)

    if instance[4] == "Weak":
        sample.append(1)
    elif instance[4] == "Strong":
        sample.append(2)

    prediction = clf.predict_proba([sample])[0]
    clasification = "Unsure"
    conf = "NA"
    if prediction[0] >= .75:
        classification = "No"
        conf = prediction[0]
    elif prediction[1] >= .75:
        classification = "Yes"
        conf = prediction[1]

    print(instance[0],instance[1], instance[2] if instance[1] == "Overcast" else '\t' + instance[2], '\t' + instance[3], '\t' + instance[4], clasification, '\t' + str(conf if conf == "NA" else round(conf, 3)),sep='\t')
