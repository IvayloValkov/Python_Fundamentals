substrings_words = input().split(", ")
words = input().split(", ")

matches_words = []

for substring in substrings_words:
    for word in words:
        if substring in word and substring not in matches_words:
            matches_words.append(substring)

print(matches_words)