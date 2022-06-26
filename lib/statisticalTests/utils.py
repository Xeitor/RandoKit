from scipy.stats import chi2
from scipy.stats import ksone
from scipy.stats import norm


def ks_critical_value(n_trials, alpha):
    return ksone.ppf(1 - alpha / 2, n_trials)


def chi_square_critical_value(degrees_of_freedom, significance_level):
    print(degrees_of_freedom)
    print(significance_level)
    return chi2.isf(df=degrees_of_freedom, q=significance_level)


def normal_distribution_critical_value(significance_level):
    return norm.ppf(1 - significance_level / 2)


def calculate_streaks(rachas):
    streaks = 0
    previous = rachas[0]

    for index in range(1, len(rachas) - 1):
        if rachas[index] != previous:
            streaks += 1
            previous = rachas[index]

    if rachas[-1] == previous:
        streaks += 1
    else:
        streaks += 2

    return streaks
