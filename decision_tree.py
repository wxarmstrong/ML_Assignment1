#-------------------------------------------------------------------------
# AUTHOR: William Armstrong
# FILENAME: decision_tree.py
# SPECIFICATION: Creates a decision tree from CSV test data
# FOR: CS 4200 - Assignment #1
# TIME SPENT: ~30 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
# X =
num_attributes = len(db[0])-1
valCounter = [1]*num_attributes
valdict = {}

print(valCounter)

for row in db:
    xRow = []
    for i, value in enumerate(row):
        if (i == num_attributes):
            break
        if value not in valdict:
            valdict[value] = valCounter[i]
            valCounter[i] = valCounter[i] + 1
        xRow.append(valdict[value])
    X.append(xRow)
    
print(X)
            
#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
# Y =

yCounter = 1
yDict = {}
for row in db:
    yval = row[num_attributes]
    if yval not in yDict:
        yDict[yval] = yCounter
        yCounter = yCounter + 1
    Y.append(yval)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()