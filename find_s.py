#-------------------------------------------------------------------------
# AUTHOR: William Armstrong
# FILENAME: find_s.py
# SPECIFICATION: Derives the maximally specific hypothesis from training data in a CSV file
# FOR: CS 4200- Assignment #1
# TIME SPENT: ~10 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)

#find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")
for row in db:
    if row[4] == "Yes":
        if (hypothesis[0] == '0'):
            hypothesis = row[0:num_attributes]
        else:
            for i in range(0, num_attributes):
                if (row[i] != hypothesis[i]):
                    hypothesis[i] = '?'

print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)
