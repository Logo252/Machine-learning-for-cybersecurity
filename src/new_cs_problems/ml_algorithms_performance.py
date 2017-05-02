# -*- coding: utf-8 -*-

import numpy as np
# np.set_printoptions(threshold=np.inf)  # To show full numpy array for debugging

import pandas as pd
import matplotlib.pyplot as plt

# Importing cross_validation method
from sklearn import cross_validation

# Importing ML classifiers from sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC  # svm - Support Vector Machines
from sklearn.ensemble import AdaBoostClassifier

# Importing training data files for computer security issues
from src.parameters import GENERATED_SAMPLES_FILE_FOR_CONSTRUCTOR
from src.parameters import GENERATED_SAMPLES_FILE_FOR_TRACKWARE


def run_script():
    """
    Runs the script as the standalone program
    """
    # Configuration for cross validation test harness
    number_of_folds = 10

    # Seed ensures we have the same sequence of random numbers
    seed = 7

    ml_methods = [('K-Nearest neighbors', KNeighborsClassifier()),
                  ('Decision tree', DecisionTreeClassifier()),
                  ('Naive Bayes', GaussianNB()),
                  ('Logistic regression', LogisticRegression()),
                  ('SVM', SVC()),
                  ('AdaBoost', AdaBoostClassifier()),
                  ]

    # ----------------------------- For constructor issue -----------------------------
    data_frame = pd.read_csv(GENERATED_SAMPLES_FILE_FOR_CONSTRUCTOR, sep=', ', engine='python')

    # Features
    features = np.array(data_frame.drop(['class'], 1))

    # Labels
    labels = np.array(data_frame['class'])

    number_of_instances = len(features)

    print("-------------- ML ALGORITHMS PERFORMANCE FOR CONSTRUCTOR ISSUE --------------\n")
    evaluate_methods_performance(ml_methods=ml_methods,
                                 number_of_instances=number_of_instances,
                                 number_of_folds=number_of_folds,
                                 seed=seed,
                                 features=features,
                                 labels=labels,
                                 problem_title='constructor')

    # # ----------------------------- For trackware issue -----------------------------
    # data_frame = pd.read_csv(GENERATED_SAMPLES_FILE_FOR_TRACKWARE, sep=', ', engine='python')
    #
    # # Features
    # features = np.array(data_frame.drop(['class'], 1))
    #
    # # Labels
    # labels = np.array(data_frame['class'])
    #
    # number_of_instances = len(features)
    #
    # print("-------------- ML ALGORITHMS PERFORMANCE FOR TRACKWARE ISSUE --------------\n")
    # evaluate_methods_performance(ml_methods=ml_methods,
    #                              number_of_instances=number_of_instances,
    #                              number_of_folds=number_of_folds,
    #                              seed=seed,
    #                              features=features,
    #                              labels=labels,
    #                              problem_title='trackware')


def evaluate_methods_performance(ml_methods, number_of_instances,
                                 number_of_folds, seed, features, labels, problem_title):
    """
    Evaluates machine learning methods for cs problem - constructor
    :param ml_methods: machine learning methods
    :param number_of_instances: number of instances
    :param number_of_folds: number of folds
    :param seed: seed
    :param features: features
    :param labels: labels
    :param problem_title: title of the problem
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
                                    results=results,
                                    problem_title=problem_title)


def show_plot_of_algorithms_results(methods_names, results, problem_title):
    """
    Shows plot of machine learning algorithms results
    :param methods_names: Machine learning methods names
    :param results: Results got from applying methods for constructor
    :param problem_title: title of the problem
    """
    fig = plt.figure()

    # Add a subplot to the new figure, 111 means "1x1 grid, first subplot"
    ax = fig.add_subplot(111)
    plt.boxplot(results)

    # x axis title
    plt.xlabel('Machine learning algorithms')

    # y axis title
    plt.ylabel('Accuracy')

    plt.title('Machine learning algorithms applied for {}'.format(problem_title))
    # Name of each box
    ax.set_xticklabels(methods_names)

    # Change font size of the text
    plt.rcParams.update({'font.size': 23})

    # Show box plot
    plt.show()


if __name__ == "__main__":
    run_script()
