import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cross_validation
from src.parameters import spam_file

# ML methods
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

#                                   SPAM PROBLEM
# ------------------------------------------------------------------------------------
dataFrame = pd.read_csv(spam_file)

# features (attributes)
x = np.array(dataFrame.drop(['class'], 1))

# labels
y = np.array(dataFrame['class'])

# configuration for cross validation test harness
number_of_folds = 10
number_of_instances = len(x)
# seed ensures we have the same sequence of random numbers
seed = 7

# ML methods - Decision Tree, Naive Bayes, Support Vector Machines, Neural Networks, Random Forest
methods = [('Decision tree', DecisionTreeClassifier()),
           ('Naive Bayes', GaussianNB()),
           # SVM - Support vector machines
           ('SVM', SVC()),
           # DNN - Deep neural network with 5 hidden layers, each of the layers has 5 neurons
           ('DNN', MLPClassifier(hidden_layer_sizes=(5, 5, 5, 5, 5))),
           ('Random forest', RandomForestClassifier()),
           ]

# evaluate each method in turn
results = []
# ML methods names
methods_names = []
scoring = 'accuracy'

for name, method in methods:

    # noinspection PyDeprecation
    k_fold = cross_validation.KFold(n=number_of_instances, n_folds=number_of_folds, random_state=seed)
    # noinspection PyDeprecation
    cv_results = cross_validation.cross_val_score(method, x, y, cv=k_fold, scoring=scoring)

    results.append(cv_results)
    methods_names.append(name)

    print("\t\t%s" % name)

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
