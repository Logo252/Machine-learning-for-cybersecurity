# -*- coding: utf-8 -*-

import os

dir_name = os.path.dirname

# CS problems training data
spam_file = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'cs_problems', 'spam', 'training.spambase.data.txt')
phishing_file = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'cs_problems', 'phishing', 'training.phishing.data.txt')

# New CS problems
trackware_file = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'trackware', 'training.trackware.data.txt')
constructor_file = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'constructor', 'training.constructor.data.txt')

# print(spam_file)
# print(phishing_file)
# print(trackware_file)
# print(constructor_file)
