word = input()

for index in range(len(word)):
    char = word[index]

    if index + 1 == len(word) or char != word[index+1]:
        print(char, end="")

