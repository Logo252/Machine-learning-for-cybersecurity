# -*- coding: utf-8 -*-

import os

dir_name = os.path.dirname

# Training data for CS problems
spam_file = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'cs_problems', 'spam', 'training.spambase.data.txt')
phishing_file = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'cs_problems', 'phishing', 'training.phishing.data.txt')

# Training data fir New CS problems

# Trackware
trackware_file = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'trackware', 'training_trackware_data.txt')
generated_samples_for_trackware = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'trackware', 'generated_samples.txt')

# Constructor
constructor_file = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'constructor', 'training_constructor_data.txt')
generated_samples_for_cosntructor = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'constructor', 'generated_samples.txt')
