# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from src.ml_algorithms_performance.basic_functions import LOGGER
from src.ml_algorithms_performance.basic_functions import \
    evaluate_methods_performance
from src.parameters import TRAINING_DATA_FOR_PHISHING


def run_script():
    """
    Runs the script as the standalone program.
    """
    # Configuration for cross validation test harness
    number_of_folds = 10

    # Seed ensures we have the same sequence of random numbers
    seed = 7

    # ML methods - Decision Tree, Naive Bayes, Support Vector Machines,
    # Deep neural network, Random Forest
    ml_methods = [('Decision tree', DecisionTreeClassifier()),
                  ('Naive Bayes', GaussianNB()),
                  # SVM - Support vector machines
                  ('SVM', SVC()),
                  # DNN - Deep neural network with 5 hidden layers,
                  # each of the layers has 5 neurons
                  ('DNN', MLPClassifier(hidden_layer_sizes=(5, 5, 5, 5, 5))),
                  ('Random forest', RandomForestClassifier()),
                  ]

    LOGGER.info("-------------- ML ALGORITHMS PERFORMANCE --------------\n")
    LOGGER.info("-------------- FOR PHISHING --------------\n")
    data_frame = pd.read_csv(TRAINING_DATA_FOR_PHISHING,
                             sep=',',
                             engine='python')

    samples = np.array(data_frame.drop(['class'], 1))
    labels = np.array(data_frame['class'])
    number_of_instances = len(samples)
    problem_title = 'phishing'

    evaluate_methods_performance(ml_methods=ml_methods,
                                 number_of_instances=number_of_instances,
                                 number_of_folds=number_of_folds,
                                 seed=seed,
                                 samples=samples,
                                 labels=labels,
                                 problem_title=problem_title)

    LOGGER.info("-------------- ML ALGORITHMS PERFORMANCE --------------\n")
    LOGGER.info("-------------- FOR SPAM --------------\n")
    data_frame = pd.read_csv(TRAINING_DATA_FOR_PHISHING,
                             sep=',',
                             engine='python')

    samples = np.array(data_frame.drop(['class'], 1))
    labels = np.array(data_frame['class'])
    number_of_instances = len(samples)
    problem_title = 'spam'

    evaluate_methods_performance(ml_methods=ml_methods,
                                 number_of_instances=number_of_instances,
                                 number_of_folds=number_of_folds,
                                 seed=seed,
                                 samples=samples,
                                 labels=labels,
                                 problem_title=problem_title)


if __name__ == "__main__":
    run_script()
