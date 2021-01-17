def is_palindrome(element):
    revered_element = element[::-1]
    if element == revered_element:
        return True
    return False


def separate_element(text, separator):
    numbers_as_strings = text.split(separator)
    return numbers_as_strings


data = input()
nums_strings = separate_element(data, ", ")

for el in nums_strings:
    print(is_palindrome(el))