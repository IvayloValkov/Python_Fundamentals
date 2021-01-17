cards = input().split()
shuffle_count = int(input())
middle_lenght = len(cards) // 2

for i in range(shuffle_count):
    res = []

    for index in range(middle_lenght):
        first_card = cards[index]

        current_index_second_deck = index + middle_lenght
        second_card = cards[current_index_second_deck]

        res.append(first_card)
        res.append(second_card)

    cards = res

print(cards)