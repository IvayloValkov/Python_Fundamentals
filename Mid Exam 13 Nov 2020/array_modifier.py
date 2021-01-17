array1 = [int(i) for i in input().split()]
command = input()


# new_num = 0

def swap(array, index_1, index_2):
    array[index_1], array[index_2] = array[index_2], array[index_1]
    return array


def multiply(array, index_1, index_2):
    array[index_1] = array[index_1] * array[index_2]
    # if array[index_1] > array[index_2]:
    #     array.pop(index_2)
    #     array.insert(index_2, new_num)
    # else:
    #     array.pop(index_1)
    #     array.insert(index_1, new_num)
    return array


while not command == "end":
    line = command.split()[0]
    if line == "swap":
        ind_1 = int(command.split()[1])
        ind_2 = int(command.split()[2])
        swap(array1, ind_1, ind_2)
    if line == "multiply":
        ind_1 = int(command.split()[1])
        ind_2 = int(command.split()[2])
        multiply(array1, ind_1, ind_2)
    if line == "decrease":
        for i in range(len(array1)):
            array1[i] -= 1
    command = input()

print(", ".join(str(i) for i in array1))