# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cross_validation
from src.parameters import trackware_file

# Importing ML classifiers
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier

#                                   TRACKWARE PROBLEM
# ------------------------------------------------------------------------------------
dataFrame = pd.read_csv(trackware_file, sep=', ')

# Features
x = np.array(dataFrame.drop(['class'], 1))

# Labels
y = np.array(dataFrame['class'])

# Configuration for cross validation test harness
number_of_folds = 10
number_of_instances = len(x)
# Seed ensures we have the same sequence of random numbers
seed = 7

'''
            ML methods
- K-Nearest neighbors
- Decision tree
- Naive Bayes
- Logistic regression
- SVM (Support Vector Machines)
- AdaBoost
'''
ml_methods = [('K-Nearest neighbors', KNeighborsClassifier()),
              ('Decision tree', DecisionTreeClassifier()),
              ('Naive Bayes', GaussianNB()),
              ('Logistic regression', LogisticRegression()),
              ('SVM', SVC()),
              ('AdaBoost', AdaBoostClassifier()),
              ]

# Evaluate each method in turn
results = []
methods_names = []
scoring = 'accuracy'

for name, method in ml_methods:
    # noinspection PyDeprecation
    k_fold = cross_validation.KFold(n=number_of_instances,
                                    n_folds=number_of_folds,
                                    random_state=seed)
    # noinspection PyDeprecation
    cv_results = cross_validation.cross_val_score(method,
                                                  x,
                                                  y,
                                                  cv=k_fold,
                                                  scoring=scoring)

    results.append(cv_results)
    methods_names.append(name)

    print("\t\t%s" % name)

    # Mean accuracy and standard deviation accuracy
    accuracy_message = "Mean accuracy (standard deviation accuracy): %.3f (" \
                       "+/- %.3f)\n" % (
                           cv_results.mean() * 100, cv_results.std() * 100)
    print(accuracy_message)

# box plot for comparison of algorithms
fig = plt.figure()
# add a subplot to the new figure, 111 means "1x1 grid, first subplot"
ax = fig.add_subplot(111)
plt.boxplot(results)
# x axis title
plt.xlabel('Machine learning algorithms')
# y axis title
plt.ylabel('Accuracy')
plt.title('Machine learning algorithms applied for trackware')
# name of each box
ax.set_xticklabels(methods_names)
# change font size of the text
plt.rcParams.update({'font.size': 23})
# show box plot
plt.show()
