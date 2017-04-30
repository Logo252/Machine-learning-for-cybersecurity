# -*- coding: utf-8 -*-

import os

dir_name = os.path.dirname

# Training data for CS problems
SPAM_FILE = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'cs_problems', 'spam', 'training.spambase.data.txt')
PHISHING_FILE = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'cs_problems', 'phishing', 'training.phishing.data.txt')

# Training data for New CS problems

# Trackware
TRACKWARE_FILE = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'trackware', 'training_trackware_data.txt')
GENERATED_SAMPLES_FILE_FOR_TRACKWARE = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'trackware', 'generated_samples.txt')
NO_OF_TRACKWARE_FEATURES = 7

# Constructor
CONSTRUCTOR_FILE = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'constructor', 'training_constructor_data.txt')
GENERATED_SAMPLES_FIILE_FOR_CONSTRUCTOR = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'constructor', 'generated_samples.txt')
NO_OF_CONSTRUCTOR_FEATURES = 8
