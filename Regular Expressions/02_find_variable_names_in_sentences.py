import re

data = input()

    # pattern = r"\b_([a-zA-Z0-9]+\b)"
pattern = r"\b(_)([a-zA-Z0-9]+\b)"

    # words = re.findall(pattern, data)
words = re.finditer(pattern, data)
words = [word.group(2) for word in words]
    # words = [word for word in words]
                # variable_names = []
                # for word in words:
                #     variable_names.append(word[1])
                # print(",".join(variable_names))
print(','.join(words))

