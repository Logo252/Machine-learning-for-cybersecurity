# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from src.ml_algorithms_performance.basic_functions import LOGGER
from src.ml_algorithms_performance.basic_functions import \
    evaluate_methods_performance
from src.parameters import ALL_SAMPLES_FOR_TRACKWARE


def run_script():
    """
    Runs the script as the standalone program.
    """
    # Configuration for cross validation test harness
    number_of_folds = 10

    # Seed ensures we have the same sequence of random numbers
    seed = 7

    ml_methods = [('K-NN', KNeighborsClassifier()),
                  ('Decision tree', DecisionTreeClassifier()),
                  ('Naive Bayes', GaussianNB()),
                  ('Logistic regression', LogisticRegression()),
                  ('SVM', SVC()),
                  ('AdaBoost', AdaBoostClassifier()),
                  ('Random forest', RandomForestClassifier()),
                  # added `max_iter=750` to NN (Neural Networks)
                  # to suppress a warning
                  ('NN', MLPClassifier(max_iter=750))
                  ]

    LOGGER.info("-------------- ML ALGORITHMS PERFORMANCE --------------\n")
    LOGGER.info("-------------- FOR TRACKWARE --------------\n")
    data_frame = pd.read_csv(ALL_SAMPLES_FOR_TRACKWARE,
                             sep=', ',
                             engine='python')

    samples = np.array(data_frame.drop(['class'], 1))
    labels = np.array(data_frame['class'])
    number_of_instances = len(samples)
    problem_title = 'trackware'

    evaluate_methods_performance(ml_methods=ml_methods,
                                 number_of_instances=number_of_instances,
                                 number_of_folds=number_of_folds,
                                 seed=seed,
                                 samples=samples,
                                 labels=labels,
                                 problem_title=problem_title)


if __name__ == "__main__":
    run_script()
