# -*- coding: utf-8 -*-
import os
dir_name = os.path.dirname
spam_file = os.path.join(dir_name(dir_name(__file__)), "datasets", "spam", "spambase.data.txt")
phishing_file = os.path.join(dir_name(dir_name(__file__)), "datasets", "phishing", "training.phishing.data.txt")
