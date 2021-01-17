def factorial(n_1, n_2):
    n1 = n_1
    n2 = n_2

    def factorial_n1(n1):
        if n1 == 0:
            return 1
        else:
            return n1 * factorial_n1(n1 - 1)

    def factorial_n2(n2):
        if n2 == 0:
            return 1
        else:
            return n2 * factorial_n2(n2 - 1)

    return factorial_n1(n1) // factorial_n2(n2)


number_1 = int(input())
number_2 = int(input())

print(f"{factorial(number_1, number_2):.2f}")