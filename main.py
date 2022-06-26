from __future__ import print_function, unicode_literals
from PyInquirer import prompt

from lib.randomNumberGenerators.generators import generate_lcg, middle_squares, python_rand
from lib.randomNumberGenerators.lgc_configuration import LgcConfiguration
from lib.statisticalTests.statistical_tests import chi_square_uniformity_test, kolmogorov_smirnov_uniformity_test, \
    streaks_independence_test, serial_uniformity_test
from lib.utilities.utils import write_array_to_file, read_file_to_array


def main():
    questions = [
        {
            'type': 'list',
            'name': 'command',
            'message': 'Elegir comando a utilizar',
            'choices': [
                {
                    'name': 'Generar números aleatorios',
                    'value': 0
                },
                {
                    'name': 'Validar números generados',
                    'value': 1
                }]
        }
    ]

    answers = prompt(questions)
    if answers['command'] == 0:
        generate_random_numbers()
    elif answers['command'] == 1:
        validate_random_numbers()


def generate_random_numbers():
    questions = [
        {
            'type': 'list',
            'name': 'generator',
            'message': 'Elegir generador a utilizar',
            'choices': [
                {
                    'name': 'Congruencial lineal',
                    'value': 'lcg'
                },
                {
                    'name': 'Cuadrados medios',
                    'value': 'middle_squares'
                },
                {
                    'name': 'Mersenne Twister (Python rand)',
                    'value': 'python_rand'
                }
            ]
        },
        {
            'type': 'input',
            'name': 'file_name',
            'message': 'Path del archivo para guardar los números generados',
        },
        {
            'type': 'input',
            'name': 'num_iterations',
            'message': 'Cantidad de números aleatorios a generar',
        }

    ]
    answers = prompt(questions)
    configuration = {'num_iterations': int(answers['num_iterations']), 'file_name': answers['file_name']}
    if answers['generator'] == 'lcg':
        questions = [
            {
                'type': 'input',
                'name': 'mod',
                'message': 'Ingrese módulo',
            },
            {
                'type': 'input',
                'name': 'seed',
                'message': 'Ingrese semilla',
            },
            {
                'type': 'input',
                'name': 'multiplier',
                'message': 'Ingrese multiplicador',
            },
            {
                'type': 'input',
                'name': 'increment',
                'message': 'Ingrese incremento',
            },
        ]
        lgc_configuration = prompt(questions)
        lgc_configuration = LgcConfiguration(mod=int(lgc_configuration['mod']), seed=int(lgc_configuration['seed']),
                                             multiplier=int(lgc_configuration['multiplier']),
                                             increment=int(lgc_configuration['increment']))
        random_numbers = generate_lcg(num_iterations=configuration['num_iterations'],
                                      lgc_configuration=lgc_configuration)
    elif answers['generator'] == 'middle_squares':
        questions = [
            {
                'type': 'input',
                'name': 'seed',
                'message': 'Ingrese semilla'
            },
            {
                'type': 'input',
                'name': 'length',
                'message': 'Ingrese longitud de los números aleatorios'
            }]
        middle_squares_configuration = prompt(questions)
        random_numbers = middle_squares(num_iterations=int(configuration['num_iterations']),
                                        seed=int(middle_squares_configuration['seed']),
                                        length=int(middle_squares_configuration['length']))
    elif answers['generator'] == 'python_rand':
        questions = [
            {
                'type': 'input',
                'name': 'seed',
                'message': 'Ingrese semilla'
            }]
        python_rand_configuration = prompt(questions)
        random_numbers = python_rand(num_iterations=int(configuration['num_iterations']),
                                     seed=int(python_rand_configuration['seed']))

    write_array_to_file(random_numbers, configuration['file_name'])


def validate_random_numbers():
    questions = [
        {
            'type': 'input',
            'name': 'file_path',
            'message': 'Path del archivo con los números aleatorios'
        },
        {
            'type': 'input',
            'name': 'significance_level',
            'message': 'Ingrese el nivel de significancia para la prueba'
        },
        {
            'type': 'checkbox',
            'name': 'test',
            'message': 'Elegir pruebas a realizar',
            'choices': [
                {
                    'name': 'Chi-cuadrado',
                    'value': 'chi_squared'
                },
                {
                    'name': 'Kolmogorov-Smirnov',
                    'value': 'kolmogorov_smirnov'
                },
                {
                    'name': 'Rachas',
                    'value': 'streaks'
                },
                {
                    'name': 'Serial',
                    'value': 'serial'
                }
            ]
        }
    ]
    answers = prompt(questions)
    random_numbers = read_file_to_array(answers['file_path'])
    results = None
    for test in answers['test']:
        if test == 'serial':
            print('Prueba de uniformidad serial')
            dimensions = int(input("Ingrese cantidad de dimensiones para hacer la prueba: "))
            freedom_degrees = int(input("Ingrese grados de libertad (intervalos del histograma): "))
            results = serial_uniformity_test(random_numbers=random_numbers.copy(),
                                             significance_level=float(answers['significance_level']),
                                             dimensions=dimensions, freedom_degrees=freedom_degrees)
        elif test == 'chi_squared':
            print('Prueba de uniformidad Chi-Cuadrado')
            results = chi_square_uniformity_test(random_numbers=random_numbers.copy(),
                                                 significance_level=float(answers['significance_level']))
        elif test == 'kolmogorov_smirnov':
            print('Prueba de uniformidad Kolmogorov-Smirnov')
            results = kolmogorov_smirnov_uniformity_test(random_numbers=random_numbers.copy(),
                                                         significance_level=float(answers['significance_level']))
        elif test == 'streaks':
            print('Prueba de independencia Rachas')
            results = streaks_independence_test(random_numbers=random_numbers.copy(),
                                                significance_level=float(answers['significance_level']))
        process_results(results)


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
    main()
