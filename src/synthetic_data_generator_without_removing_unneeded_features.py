# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

import random

from src.parameters import GENERATED_SAMPLES_FILE_FOR_CONSTRUCTOR
from src.parameters import CONSTRUCTOR_SAMPLES_FILE

from src.parameters import GENERATED_SAMPLES_FILE_FOR_TRACKWARE
from src.parameters import TRACKWARE_SAMPLES_FILE

# Constants
NO_OF_SAMPLES = 100  # Number of samples which will be generated for the problem (duplicate samples will be removed)

# Possible values of the feature
ZERO = 0
ONE = 1


def run_script():
    """
    Runs the script as the standalone program
    """
    print('----------------------- CONSTRUCTOR -----------------------')
    file_name = GENERATED_SAMPLES_FILE_FOR_CONSTRUCTOR
    data_samples_file = CONSTRUCTOR_SAMPLES_FILE

    data_frame = pd.read_csv(data_samples_file, sep=', ', engine='python')
    no_of_features = len(data_frame.columns)

    export_samples_and_generated_random_data(file_name, no_of_features, data_frame)
    print("Generated random data has been exported to\n'{}' for constructor\n".format(file_name))

    print('----------------------- TRACKWARE -----------------------')
    file_name = GENERATED_SAMPLES_FILE_FOR_TRACKWARE
    data_samples_file = TRACKWARE_SAMPLES_FILE

    data_frame = pd.read_csv(data_samples_file, sep=', ', engine='python')
    no_of_features = len(data_frame.columns)

    export_samples_and_generated_random_data(file_name, no_of_features, data_frame)
    print("Generated random data has been exported to\n'{}' for trackware\n".format(file_name))


def export_samples_and_generated_random_data(file_name, no_of_features, data_frame):
    """
    Exports generated random data to specified file.
    :param file_name: file name
    :param no_of_features: number of features
    :param data_frame: malicious data samples
    """
    with open(file_name, 'w') as txt_file:

        # Writing features to the file and to console
        features = list(data_frame)
        features_as_string = ', '.join(str(feature) for feature in features)
        txt_file.write(features_as_string)
        txt_file.write(', class')
        txt_file.write('\n')  # new line
        print("Features names:\n{}\n".format(features_as_string))

        # Samples from data frame as numpy array (without header)
        samples = np.array(data_frame.as_matrix())
        samples = samples.tolist()

        # Writing samples to the file
        for sample in samples:
            sample_as_string = ', '.join(str(feature) for feature in sample)
            txt_file.write(sample_as_string)
            txt_file.write(', 1')  # category - 1 (malware) at the end of the line
            txt_file.write('\n')  # new line

        # Writing random samples to the file
        i = 1
        new_samples = []
        while i <= NO_OF_SAMPLES:
            i += 1

            new_sample = []
            for _ in range(no_of_features):
                feature_value = random.randint(ZERO, ONE)
                new_sample.append(feature_value)

            # If the new sample has been already generated or he is the same as real sample
            # then skip everything and try to generate new sample
            if new_sample in new_samples or new_sample in samples:
                continue
            else:
                new_samples.append(new_sample)
                new_sample_as_string = ', '.join(str(feature) for feature in new_sample)
                txt_file.write(new_sample_as_string)

            category = None

            # Finding out in which category new sample belongs to (comparing with given malicious data samples)
            for data_sample in samples:
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

            txt_file.write(', {}'.format(category))  # new category - 0 or 1
            txt_file.write('\n')  # new line


if __name__ == "__main__":
    run_script()