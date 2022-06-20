from numpy import loadtxt


def write_array_to_file(array, text_file_name):
    outFile = open(text_file_name, "w")
    size = len(array)
    counter = 0
    while counter < size:
        # Write to file
        writeValue = str(array[counter])
        outFile.write(writeValue + "\n")
        counter = counter + 1

    print(f"Successfully stored {size} random numbers in file named: '{text_file_name}'")

    outFile.close()


def read_file_to_array(text_file_name):
    array = loadtxt(text_file_name)
    return array
