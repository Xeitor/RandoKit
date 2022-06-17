import unittest

from lib.randomNumberGenerators.lgc_configuration import LgcConfigurationFactory
from lib.randomNumberGenerators.generators import *
from lib.statisticalTests.statistical_tests import ji_square_statistic, streaks_statistic, kolmogorov_smirnov_statistic


class TestsStatisticMethods(unittest.TestCase):

    def test_ji_square(self):
        intervals = [20, 18, 21, 20, 21]
        expected_value = 0.3
        self.assertEqual(ji_square_statistic(intervals), expected_value)

    def test_streaks(self):
        random_numbers = [0.00001, 0.13154, 0.75561, 0.45865, 0.53277, 0.21896, 0.04704, 0.67886, 0.6793, 0.93469, 0.3835, 0.51942, 0.83097, 0.03457, 0.05346, 0.5297, 0.67115, 0.0077, 0.38342, 0.06684, 0.41749, 0.68677, 0.58898, 0.93044, 0.84617, 0.52693, 0.09196, 0.65392, 0.416, 0.70119, 0.91032, 0.7622, 0.26245, 0.04746, 0.73608, 0.32823, 0.63264, 0.75641, 0.99104, 0.36534]
        expected_value = 0.2266
        self.assertAlmostEqual(streaks_statistic(random_numbers), expected_value, places=4)
        pass

    def test_kolmogorov_smirnov(self):
        random_numbers = [0.05, 0.46, 0.84, 0.41, 0.72, 0.24, 0.68, 0.62, 0.11, 0.92, 0.18, 0.21, 0.5, 0.61, 0.77, 0.76]
        expected_value = 0.105
        self.assertAlmostEqual(kolmogorov_smirnov_statistic(random_numbers), expected_value, places=3)


if __name__ == '__main__':
    unittest.main()
