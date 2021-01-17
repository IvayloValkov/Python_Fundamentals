string = input()
n = int(input())

result = []
s = string.split(" ")

for i in range(0, n):
    j = s[1:int(len(s) / 2)]
    p = s[int(len(s) / 2): -1]
    result = [None] * (len(p) + len(j))
    result[::2] = p
    result[1::2] = j
    result.append(s[-1])
    result.insert(0, s[0])
    s = result

print(s)