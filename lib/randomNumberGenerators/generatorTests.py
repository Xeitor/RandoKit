import unittest

from lib.randomNumberGenerators.lgc_configuration import LgcConfigurationFactory
from lib.randomNumberGenerators.linearCongruentialGenerator import *


class TestGenerators(unittest.TestCase):

    def test_lgc_generator(self):
        # Testing for randu configurations
        lgc_configuration = LgcConfiguration(seed=4, mod=8, multiplier=5, increment=7)
        values = generate_lcg(7, lgc_configuration)
        expected_values = [0.375, 0.75, 0.625, 0.0, 0.875, 0.25, 0.125]
        self.assertEqual(values, expected_values)

    def test_invalid_lgc_configuration(self):
        pass

    def test_middle_square_generator(self):
        pass

    def test_python_rand(self):
        pass


if __name__ == '__main__':
    unittest.main()
