# -*- coding: utf-8 -*-

import random

# Constants
LABEL = '0'
SAMPLES = 50
FEATURES = 8

MINIMUM = 0
MAXIMUM = 1
FILE_NAME = 'samples.txt'


def run_script():
    """
    Runs the script as the standalone program
    """
    export_random_data(SAMPLES, MINIMUM, MAXIMUM, FILE_NAME)

    print("Data has been exported to {}".format(FILE_NAME))


def export_random_data(samples, minimum, maximum, file_name):
    """
    Exports generated random data to specified file.
    :param samples: samples
    :param minimum: minimum value of the feature
    :param maximum: maximum value of the feature
    :param file_name: file name
    """
    i = 1
    with open(file_name, "w") as txt_file:
        while i <= samples:
            txt_file.write(
                "{}, {}\n".format(random.randint(minimum, maximum), LABEL))
            i += 1


if __name__ == "__main__":
    run_script()
