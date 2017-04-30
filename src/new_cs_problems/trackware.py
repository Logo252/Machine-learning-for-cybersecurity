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
from sklearn.svm import SVC  # SVM - Support Vector Machines
from sklearn.ensemble import AdaBoostClassifier


def run_script():
    """
    Runs the script as the standalone program
    """
    data_frame = pd.read_csv(trackware_file, sep=', ', engine='python')

    # Features
    features = np.array(data_frame.drop(['class'], 1))

    # Labels
    labels = np.array(data_frame['class'])

    # Configuration for cross validation test harness
    number_of_folds = 10
    number_of_instances = len(features)

    # Seed ensures we have the same sequence of random numbers
    seed = 7

    ml_methods = [('K-Nearest neighbors', KNeighborsClassifier()),
                  ('Decision tree', DecisionTreeClassifier()),
                  ('Naive Bayes', GaussianNB()),
                  ('Logistic regression', LogisticRegression()),
                  ('SVM', SVC()),
                  ('AdaBoost', AdaBoostClassifier()),
                  ]

    evaluate_methods_for_trackware(ml_methods=ml_methods,
                                   number_of_instances=number_of_instances,
                                   number_of_folds=number_of_folds,
                                   seed=seed,
                                   features=features,
                                   labels=labels
                                   )


def evaluate_methods_for_trackware(ml_methods, number_of_instances,
                                   number_of_folds, seed, features, labels):
    """
    Evaluates machine learning methods for cs problem - trackware
    :param ml_methods: machine learning methods
    :param number_of_instances: number of instances
    :param number_of_folds: number of folds
    :param seed: seed
    :param features: features
    :param labels: labels
    """
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
                                                      features,
                                                      labels,
                                                      cv=k_fold,
                                                      scoring=scoring)

        results.append(cv_results)
        methods_names.append(name)

        print("\t\t%s" % name)

        # Mean accuracy and standard deviation accuracy
        accuracy_message = "Mean accuracy (standard deviation accuracy): " \
                           "%.3f (+/- %.3f)\n" % (
                               cv_results.mean() * 100, cv_results.std() * 100)
        print(accuracy_message)

    show_plot_of_algorithms_results(methods_names=methods_names,
                                    results=results)


def show_plot_of_algorithms_results(methods_names, results):
    """
    Shows plot of machine learning algorithms results
    :param methods_names: Machine learning methods names
    :param results: Results got from applying methods for trackware
    :return: 
    """
    fig = plt.figure()

    # Add a subplot to the new figure, 111 means "1x1 grid, first subplot"
    ax = fig.add_subplot(111)
    plt.boxplot(results)

    # x axis title
    plt.xlabel('Machine learning algorithms')

    # y axis title
    plt.ylabel('Accuracy')

    plt.title('Machine learning algorithms applied for trackware')
    # Name of each box
    ax.set_xticklabels(methods_names)

    # Change font size of the text
    plt.rcParams.update({'font.size': 23})

    # Show box plot
    plt.show()


if __name__ == "__main__":
    run_script()
