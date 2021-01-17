# n = int(input())
#
# for num in range(1, n + 1):
#     sum_of_digits = 0
#     digits = num
#
#     while digits > 0:
#         sum_of_digits += digits % 10
#         digits = int(digits / 10)

word_snake = input()

word_matches = ["water", "sand", "sun", "fish"]
match = 0

for i in range(len(word_matches)):
    match += word_snake.lower().count(word_matches[i])

print(match)
