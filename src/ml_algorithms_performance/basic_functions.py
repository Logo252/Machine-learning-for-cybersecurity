# -*- coding: utf-8 -*-
import logging

import matplotlib.pyplot as plt
from sklearn import cross_validation

# Logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s')
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)  # logging.DEBUG, logging.WARNING


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

        LOGGER.info("\t\t%s", name)

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

    axes = fig.add_subplot(111)  # 111 means "1x1 grid, first subplot"
    plt.boxplot(results)

    # x and y axis titles
    plt.xlabel('Machine learning algorithms')
    plt.ylabel('Accuracy')

    plt.title(
        'Machine learning algorithms applied for {}'.format(problem_title))

    # Set the Name of each box
    axes.set_xticklabels(methods_names)

    # Change font size of the text
    plt.rcParams.update({'font.size': 23})

    plt.show()
