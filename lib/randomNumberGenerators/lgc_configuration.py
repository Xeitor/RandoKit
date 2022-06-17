class LgcConfiguration:
    def __init__(self, seed, mod, multiplier, increment):
        self.seed = seed
        self.mod = mod
        self.multiplier = multiplier
        self.increment = increment

    @property
    def seed(self):
        return self.seed

    @seed.setter
    def seed(self, seed):
        if not seed:
            raise Exception("description cannot be empty")
        self._seed = seed

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        if not (v > 0): raise Exception("value must be greater than zero")
        self._value = v


class LgcConfigurationFactory:
    CONFIGURATIONS = {
        'randu': {
            'seed': 1,
            'mod': (2 ** 31),
            'multiplier': 65539,
            'increment': 0
        }
    }

    @classmethod
    def get_configuration(cls, name):
        seed = cls.CONFIGURATIONS[name]["seed"]
        mod = cls.CONFIGURATIONS[name]["mod"]
        multiplier = cls.CONFIGURATIONS[name]["multiplier"]
        increment = cls.CONFIGURATIONS[name]["increment"]
        return LgcConfiguration(seed, mod, multiplier, increment)
