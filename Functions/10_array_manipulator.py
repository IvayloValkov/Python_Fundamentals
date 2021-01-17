def exchange(array, index):
    last_part = array[:index + 1]
    first_part = array[index + 1:]
    array = first_part
    array += last_part

    return array


def max_even(array):
    max_int = min(array)
    index = -1

    for i in range(0, len(array)):
        if array[i] >= max_int and array[i] % 2 == 0:
            max_int = array[i]
            index = i

    return index


def max_odd(array):
    max_int = min(array)
    index = -1

    for i in range(0, len(array)):
        if array[i] >= max_int and array[i] % 2 == 1:
            index = i
            max_int = array[i]

    return index


def max_index(array, parity):
    if parity == 'even':
        return max_even(array)

    return max_odd(array)


def min_even(array):
    min_int = max(array)
    index = -1

    for i in range(0, len(array)):
        if array[i] <= min_int and array[i] % 2 == 0:
            min_int = array[i]
            index = i

    return index


def min_odd(array):
    min_int = max(array)
    index = -1

    for i in range(0, len(array)):
        if array[i] <= min_int and array[i] % 2 == 1:
            min_int = array[i]
            index = i

    return index


def min_index(array, parity):
    if parity == 'even':
        return min_even(array)

    return min_odd(array)


def first_even_elements(array, count):
    even_only = list(filter(lambda el: el % 2 == 0, array))
    first_elements_array = []
    for i in range(len(even_only)):
        if count == 0:
            break
        first_elements_array.append(even_only[i])
        count -= 1

    return first_elements_array


def first_odd_elements(array, count):
    odd_only = list(filter(lambda el: el % 2 == 1, array))
    first_elements_array = []
    for i in range(len(odd_only)):
        if count == 0:
            break
        first_elements_array.append(odd_only[i])
        count -= 1

    return first_elements_array


def first_elements(array, count, parity):
    if parity == 'even':
        return first_even_elements(array, count)

    return first_odd_elements(array, count)


def last_even_elements(array, count):
    array = array[::-1]
    even_only = list(filter(lambda el: el % 2 == 0, array))
    last_elements_array = []
    for i in range(len(even_only)):
        if count == 0:
            break
        last_elements_array.append(even_only[i])
        count -= 1

    last_elements_array = last_elements_array[::-1]
    return last_elements_array


def last_odd_elements(array, count):
    array = array[::-1]
    odd_only = list(filter(lambda el: el % 2 == 1, array))
    last_elements_array = []
    for i in range(len(odd_only)):
        if count == 0:
            break
        last_elements_array.append(odd_only[i])
        count -= 1

    last_elements_array = last_elements_array[::-1]
    return last_elements_array


def last_elements(array, count, parity):
    if parity == 'even':
        return last_even_elements(array, count)

    return last_odd_elements(array, count)


arr = [int(i) for i in input().split(' ')]

word = input()
while word != 'end':

    commands = word.split(' ')

    if commands[0] == 'exchange':
        if int(commands[1]) >= len(arr) or int(commands[1]) < 0:
            print("Invalid index")
        else:
            arr = exchange(arr, int(commands[1]))
    elif commands[0] == 'max':
        res = max_index(arr, commands[1])
        if res == -1:
            print("No matches")
        else:
            print(res)
    elif commands[0] == 'min':
        res = min_index(arr, commands[1])
        if res == -1:
            print("No matches")
        else:
            print(res)
    elif commands[0] == 'first':
        if int(commands[1]) > len(arr):
            print("Invalid count")
        else:
            res = first_elements(arr, int(commands[1]), commands[2])
            print(res)
    elif commands[0] == 'last':
        if int(commands[1]) > len(arr):
            print("Invalid count")
        else:
            res = last_elements(arr, int(commands[1]), commands[2])
            print(res)

    word = input()

print(arr)