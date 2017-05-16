# -*- coding: utf-8 -*-
import unittest

from src import synthetic_data_generator

# Constants
MALICIOUS_DATA_SAMPLES = [[1, 0, 1, 0, 0, 0, 1, 0], [1, 1, 1, 0, 1, 0, 1, 0]]
NO_OF_FEATURES = 8
NEW_SAMPLE = [1, 0, 1, 1, 1, 0, 1, 1]

# Not correct constants
INVALID_MALICIOUS_DATA_SAMPLES = [[0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0]]
INVALID_NO_OF_FEATURES = 0
INVALID_NEW_SAMPLE = [0, 0, 0, 0, 0, 0, 0, 0]


class TestGetCategory(unittest.TestCase):
    """
    Tests for function - 'get_category'
    """

    def test_with_correct_arguments(self):
        """
        It should get correct category.
        """
        response = synthetic_data_generator.get_category(
            MALICIOUS_DATA_SAMPLES,
            NO_OF_FEATURES,
            NEW_SAMPLE)
        category = '1'
        self.assertEqual(category, response)

        # def test_without_correct_arguments(self):
        #     """
        #     It should get the exception.
        #     """
        #     synthetic_data_generator.get_category(
        #         INVALID_MALICIOUS_DATA_SAMPLES,
        #         INVALID_NO_OF_FEATURES,
        #         INVALID_NEW_SAMPLE)
