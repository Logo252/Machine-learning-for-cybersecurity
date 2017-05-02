# -*- coding: utf-8 -*-

import numpy as np
import random

# Importing VarianceThreshold (Feature selector) from sklearn
from sklearn.feature_selection import VarianceThreshold

from src.parameters import GENERATED_SAMPLES_FILE_FOR_CONSTRUCTOR
from src.parameters import LISTS_OF_CONSTRUCTOR_SAMPLES

from src.parameters import GENERATED_SAMPLES_FILE_FOR_TRACKWARE
from src.parameters import LISTS_OF_TRACKWARE_SAMPLES

# Constants
NO_OF_SAMPLES = 500  # Number of generated samples for each problem

# Possible values of the feature
ZERO = 0
ONE = 1


def run_script():
    """
    Runs the script as the standalone program
    """

    # ----------------------- For constructor -----------------------
    file_name = GENERATED_SAMPLES_FILE_FOR_CONSTRUCTOR
    data_samples = LISTS_OF_CONSTRUCTOR_SAMPLES

    updated_data_samples = remove_unneeded_features(data_samples)
    modified_samples = add_category_to_samples(1, updated_data_samples)
    no_of_features = len(modified_samples) - 1

    # print(updated_data_samples)
    # print(modified_samples)
    # exit(0)

    export_random_data(file_name, no_of_features, modified_samples)
    print("Generated random data has been exported to '{}' for constructor\n".format(file_name))

    remove_duplicate_lines_in_file(file_name)
    # sort_file_lines_by_category(file_name, no_of_features)  # from 0 to 1

    # ----------------------- For trackware -----------------------
    file_name = GENERATED_SAMPLES_FILE_FOR_TRACKWARE
    data_samples = LISTS_OF_TRACKWARE_SAMPLES

    updated_data_samples = remove_unneeded_features(data_samples)
    modified_samples = add_category_to_samples(1, updated_data_samples)
    no_of_features = len(modified_samples) - 1

    # print(updated_data_samples)
    # print(modified_samples)
    # exit(0)

    export_random_data(file_name, no_of_features, data_samples)
    print("Generated random data has been exported to '{}' for trackware\n".format(file_name))

    remove_duplicate_lines_in_file(file_name)
    # sort_file_lines_by_category(file_name, no_of_features)  # from 0 to 1


def remove_unneeded_features(data_samples):
    """
    Removes features that have the same value in given data samples.
    :param data_samples: given data samples
    :return: updated data samples
    """
    sel = VarianceThreshold()
    return sel.fit_transform(data_samples)


def add_category_to_samples(category, samples):
    """
    Adds category to all given data samples.
    :param category: Given category - 1 or 0
    :param samples: data samples
    :return: data samples with category
    """
    modified_samples = []
    for sample in samples:
        updated_sample = list(np.append(sample, [category]))
        modified_samples.append(updated_sample)
    return modified_samples


def export_random_data(file_name, no_of_features, data_samples):
    """
    Exports generated random data to specified file.
    :param file_name: file name
    :param no_of_features: number of features
    :param data_samples: malicious data samples
    """
    add_header_to_file(file_name, no_of_features)

    with open(file_name, "a") as txt_file:
        i = 1
        while i <= NO_OF_SAMPLES:
            i += 1

            new_sample = []
            for _ in range(no_of_features):
                feature_value = random.randint(ZERO, ONE)
                new_sample.append(feature_value)

                txt_file.write('{}, '.format(feature_value))

            category = None
            # new_sample = [1, 1, 0, 0, 0, 1, 1, 0]  # For debugging

            # Finding out in which category new sample belongs to (comparing with given malicious data samples)
            for data_sample in data_samples:
                for index in range(len(new_sample)):
                    if data_sample[index] == 1:
                        # If malicious sample's feature value (1) matches to new sample's feature value
                        # then set sample as malicious, otherwise as benign and break cycle
                        if data_sample[index] == new_sample[index]:
                            category = '1'
                        else:
                            category = '0'
                            break
                if category == '1':  # If new sample's category is 1 then do not compare further to others data samples
                    break

            txt_file.write(category)  # new category - 0 or 1
            txt_file.write('\n')  # new line


def add_header_to_file(file, no_of_features):
    """
    Adds header to the given file.
    :param file: file name
    :param no_of_features: number of features
    """
    with open(file, "w") as txt_file:
        for number in range(1, no_of_features + 1):
            txt_file.write('feature_{}, '.format(number))
        txt_file.write('class')
        txt_file.write('\n')


def remove_duplicate_lines_in_file(file_name):
    """
    Removes duplicate lines in the specified file.
    :param file_name: 
    """
    with open(file_name, 'r') as read:
        lines = read.readlines()
        header = lines[0]
        lines_set = set(lines[1:])

    with open(file_name, 'w') as out:
        out.write(header)
        for line in lines_set:
            out.write(line)


def sort_file_lines_by_category(file_name, no_of_features):
    """
    Removes duplicate lines in the specified file.
    :param file_name: file name
    :param no_of_features: number of features
    """
    with open(file_name, 'r') as read:
        lines = read.readlines()
        sorted_lines = sorted(lines, key=lambda x: x.split()[no_of_features])

    with open(file_name, 'w') as out:
        for line in sorted_lines:
            out.write(line)


if __name__ == "__main__":
    run_script()
