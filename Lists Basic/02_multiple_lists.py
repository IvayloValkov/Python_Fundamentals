factor = int(input())
counter = int (input())
multiple = factor * counter
mylist = []

for num in range(factor, multiple +1, factor):
    mylist.append(num)
print(mylist)