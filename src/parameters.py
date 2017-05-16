# -*- coding: utf-8 -*-

import os

dir_name = os.path.dirname

# Training data files for cybersecurity problems
TRAINING_DATA_FOR_SPAM = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'cs_problems', 'spam', 'training.spambase.data.txt')
TRAINING_DATA_FOR_PHISHING = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'cs_problems', 'phishing', 'training.phishing.data.txt')

# Parameters for new cybersecurity problems

# Constructor
CONSTRUCTOR_SAMPLES_FILE = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'constructor', 'constructor_samples.txt')
ALL_SAMPLES_FOR_CONSTRUCTOR = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'constructor', 'all_samples.txt')

GENERATED_SAMPLES_FILE_FOR_CONSTRUCTOR = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'constructor', 'generated_samples.txt')

# Trackware
TRACKWARE_SAMPLES_FILE = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'trackware', 'trackware_samples.txt')
ALL_SAMPLES_FOR_TRACKWARE = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'trackware', 'all_samples.txt')

GENERATED_SAMPLES_FILE_FOR_TRACKWARE = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'trackware', 'generated_samples.txt')
