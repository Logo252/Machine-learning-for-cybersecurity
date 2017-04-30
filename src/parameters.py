# -*- coding: utf-8 -*-

import os

dir_name = os.path.dirname

# Training data files for cybersecurity problems
TRAINING_DATA_FOR_SPAM = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'cs_problems', 'spam', 'training.spambase.data.txt')
TRAINING_DATA_FOR_PHISHING = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'cs_problems', 'phishing', 'training.phishing.data.txt')

# Parameters for new cybersecurity problems

# Trackware
TRAINING_DATA_FOR_TRACKWARE = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'trackware', 'training_trackware_data.txt')
GENERATED_SAMPLES_FILE_FOR_TRACKWARE = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'trackware', 'generated_samples.txt')
NO_OF_TRACKWARE_FEATURES = 7
LISTS_OF_TRACKWARE_SAMPLES = [[0, 1, 0, 0, 0, 1, 1, 1, 1],
                              [0, 0, 0, 0, 0, 0, 0, 1, 1],
                              [0, 0, 0, 0, 0, 1, 1, 1, 1],
                              [1, 0, 0, 0, 0, 1, 1, 1, 1],
                              [0, 0, 1, 1, 0, 1, 1, 1, 1],
                              [0, 0, 0, 0, 1, 1, 1, 1, 1]
                              ]
# Constructor
TRAINING_DATA_FOR_CONSTRUTOR = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'constructor', 'training_constructor_data.txt')
GENERATED_SAMPLES_FIILE_FOR_CONSTRUCTOR = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'constructor', 'generated_samples.txt')
NO_OF_CONSTRUCTOR_FEATURES = 8
LISTS_OF_CONSTRUCTOR_SAMPLES = [[0, 1, 0, 0, 0, 1, 1, 1, 1],
                                [0, 0, 0, 0, 0, 0, 0, 1, 1],
                                [0, 0, 0, 0, 0, 1, 1, 1, 1],
                                [1, 0, 0, 0, 0, 1, 1, 1, 1],
                                [0, 0, 1, 1, 0, 1, 1, 1, 1],
                                [0, 0, 0, 0, 1, 1, 1, 1, 1]
                                ]
