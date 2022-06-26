class LgcConfiguration:
    def __init__(self, seed, mod, multiplier, increment):
        self.seed = seed
        self.mod = mod
        self.multiplier = multiplier
        self.increment = increment


class LgcConfigurationFactory:
    CONFIGURATIONS = {
        'randu': {
            'seed': 1,
            'mod': (2 ** 31),
            'multiplier': 65539,
            'increment': 0
        },
        'pascal': {
            'seed': 1,
            'mod': (2 ** 32),
            'multiplier': 134775813,
            'increment': 1

        }
    }

    @classmethod
    def get_configuration(cls, name):
        seed = cls.CONFIGURATIONS[name]["seed"]
        mod = cls.CONFIGURATIONS[name]["mod"]
        multiplier = cls.CONFIGURATIONS[name]["multiplier"]
        increment = cls.CONFIGURATIONS[name]["increment"]
        return LgcConfiguration(seed, mod, multiplier, increment)
