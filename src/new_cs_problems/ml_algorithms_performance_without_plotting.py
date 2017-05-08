# -*- coding: utf-8 -*-

import numpy as np
# np.set_printoptions(threshold=np.inf)  # To show full numpy array for debugging

import pandas as pd

from sklearn import cross_validation

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC  # svm - Support Vector Machines
from sklearn.ensemble import AdaBoostClassifier

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
    print("-------------- ML ALGORITHMS PERFORMANCE FOR CONSTRUCTOR ISSUE --------------\n")

    data_frame = pd.read_csv(GENERATED_SAMPLES_FILE_FOR_CONSTRUCTOR, sep=', ', engine='python')

    # Instances
    samples = np.array(data_frame.drop(['class'], 1))

    # Labels
    labels = np.array(data_frame['class'])

    number_of_instances = len(samples)

    evaluate_methods_performance(ml_methods=ml_methods,
                                 number_of_instances=number_of_instances,
                                 number_of_folds=number_of_folds,
                                 seed=seed,
                                 samples=samples,
                                 labels=labels)

    # # ----------------------------- For trackware issue -----------------------------
    print("-------------- ML ALGORITHMS PERFORMANCE FOR TRACKWARE ISSUE --------------\n")

    data_frame = pd.read_csv(GENERATED_SAMPLES_FILE_FOR_TRACKWARE, sep=', ', engine='python')

    # Instances
    samples = np.array(data_frame.drop(['class'], 1))

    # Labels
    labels = np.array(data_frame['class'])

    number_of_instances = len(samples)

    evaluate_methods_performance(ml_methods=ml_methods,
                                 number_of_instances=number_of_instances,
                                 number_of_folds=number_of_folds,
                                 seed=seed,
                                 samples=samples,
                                 labels=labels)


def evaluate_methods_performance(ml_methods, number_of_instances,
                                 number_of_folds, seed, samples, labels):
    """
    Evaluates machine learning methods for cs problem - constructor
    :param ml_methods: machine learning methods
    :param number_of_instances: number of instances
    :param number_of_folds: number of folds
    :param seed: seed
    :param samples: samples
    :param labels: labels
    """
    scoring = 'accuracy'

    for name, method in ml_methods:
        # noinspection PyDeprecation
        k_fold = cross_validation.KFold(n=number_of_instances,
                                        n_folds=number_of_folds,
                                        random_state=seed)
        # noinspection PyDeprecation
        cv_results = cross_validation.cross_val_score(method,
                                                      samples,
                                                      labels,
                                                      cv=k_fold,
                                                      scoring=scoring)

        print("\t\t%s" % name)

        # Mean accuracy and standard deviation accuracy
        accuracy_message = "Mean accuracy (standard deviation accuracy): " \
                           "%.3f (+/- %.3f)\n" % (
                               cv_results.mean() * 100, cv_results.std() * 100)
        print(accuracy_message)


if __name__ == "__main__":
    run_script()
