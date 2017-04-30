# -*- coding: utf-8 -*-

import random

from src.parameters import GENERATED_SAMPLES_FIILE_FOR_CONSTRUCTOR
from src.parameters import NO_OF_CONSTRUCTOR_FEATURES

from src.parameters import GENERATED_SAMPLES_FILE_FOR_TRACKWARE
from src.parameters import NO_OF_TRACKWARE_FEATURES

# Constants
# LABEL = '0'
SAMPLES = 50

MINIMUM = 0
MAXIMUM = 1


def run_script():
    """
    Runs the script as the standalone program
    """
    file_name = GENERATED_SAMPLES_FIILE_FOR_CONSTRUCTOR
    no_of_features = NO_OF_CONSTRUCTOR_FEATURES

    export_random_data(SAMPLES, MINIMUM, MAXIMUM, file_name, no_of_features)
    print("Generated data has been exported to {}".format(file_name))

    file_name = GENERATED_SAMPLES_FILE_FOR_TRACKWARE
    no_of_features = NO_OF_TRACKWARE_FEATURES

    export_random_data(SAMPLES, MINIMUM, MAXIMUM, file_name, no_of_features)
    print("Generated data has been exported to {}".format(file_name))


def export_random_data(samples, minimum, maximum, file_name, no_of_features):
    """
    Exports generated random data to specified file.
    :param samples: samples
    :param minimum: minimum value of the feature
    :param maximum: maximum value of the feature
    :param file_name: file name
    :param no_of_features: number of features
    """
    i = 1
    with open(file_name, "w") as txt_file:
        while i <= samples:
            for _ in range(no_of_features):
                txt_file.write(
                    "{}, ".format(random.randint(minimum, maximum)))
            txt_file.write('\n')
            i += 1


if __name__ == "__main__":
    run_script()
