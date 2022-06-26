import math
import numpy as np
import time
from lib.statisticalTests.utils import *


def chi_square_statistic(intervals):
    """
    JI-Square test for uniformity of distribution.
    :param intervals: array of ints - has observed frequencies of every interval
    :return: float - ji square statistic value
    """
    total_observations = 0
    for observedFrequency in intervals:
        total_observations += observedFrequency

    expected_frequency = total_observations / len(intervals)
    chi_square_value = 0
    for observedFrequency in intervals:
        chi_square_value = chi_square_value + ((observedFrequency - expected_frequency) ** 2) / expected_frequency

    return chi_square_value


def streaks_statistic(random_numbers):
    standardMean = 0.5
    streaks = []
    aboveMean = 0
    belowMean = 0
    for elem in random_numbers:
        if elem > standardMean:
            aboveMean += 1
            streaks.append(1)
        else:
            belowMean += 1
            streaks.append(0)
    streak = calculate_streaks(streaks)
    size = aboveMean + belowMean
    n1_by_n2 = aboveMean * belowMean

    successionMean = ((2 * n1_by_n2) / size) + standardMean
    successionVariance = (((2 * n1_by_n2) * (2 * n1_by_n2 - size)) / ((size * size) * (size - 1)))

    statistic = (streak - successionMean) / math.sqrt(successionVariance)

    return statistic


def kolmogorov_smirnov_statistic(random_numbers):
    random_numbers.sort()
    successionSize = len(random_numbers)
    maximumDifference = 0

    index = 1
    for elem in random_numbers:
        indexOverSize = index / successionSize
        difference = abs(indexOverSize - elem)
        index += 1
        if difference > maximumDifference:
            maximumDifference = difference

    return maximumDifference


def chi_square_uniformity_test(random_numbers, degrees_of_freedom=10, significance_level=0.05):
    """
    :param random_numbers: array containing the random numbers to test.
    :param significance_level: significance level for the test.
    :param degrees_of_freedom: intervals to divide the interval numbers into
    :return: hash with both the table critical value and the result of the test.
    """
    # print('H0: Los números están distribuidos de forma uniforme')
    # print('H1: Los números no están distribuidos de forma uniforme')
    histogram = np.histogram(random_numbers, bins=degrees_of_freedom)[0]
    chi_square_critical_value_ = chi_square_critical_value(degrees_of_freedom - 1, significance_level)
    chi_square_statistic_ = chi_square_statistic(histogram)

    return {'table_critical_value': chi_square_critical_value_.round(5), 'statistic_value': chi_square_statistic_.round(5)}


def kolmogorov_smirnov_uniformity_test(random_numbers, significance_level=0.05):
    """
    :param random_numbers: array containing the random numbers to test.
    :param significance_level: significance level for the test.
    :return: hash with both the table critical value and the result of the test.
    """
    print('H0: Los números están distribuidos de forma uniforme')
    print('H1: Los números no están distribuidos de forma uniforme')
    kolmogorov_smirnov_statistic_value = kolmogorov_smirnov_statistic(random_numbers)
    kolmogorov_smirnov_critical_value = ks_critical_value(len(random_numbers), significance_level)

    return {'table_critical_value': kolmogorov_smirnov_critical_value,
            'statistic_value': kolmogorov_smirnov_statistic_value}


def streaks_independence_test(random_numbers, significance_level=0.05):
    """
    :param random_numbers: array containing the random numbers to test.
    :param significance_level: significance level for the test.
    :return: hash with both the table critical value and the result of the test.
    """

    streaks_statistic_value = streaks_statistic(random_numbers)
    normal_distribution_critical_value_ = normal_distribution_critical_value(significance_level)

    print('H0: Los números son independientes')
    print('H1: Los números no son independientes')

    return {'table_critical_value': [normal_distribution_critical_value_ * -1, normal_distribution_critical_value_],
            'statistic_value': streaks_statistic_value}


def serial_uniformity_test(random_numbers, significance_level, dimensions, freedom_degrees):
    k = math.pow(freedom_degrees, dimensions)
    arr = np.array(random_numbers)
    dimensioned_array = np.reshape(random_numbers, (-1, dimensions))
    histogram = np.histogramdd(dimensioned_array, bins=(freedom_degrees, freedom_degrees))[0].flatten(order='C')
    chi_square_critical_value_ = chi_square_critical_value(k - 1, significance_level)
    chi_square_statistic_ = chi_square_statistic(histogram)

    print(f'H0: Los números están distribuidos uniformemente en {dimensions} dimensiones')
    print(f'H0: Los números no están distribuidos uniformemente en {dimensions} dimensiones')

    return {'table_critical_value': chi_square_critical_value_, 'statistic_value': chi_square_statistic_}