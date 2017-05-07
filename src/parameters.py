# -*- coding: utf-8 -*-

import os

dir_name = os.path.dirname

# Training data files for cybersecurity problems
TRAINING_DATA_FOR_SPAM = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'cs_problems', 'spam', 'training.spambase.data.txt')
TRAINING_DATA_FOR_PHISHING = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'cs_problems', 'phishing', 'training.phishing.data.txt')

# Parameters for new cybersecurity problems

# Constructor
CONSTRUCTOR_SAMPLES_FILE = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'constructor', 'constructor_samples.txt')
GENERATED_SAMPLES_FILE_FOR_CONSTRUCTOR = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'constructor', 'generated_samples.txt')
# CONSTRUCTOR_SAMPLES = [[0, 0, 0, 0, 0, 1, 1, 1],
#                        [0, 0, 0, 0, 0, 1, 1, 1],
#                        [0, 1, 0, 0, 0, 1, 1, 1],
#                        [0, 0, 1, 1, 0, 1, 1, 1],
#                        [1, 0, 0, 0, 0, 1, 1, 1],
#                        [0, 0, 0, 0, 0, 1, 1, 1],
#                        [0, 0, 0, 0, 0, 1, 1, 1],
#                        [0, 0, 0, 0, 0, 1, 1, 1],
#                        [0, 0, 0, 0, 0, 1, 1, 1],
#                        [1, 0, 0, 0, 0, 1, 1, 1],
#                        [0, 0, 0, 0, 0, 1, 1, 1],
#                        [1, 0, 0, 0, 0, 1, 1, 1],
#                        [0, 0, 1, 1, 0, 1, 1, 1],
#                        [0, 0, 0, 0, 0, 1, 1, 1],
#                        [0, 0, 0, 0, 1, 1, 1, 1],
#                        [0, 0, 0, 0, 0, 1, 1, 1],
#                        [0, 0, 0, 0, 0, 1, 1, 1],
#                        [0, 0, 0, 0, 0, 1, 1, 1],
#                        [0, 0, 0, 0, 0, 1, 1, 1],
#                        [0, 0, 0, 0, 0, 1, 1, 1]
#                        ]


# CONSTRUCTOR_FEATURES = ['having_dot_symbol',
#                         'having_Constructor_word',
#                         'having_Vbs_or_VBS_word',
#                         'having_Worm_or_Worms_word',
#                         'having_Vbswg_word',
#                         'file_type_executable',
#                         'file_extension_exe_or_doc',
#                         'affected_windows_os']


# Trackware
TRACKWARE_SAMPLES_FILE = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'trackware', 'trackware_samples.txt')
GENERATED_SAMPLES_FILE_FOR_TRACKWARE = os.path.join(dir_name(dir_name(__file__)), 'datasets', 'new_cs_problems', 'trackware', 'generated_samples.txt')
# TRACKWARE_SAMPLES = [[0, 1, 1, 0, 0, 0, 0, 1, 0],
#                      [0, 1, 1, 0, 0, 1, 0, 1, 0],
#                      [0, 1, 1, 0, 0, 1, 1, 1, 0],
#                      [0, 1, 1, 0, 0, 1, 1, 1, 0],
#                      [0, 1, 1, 0, 1, 1, 0, 1, 0],
#                      [0, 1, 1, 0, 0, 1, 1, 1, 0],
#                      [0, 1, 1, 0, 0, 1, 0, 1, 0],
#                      [0, 1, 1, 0, 1, 1, 1, 1, 0],
#                      [0, 1, 1, 0, 0, 1, 1, 1, 0],
#                      [0, 1, 1, 0, 0, 1, 0, 1, 1],
#                      [0, 1, 1, 0, 1, 1, 0, 1, 1],
#                      [0, 1, 1, 0, 0, 1, 0, 1, 0],
#                      [0, 1, 1, 0, 1, 1, 0, 1, 1],
#                      [0, 1, 1, 0, 0, 1, 1, 1, 1],
#                      [0, 1, 1, 0, 0, 1, 0, 1, 1],
#                      [0, 1, 1, 0, 0, 1, 0, 1, 0],
#                      [0, 1, 1, 0, 0, 1, 0, 1, 0],
#                      [0, 1, 1, 0, 0, 1, 0, 1, 0],
#                      [0, 1, 1, 0, 0, 1, 0, 1, 0],
#                      [0, 1, 1, 0, 0, 1, 0, 1, 1],
#                      [0, 1, 1, 0, 0, 1, 0, 1, 1],
#                      [0, 1, 1, 0, 0, 0, 0, 1, 0],
#                      [0, 1, 1, 0, 0, 1, 0, 1, 0],
#                      [0, 1, 1, 0, 0, 1, 1, 1, 0],
#                      [0, 1, 1, 0, 1, 1, 0, 1, 1],
#                      [0, 1, 1, 0, 0, 1, 0, 1, 0],
#                      [0, 1, 1, 0, 0, 0, 0, 1, 1]
#                      ]

# TRACKWARE_FEATURES = ['having_dot_symbol',
#                       'modified_register',
#                       'file_type_executable',
#                       'crowded_HDD',
#                       'created_new_folder',
#                       'created_new_files',
#                       'modified_toolbar',
#                       'affected_windows_os',
#                       'runs_when_windows_os_starts']