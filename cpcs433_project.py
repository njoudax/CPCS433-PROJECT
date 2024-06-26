# -*- coding: utf-8 -*-
"""CPCS433_PROJECT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15KDdXAty1DXoaWvcJpS2asN2GsdvJVZh

#CPCS433_Project
"""

# Importing Libraries
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import metrics
import plotly.express as px
from matplotlib import pyplot
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.svm import SVC

"""## **Load The DataSet**"""

# Loading The Dataset
dataset = pd.read_csv('/content/riceClassification.csv')

# Print The Shape Of Data
dataset.shape

# Print The Data
dataset

# Print The Dataset Info
dataset.info()

"""## **Preprocess The Dataset**

**1. Missing Values**
"""

# Checking For Missing Values
dataset.isnull().sum()

"""There Is No Missing Value In Our DataSet

**2. Duplicated Values**
"""

# Checking For Duplicated Values
print('Number Of Duplicated Values In The Dataset: ', dataset.duplicated().sum())

"""There Is No Duplicated Value In Our DataSet

**3. Class Imbalance**
"""

# Check For Class Imbalance In The Dependent Variable
print (dataset['Class'].value_counts(ascending = True))

"""There Is No Class Imbalance In Our Dependent Variable, We Can See Clearly That The Count Of Class 0 Is 8200, And The Count Of Class 1 Is 9985 Which Shwos A Balance

Here Class 0 Means Jasmine Rice

and Class 1 Means Gonen Rice
"""

# Drop Unneeded Column Like ID
dataset = dataset.drop('id', axis = 1)

"""**4. Handle Outliers**"""

# Using IsolationForest To Detect And Fliter Out Outliers
clf = IsolationForest(random_state=1)
outliers = clf.fit_predict(dataset)
dataset = dataset[outliers == 1]

# Print The Shape After Flitering Outliers
dataset.shape

"""We Can See Clearly number of rows decrees from 18185 to 14779

**5. HeatMap**
"""

# Heatmap To Showcase The Correlation
sns.heatmap(dataset.corr(),cmap = "Purples", annot = True)

"""##Training the model"""

# Split The Values Of Independent Features(X) And Dependent Target(Y)
X = dataset.drop(columns = 'Class', axis = 1)
Y = dataset['Class']

# Splitting The Data Useing Splitting Ratio 70:30
X_train, X_test, Y_train , Y_test = train_test_split(X,Y,test_size = 0.3, random_state = 0 )

"""##Testing the model

**1. Random Foesrt**

**1.1 Accuracy**
"""

RandomForest_model = RandomForestClassifier()

# Fit Data To Random Forest Model
RandomForest_model.fit(X_train, Y_train)
Y_Train_Pred = RandomForest_model.predict(X_train)

# Print The Accuracy Score For Trainign
Train_Accuracy = metrics.accuracy_score(Y_train,Y_Train_Pred)
print ("Train Accuracy : %s" % "{0:.3%}".format(Train_Accuracy))


# Print The Accuracy Score For Testing
Y_Test_Pred = RandomForest_model.predict(X_test)
Test_Accuracy = metrics.accuracy_score(Y_test,Y_Test_Pred)
print ("Test Accuracy : %s" % "{0:.3%}".format(Test_Accuracy))

"""**1.2 Confusion Matrix**"""

# Compute Confusion Matrix
ConfusionMatrix = confusion_matrix(Y_test,Y_Test_Pred)

# Display Confusion Matrix Using A Heatmap
plt.figure(figsize = (8, 6))
sns.heatmap(ConfusionMatrix, annot = True, fmt = "d", cmap = "Purples", cbar = True)
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()

"""**2. Decision Tree**

**2.1 Accuracy**
"""

# Initialize the Decision Tree model with a specified maximum depth
dt_classifier = DecisionTreeClassifier(max_depth=5)  # You can change the depth here

# Fit the model on the training data
dt_classifier.fit(X_train, Y_train)

# Predict on the testing data
y_pred = dt_classifier.predict(X_test)

# Calculate the accuracy in percentage for the testing data
test_accuracy_percentage = accuracy_score(Y_test, y_pred) * 100

# Predict on the training data
y_pred2 = dt_classifier.predict(X_train)

# Calculate the accuracy in percentage for the training data
train_accuracy_percentage = accuracy_score(Y_train, y_pred2) * 100

# Evaluate and print the model accuracy for training data
print("Train Accuracy: %s" % "{0:.3%}".format(train_accuracy_percentage / 100))

# Evaluate and print the model accuracy for testing data
print("Test Accuracy: %s" % "{0:.3%}".format(test_accuracy_percentage / 100))

"""**2.2 Confusion Matrix**"""

# Compute Confusion Matrix
ConfusionMatrix = confusion_matrix(Y_test, y_pred)

# Display Confusion Matrix Using A Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(ConfusionMatrix, annot=True, fmt="d", cmap="Greens", cbar=True)
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()

"""**3. Random Foesrt**

**3.1 Accuracy**
"""

# Create SVM model
SVM_model = SVC()

# Fit data to SVM model
SVM_model.fit(X_train, Y_train)

# Predict on training data
Y_train_pred = SVM_model.predict(X_train)

# Print the accuracy score for training
train_accuracy = metrics.accuracy_score(Y_train, Y_train_pred)
print("Train Accuracy: %.3f%%" % (train_accuracy * 100))

# Predict on testing data
Y_test_pred = SVM_model.predict(X_test)

# Print the accuracy score for testing
test_accuracy = metrics.accuracy_score(Y_test, Y_test_pred)
print("Test Accuracy: %.3f%%" % (test_accuracy * 100))

"""**3.2 Confusion Matrix**

"""

# Compute Confusion Matrix
ConfusionMatrix = confusion_matrix(Y_test, Y_test_pred)
# Display Confusion• Matrix Using A Heatmap
plt.figure(figsize = (8, 6))
sns.heatmap(ConfusionMatrix, annot=True, fmt="d", cmap="Oranges", cbar=True)
plt.xlabel( 'Predicted Labels')
plt.ylabel('True Labels')
plt.title( 'Confusion Matrix')
plt. show()
