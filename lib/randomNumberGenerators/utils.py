def calculate_central_digits(n, length):
    n_string = str(n)
    number_length = len(n_string)

    difference = number_length - length
    remainder = difference % 2
    if remainder != 0:
        n = n * pow(10, remainder)

    index = (len(str(n)) - length) / 2
    n = str(n)
    index_inicial = int(index)
    index_final = int(index_inicial + length)
    central_digits = n[index_inicial:index_final]
    return int(central_digits)
