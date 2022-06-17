import math

from lib.statisticalTests.utils import calculate_streaks


def ji_square_statistic(intervals):
    """
    JI-Square test for uniformity of distribution.
    :param intervals: array of ints - has observed frecuencies of every interval
    :return: float - ji square statistic value
    """
    total_observations = 0
    for observedFrequency in intervals:
        total_observations += observedFrequency

    expected_frequency = total_observations / len(intervals)
    ji_square_value = 0
    for observedFrequency in intervals:
        ji_square_value = ji_square_value + ((observedFrequency - expected_frequency) ** 2) / expected_frequency

    return ji_square_value


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
    # Ordenar sucesion en orden ascendente
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


def poker_test():
    return 0


def serial_test():
    return 0
