def recursive_max(numbers: list):
    if len(numbers) == 1:
        return numbers[0]
    if len(numbers) == 2:
        if numbers[0] >= numbers[1]:
            return numbers[0]
        else:
            return numbers[1]
    if len(numbers) > 2:
        numbers[0] = recursive_max(numbers[0:2])
        numbers.pop(1)
        return recursive_max(numbers)

def recursive_max_file(my_file):
    file = open(my_file, "rt")
    numbers_strings = file.readlines()
    numbers = list(map(int, numbers_strings))
    return recursive_max(numbers)

############################### MAIN PROGRAM ###################################

print(recursive_max_file("numbers.txt"))
