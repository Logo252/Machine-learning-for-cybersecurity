# -*- coding: utf-8 -*-

import random

from src.parameters import GENERATED_SAMPLES_FIILE_FOR_CONSTRUCTOR
from src.parameters import NO_OF_CONSTRUCTOR_FEATURES
from src.parameters import LISTS_OF_CONSTRUCTOR_SAMPLES

from src.parameters import GENERATED_SAMPLES_FILE_FOR_TRACKWARE
from src.parameters import NO_OF_TRACKWARE_FEATURES
from src.parameters import LISTS_OF_TRACKWARE_SAMPLES

# Constants
NO_OF_SAMPLES = 100  # Number of generated samples for each problem

# Possible values of the feature
ZERO = 0
ONE = 1


def run_script():
    """
    Runs the script as the standalone program
    """

    # ----------------------- For constructor -----------------------
    file_name = GENERATED_SAMPLES_FIILE_FOR_CONSTRUCTOR
    no_of_features = NO_OF_CONSTRUCTOR_FEATURES
    data_samples = LISTS_OF_CONSTRUCTOR_SAMPLES

    export_random_data(file_name, no_of_features, data_samples)
    print("Generated random data has been exported to '{}' for constructor\n".format(file_name))

    remove_duplicate_lines_in_file(file_name)
    sort_file_lines_by_category(file_name, no_of_features)

    # ----------------------- For trackware -----------------------
    file_name = GENERATED_SAMPLES_FILE_FOR_TRACKWARE
    no_of_features = NO_OF_TRACKWARE_FEATURES
    data_samples = LISTS_OF_TRACKWARE_SAMPLES

    export_random_data(file_name, no_of_features, data_samples)
    print("Generated random data has been exported to '{}' for trackware\n".format(file_name))

    remove_duplicate_lines_in_file(file_name)
    sort_file_lines_by_category(file_name, no_of_features)


def export_random_data(file_name, no_of_features, data_samples):
    """
    Exports generated random data to specified file.
    :param file_name: file name
    :param no_of_features: number of features
    :param data_samples: malicious data samples
    """
    with open(file_name, "w") as txt_file:
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


def remove_duplicate_lines_in_file(file_name):
    """
    Removes duplicate lines in the specified file.
    :param file_name: 
    """
    with open(file_name, 'r') as read:
        lines = read.readlines()
        lines_set = set(lines)

    with open(file_name, 'w') as out:
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