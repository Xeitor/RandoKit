import unittest

import numpy as np

from lib.randomNumberGenerators.lgc_configuration import LgcConfigurationFactory
from lib.randomNumberGenerators.generators import *
from lib.statisticalTests.statistical_tests import *


class TestsStatisticMethods(unittest.TestCase):

    def test_ji_square(self):
        intervals = [20, 18, 21, 20, 21]
        expected_value = 0.3
        self.assertEqual(chi_square_statistic(intervals), expected_value)

    def test_streaks(self):
        random_numbers = [0.00001, 0.13154, 0.75561, 0.45865, 0.53277, 0.21896, 0.04704, 0.67886, 0.6793, 0.93469,
                          0.3835, 0.51942, 0.83097, 0.03457, 0.05346, 0.5297, 0.67115, 0.0077, 0.38342, 0.06684,
                          0.41749, 0.68677, 0.58898, 0.93044, 0.84617, 0.52693, 0.09196, 0.65392, 0.416, 0.70119,
                          0.91032, 0.7622, 0.26245, 0.04746, 0.73608, 0.32823, 0.63264, 0.75641, 0.99104, 0.36534]
        expected_value = 0.2266
        self.assertAlmostEqual(streaks_statistic(random_numbers), expected_value, places=4)
        pass

    def test_kolmogorov_smirnov(self):
        random_numbers = [0.05, 0.46, 0.84, 0.41, 0.72, 0.24, 0.68, 0.62, 0.11, 0.92, 0.18, 0.21, 0.5, 0.61, 0.77, 0.76]
        expected_value = 0.105
        expected_critical_value = 0.2577
        self.assertAlmostEqual(expected_critical_value, ks_critical_value(16, 0.2), places=3)
        self.assertAlmostEqual(kolmogorov_smirnov_statistic(random_numbers), expected_value, places=3)

    def test_kolmogorov_smirnov_uniformity_test(self):
        random_numbers = [0.05, 0.46, 0.84, 0.41, 0.72, 0.24, 0.68, 0.62, 0.11, 0.92, 0.18, 0.21, 0.5, 0.61, 0.77, 0.76]
        results = kolmogorov_smirnov_uniformity_test(random_numbers, 0.2)
        expected_calculated_statistic = 0.105
        expected_calculated_critical_value = 0.2577
        self.assertAlmostEqual(results['statistic_value'], expected_calculated_statistic, places=3)
        self.assertAlmostEqual(results['table_critical_value'], expected_calculated_critical_value, places=3)

    def test_streaks_independence_test(self):
        random_numbers = [0.00001, 0.13154, 0.75561, 0.45865, 0.53277, 0.21896, 0.04704, 0.67886, 0.6793, 0.93469,
                          0.3835, 0.51942, 0.83097, 0.03457, 0.05346, 0.5297, 0.67115, 0.0077, 0.38342, 0.06684,
                          0.41749, 0.68677, 0.58898, 0.93044, 0.84617, 0.52693, 0.09196, 0.65392, 0.416, 0.70119,
                          0.91032, 0.7622, 0.26245, 0.04746, 0.73608, 0.32823, 0.63264, 0.75641, 0.99104, 0.36534]
        results = streaks_independence_test(random_numbers, 0.1)
        expected_calculated_statistic = 0.227
        expected_calculated_critical_value = 1.645
        self.assertAlmostEqual(results['statistic_value'], expected_calculated_statistic, places=3)
        self.assertAlmostEqual(results['table_critical_value'][0], expected_calculated_critical_value, places=3)

    def test_chi_square_uniformity_test(self):
        random_numbers = []
        results = chi_square_uniformity_test(random_numbers=random_numbers, significance_level=0.01,
                                             degrees_of_freedom=10)
        expected_calculated_statistic = 0.0
        expected_calculated_critical_value = 0.0
        self.assertAlmostEqual(results['statistic_value'], expected_calculated_statistic, places=3)
        self.assertAlmostEqual(results['table_critical_value'], expected_calculated_critical_value, places=3)

    def test_chi_square_critical_values(self):
        significance_level = 0.2
        degrees_of_freedom = 4
        expected_critical_value = 9.4877
        critical_value = chi_square_critical_value(99, 0.1)
        self.assertAlmostEqual(critical_value, expected_critical_value)
    def test_serial_independence_test(self):
        random_numbers = [0.05, 0.46, 0.84, 0.41, 0,0.72, 0.24, 0.68, 0.62, 0.11, 0.92, 0.18, 0.21, 0.5, 0.61, 0.77, 0.76]
        new_array = np.reshape(random_numbers, (-1, 3))
        histogram = np.histogramdd(new_array, bins=5)
        print(histogram[0])
        print(histogram[0].flatten(order='C'))

    def test_serial_independence_test_two(self):
        random_numbers = [0.872, 0.219, 0.570, 0.618, 0.291, 0.913, 0.950, 0.041, 0.842, 0.512, 0.151, 0.511, 0.343,
                          0.036, 0.706, 0.462, 0.596, 0.586, 0.058, 0.213, 0.809, 0.005, 0.443, 0.608, 0.384, 0.946,
                          0.300, 0.203, 0.868, 0.879]
        results = serial_uniformity_test(random_numbers, 0.05, 3, 3)
        print(results)
        expected_calculated_statistic = 5.999
        expected_calculated_critical_value = 15.507
        self.assertAlmostEqual(results['statistic_value'], expected_calculated_statistic, places=2)
        self.assertAlmostEqual(results['table_critical_value'], expected_calculated_critical_value, places=2)


if __name__ == '__main__':
    unittest.main()
