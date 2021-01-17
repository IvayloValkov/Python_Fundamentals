n_electrons = int(input())
electrons = []
cell_number = 1
while n_electrons > 0:
    possible_electron = 2 * cell_number ** 2
    if possible_electron > n_electrons:
        electrons.append(n_electrons)
    else:
        electrons.append(possible_electron)
    n_electrons -= possible_electron
    cell_number += 1

print(electrons)