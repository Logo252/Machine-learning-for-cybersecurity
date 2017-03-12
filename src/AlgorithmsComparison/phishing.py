# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cross_validation
import datetime
from src.parameters import phishing_file

# ML methods
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

#                                   PHISHING PROBLEM
# ------------------------------------------------------------------------------------
dataFrame = pd.read_csv(phishing_file)

# features (attributes)
x = np.array(dataFrame.drop(['Result'], 1))

# labels
y = np.array(dataFrame['Result'])

# configuration for cross validation test harness
number_of_folds = 10
number_of_instances = len(x)
# seed ensures we have the same sequence of random numbers
seed = 7

# ML methods - Decision Tree, Naive Bayes, Support Vector Machines, Neural Networks, Random Forest, Logistic Regression
methods = [('Decision tree', DecisionTreeClassifier()),
           ('Naive Bayes', GaussianNB()),
           # SVM - Support vector machines
           ('SVM', SVC()),
           # DNN - Deep neural network with 5 hidden layers, each of the layers has 5 neurons
           ('DNN', MLPClassifier(hidden_layer_sizes=(5, 5, 5, 5, 5))),
           ('Random forest', RandomForestClassifier()),
           ('Logistic regression', LogisticRegression()),
           ]

# evaluate each method in turn
results = []
methods_names = []
scoring = 'accuracy'

for name, method in methods:

    # time now before algorithm performance
    time_before = datetime.datetime.now()

    # noinspection PyDeprecation
    k_fold = cross_validation.KFold(n=number_of_instances, n_folds=number_of_folds, random_state=seed)
    # noinspection PyDeprecation
    cv_results = cross_validation.cross_val_score(method, x, y, cv=k_fold, scoring=scoring)

    # time now after algorithm performance
    time_after = datetime.datetime.now()
    # elapsed time of algorithm performance
    difference = time_after - time_before
    elapsed_time = difference.total_seconds()

    results.append(cv_results)
    methods_names.append(name)

    print("\t\t%s" % name)
    print("Elapsed time: %.3f s" % elapsed_time)
    # Mean accuracy and standard deviation accuracy
    accuracy_message = "Mean accuracy: %.3f (+/- %.3f)\n" % (cv_results.mean()*100, cv_results.std()*100)
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
plt.title('Comparison of machine learning algorithms')
# name of each box
ax.set_xticklabels(methods_names)
# change font size of the text
plt.rcParams.update({'font.size': 23})
# show box plot
plt.show()
