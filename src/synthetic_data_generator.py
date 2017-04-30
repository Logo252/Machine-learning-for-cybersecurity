# -*- coding: utf-8 -*-

import random

from src.parameters import GENERATED_SAMPLES_FIILE_FOR_CONSTRUCTOR
from src.parameters import NO_OF_CONSTRUCTOR_FEATURES

from src.parameters import GENERATED_SAMPLES_FILE_FOR_TRACKWARE
from src.parameters import NO_OF_TRACKWARE_FEATURES

# Constants
SAMPLES = 50

# Possible value of the feature
MINIMUM = 0
MAXIMUM = 1


def run_script():
    """
    Runs the script as the standalone program
    """
    export_random_data(SAMPLES, MINIMUM, MAXIMUM, GENERATED_SAMPLES_FIILE_FOR_CONSTRUCTOR, NO_OF_CONSTRUCTOR_FEATURES)
    print("Generated data has been exported to '{}' for constructor".format(GENERATED_SAMPLES_FIILE_FOR_CONSTRUCTOR))


    export_random_data(SAMPLES, MINIMUM, MAXIMUM, GENERATED_SAMPLES_FILE_FOR_TRACKWARE, NO_OF_TRACKWARE_FEATURES)
    print("Generated data has been exported to '{}' for trackware".format(GENERATED_SAMPLES_FILE_FOR_TRACKWARE))


def export_random_data(samples, minimum, maximum, file_name, no_of_features):
    """
    Exports generated random data to specified file.
    :param samples: samples
    :param minimum: minimum value of the feature
    :param maximum: maximum value of the feature
    :param file_name: file name
    :param no_of_features: number of features
    """
    with open(file_name, "w") as txt_file:
        i = 1
        while i <= samples:
            for _ in range(no_of_features):
                txt_file.write(
                    "{}, ".format(random.randint(minimum, maximum)))
            txt_file.write('\n')
            i += 1


if __name__ == "__main__":
    run_script()
