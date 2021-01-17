message = input().split(" ")

for word in message:
    new_message = ""
    first_letter_ascii = [letter for letter in word if letter.isdigit()]
    left_characters = [letter for letter in word if letter.isalpha()]
    left_characters[0], left_characters[-1] = left_characters[-1], left_characters[0]
    first_letter_ascii = chr(int("".join(first_letter_ascii)))
    new_message += first_letter_ascii + ''.join(left_characters)
    print(new_message, end=" ")