def ascii_table_characters(start_string, end_string):
    for char in range(ord(character_1) + 1, ord(character_2)):
        result = chr(char)
        print(result, end =" ")


character_1 = input()
character_2 = input()
ascii_table_characters(start_string=character_1, end_string=character_2)
