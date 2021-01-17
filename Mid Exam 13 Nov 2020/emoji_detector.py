def is_valid(emoji):
    is_valid = False
    is_surrounded = False
    at_least_seven = False
    starts_with_upper = False
    continues_lower = False

    if emoji[:2] == emoji[-2:]:
        is_surrounded = True
    if len(emoji) >= 7:
        at_least_seven = True
    if emoji[2].isupper():
        starts_with_upper = True
    if emoji[3:-2].islower() and emoji[3:-2].isalpha():
        continues_lower = True
    if is_surrounded and at_least_seven and starts_with_upper and continues_lower:
        is_valid = True
    return is_valid


def find_emojies(text):
    potential_emojies = []
    text = string.replace("::", "**")
    while "**" in text:
        start_index = text.find("**")
        text = text[start_index:]
        next_index = text[2:].find("**") + 4
        emoji = text[:next_index]

        if is_valid(emoji):
            potential_emojies.append(emoji)
            text = text[next_index:]
        else:
            text = text[2:]
    return potential_emojies


def fix_it(potential_emojies, string):
    new_emojies = []
    for index, emoji in enumerate(potential_emojies):
        if emoji[2:-2] in string:
            check = string.index(emoji[2:-2]) - 1
            check_2 = string.index(emoji[2:-2]) + len(emoji[2:-2]) + 1
            if (string[check] == ":" or string[check_2] == ":") and string[check] == string[check_2]:
                new_emoji = "::" + emoji[2:-2] + "::"
                new_emojies.append(new_emoji)
            elif string[check] == "*" and string[check_2] == "*":
                new_emojies.append(emoji)
    return new_emojies


def coolness(string):
    coolness = 1
    for char in string:
        if char.isdigit():
            coolness *= int(char)
    return coolness


def cool(emoji):
    cool = 0
    for char in emoji:
        if char.isalpha():
            char = ord(char)
            cool += char
    return cool


string = input()
check_emojies = find_emojies(string)
valid_emojies = fix_it(check_emojies, string)
coolthrashhold = coolness(string)

print(f"Cool threshold: {coolthrashhold}")
print(f"{len(valid_emojies)} emojis found in the text. The cool ones are:")
for emoji in valid_emojies:
    if cool(emoji) >= coolthrashhold:
        print(emoji)