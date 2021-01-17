num = int(input())

for first_letter in range(0, num):
    for second_letter in range(0, num):
        for third_letter in range(0, num):
            print(f"{chr(97 + first_letter)}{chr(97 + second_letter)}{chr(97 + third_letter)}")