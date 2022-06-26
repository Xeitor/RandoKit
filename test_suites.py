from lib.randomNumberGenerators.generators import *
from lib.statisticalTests.statistical_tests import *


def test_suites():
    sizes_to_test = [500000, 1000000, 5000000]
    # generators = ['lcg_randu', 'lgc_pascal', 'middle_squares', 'python_rand']

    print('Generator: LGC_RANDU')
    for size in sizes_to_test:
        print(f'------------Size ({size})------------')
        start = time.time()
        random_numbers = generate_lcg(size, LgcConfigurationFactory.get_configuration('randu'))
        end = time.time()
        print(f'Time: {end - start}')

    print('Generator: LGC_PASCAL')
    for size in sizes_to_test:
        print(f'------------Size ({size})------------')
        start = time.time()
        random_numbers = generate_lcg(size, LgcConfigurationFactory.get_configuration('pascal'))
        end = time.time()
        print(f'Time: {end - start}')
        # run_kolmogorov(random_numbers)

    print('Generator: MIDDLE_SQUARES')
    for size in sizes_to_test:
        start = time.time()
        print(f'------------Size ({size})------------')
        random_numbers = middle_squares(size, seed=9223372036854775807, length=15)
        end = time.time()
        print(f'Time: {end - start}')
        # run_serial(random_numbers)

    print('Generator: PYTHON_RAND')
    for size in sizes_to_test:
        print(f'------------Size ({size})------------')
        start = time.time()
        random_numbers = python_rand(size, seed=1)
        end = time.time()
        print(end - start)
        # run_kolmogorov(random_numbers)
    return


def run_chi_square(random_numbers):
    significance_levels = [0.1, 0.05]
    for significance_level in significance_levels:
        print(f'------------Significance level ({significance_level})------------')
        results = chi_square_uniformity_test(random_numbers=random_numbers.copy(), significance_level=significance_level)
        process_results(results)
        print('Chi-Square: ' + str(results))
    print('-----------------------------------------------------')


def run_kolmogorov(random_numbers):
    print(f'------------Significance level ({0.1})------------')
    results = kolmogorov_smirnov_uniformity_test(random_numbers=random_numbers.copy(), significance_level=0.1)
    process_results(results)
    print('Kolmogorov: ' + str(results))
    print('-----------------------------------------------------')


def run_streaks(random_numbers):
    significance_level = 0.1
    print(f'------------Significance level {significance_level}------------')
    results = streaks_independence_test(random_numbers=random_numbers.copy(), significance_level=significance_level)
    print('Streaks: ' + str(results))
    process_results(results)
    print('-----------------------------------------------------')


def run_serial(random_numbers):
    significance_level = 0.1
    print(f'------------Significance level {significance_level}------------')
    results = serial_uniformity_test(random_numbers=random_numbers.copy(), significance_level=significance_level, dimensions=2, freedom_degrees=10)
    process_results(results)
    print('Rachas: ' + str(results))
    print('-----------------------------------------------------')


def process_results(results):
    statistic_value = results['statistic_value']
    table_critical_value = results['table_critical_value']
    if isinstance(table_critical_value, list):
        if table_critical_value[0] < statistic_value <= table_critical_value[1]:
            print(f"La hipotesis nula se acepta: {table_critical_value[0]} < {statistic_value} <= {table_critical_value[1]}")
        else:
            print(f"La hipotesis nula se rechaza, el estadístico calculado {statistic_value}, no se encuentra en el intervalo {table_critical_value[0]} < Z <= {table_critical_value[1]}")
    else:
        if statistic_value <= table_critical_value:
            print(f"La hipotesis nula se acepta: {statistic_value} <= {table_critical_value}")
        else:
            print(f"La hipotesis nula se rechaza, {statistic_value} > {table_critical_value}")

if __name__ == '__main__':
    test_suites()
