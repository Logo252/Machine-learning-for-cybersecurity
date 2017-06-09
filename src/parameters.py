# -*- coding: utf-8 -*-

import os

DIR_NAME = os.path.dirname

# ----------- SPAM -----------
TRAINING_DATA_FOR_SPAM = os.path.join(DIR_NAME(DIR_NAME(__file__)),
                                      'datasets',
                                      'cs_problems',
                                      'spam',
                                      'training.spambase.data.txt')

# ----------- PHISHING -----------
TRAINING_DATA_FOR_PHISHING = os.path.join(DIR_NAME(DIR_NAME(__file__)),
                                          'datasets',
                                          'cs_problems',
                                          'phishing',
                                          'training.phishing.data.txt')

# ----------- TRACKWARE -----------
TRACKWARE_SAMPLES_FILE = os.path.join(DIR_NAME(DIR_NAME(__file__)),
                                      'datasets',
                                      'cs_problems',
                                      'trackware',
                                      'trackware_samples.txt')
ALL_SAMPLES_FOR_TRACKWARE = os.path.join(DIR_NAME(DIR_NAME(__file__)),
                                         'datasets',
                                         'cs_problems',
                                         'trackware',
                                         'all_samples.txt')
GENERATED_SAMPLES_FILE_FOR_TRACKWARE = os.path.join(
    DIR_NAME(DIR_NAME(__file__)),
    'datasets',
    'cs_problems',
    'trackware',
    'generated_samples.txt')
