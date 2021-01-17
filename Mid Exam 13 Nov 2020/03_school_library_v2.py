shelf = input().split("&")

command = input()

while not command == "Done":
    command_type = command.split(" | ")[0]
    book_name = command.split(" | ")[1]

    if command_type == "Add Book":
        if not book_name in shelf:
            shelf.insert(0, book_name)
    elif command_type == "Take Book":
        if book_name in shelf:
            shelf.remove(book_name)
    elif command_type == "Swap Books":
        book_name_2 = command.split(" | ")[2]
        if book_name in shelf and book_name_2 in shelf:
            book_idx = shelf.index(book_name)
            book_2_idx = shelf.index(book_name_2)
            shelf[book_idx], shelf[book_2_idx] = shelf[book_2_idx], shelf[book_idx]
    elif command_type == "Insert Book":
        shelf.append(book_name)
    elif command_type == "Check Book":
        index = int(command.split(" | ")[1])
        if 0 <= index <= len(shelf):
            print(shelf[index])

    command = input()

print(", ".join(shelf))