# -*- coding: utf-8 -*-
import logging

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from src.parameters import TRAINING_DATA_FOR_PHISHING

# Logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)  # logging.DEBUG, logging.WARNING


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


def evaluate_methods_performance(ml_methods, number_of_instances,
                                 number_of_folds, seed, samples, labels,
                                 problem_title):
    """
    Evaluates machine learning methods for given computer security issue.
    :param ml_methods: machine learning methods
    :param number_of_instances: number of instances
    :param number_of_folds: number of folds
    :param seed: seed
    :param samples: samples
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
                                                      samples,
                                                      labels,
                                                      cv=k_fold,
                                                      scoring=scoring)

        results.append(cv_results)
        methods_names.append(name)

        LOGGER.info("\t\t%s" % name)

        accuracy_message = "Mean accuracy (standard deviation): " \
                           "%.3f%% (+/- %.3f%%)\n" % (
                               cv_results.mean() * 100, cv_results.std() * 100)
        LOGGER.info(accuracy_message)

    show_plot_of_algorithms_results(methods_names=methods_names,
                                    results=results,
                                    problem_title=problem_title)


def show_plot_of_algorithms_results(methods_names, results, problem_title):
    """
    Shows plot of machine learning algorithms results.
    :param methods_names: machine learning methods names
    :param results: results got from applying methods for constructor
    :param problem_title: title of the problem
    """
    fig = plt.figure()

    ax = fig.add_subplot(111)  # 111 means "1x1 grid, first subplot"
    plt.boxplot(results)

    # x and y axis titles
    plt.xlabel('Machine learning algorithms')
    plt.ylabel('Accuracy')

    plt.title(
        'Machine learning algorithms applied for {}'.format(problem_title))

    # Set the Name of each box
    ax.set_xticklabels(methods_names)

    # Change font size of the text
    plt.rcParams.update({'font.size': 23})

    plt.show()


if __name__ == "__main__":
    run_script()
