import random as rnd
from lib.randomNumberGenerators.lgc_configuration import LgcConfiguration, LgcConfigurationFactory
from lib.randomNumberGenerators.utils import calculate_central_digits


def python_rand(num_iterations, seed=None):
    """
    Run the built-in python random number generator
    :param seed:  int - number of random numbers requested
    :param num_iterations:  int - number of random numbers requested
    :return: array - contains all random numbers generated
    """
    # Initialize seed
    if seed is None:
        seed = 1
    rnd.seed(seed)

    random_numbers = []
    counter = 0
    while counter < num_iterations:
        x_value = rnd.random()
        random_numbers.append(x_value)
        counter = counter + 1

    return random_numbers


def generate_lcg(num_iterations, lgc_configuration=None):
    """
    Linear Congruential Generator
    :param lgc_configuration: LgcConfiguration object - has the seed, mod, multiplier and increment
    :param num_iterations: int - number of random numbers requested
    :return: array - contains all random numbers generated
    """

    if lgc_configuration is None:
        lgc_configuration = LgcConfigurationFactory.get_lgc_configuration('randu')

    if not isinstance(lgc_configuration, LgcConfiguration):
        raise Exception("lgc_configuration should be an instance of LgcConfiguration")

    # Initialize variables
    x_value = lgc_configuration.seed
    a = lgc_configuration.multiplier
    c = lgc_configuration.increment
    m = lgc_configuration.mod

    counter = 0
    random_numbers = []
    while counter < num_iterations:
        x_value = ((a * x_value) + c) % m
        writeValue = x_value / m
        random_numbers.append(writeValue)
        counter = counter + 1

    return random_numbers


def middle_squares(num_iterations, seed, length):
    """
    Middle Squares generator
    :param length: int - length of the generated random numbers
    :param seed: int - seed of the generator
    :param num_iterations: int - number of random numbers requested
    :return: array - contains all random numbers generated
    """
    normalizer = pow(10, length)
    random_numbers = []
    counter = 0

    while counter < num_iterations:
        power_of_two = pow(seed, 2)
        central_part = calculate_central_digits(power_of_two, length)
        seed = central_part
        normalized_number = central_part / normalizer
        random_numbers.append(normalized_number)

    return random_numbers
