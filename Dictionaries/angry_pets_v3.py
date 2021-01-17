price_ratings = [int(el) for el in input().split()]
entry_point = int(input())
items_type = input()
price_ratings_type = input()

left_items = price_ratings[:entry_point]
right_items = price_ratings[entry_point + 1:]

if items_type == "cheap":
    left_items = [el for el in left_items if el < price_ratings[entry_point]]
    right_items = [el for el in right_items if el < price_ratings[entry_point]]

elif items_type == "expensive":
    left_items = [el for el in left_items if el >= price_ratings[entry_point]]
    right_items = [el for el in right_items if el >= price_ratings[entry_point]]

if price_ratings_type == "positive":
    left_items = [el for el in left_items if el > 0]
    right_items = [el for el in right_items if el > 0]

elif price_ratings_type == "negative":
    left_items = [el for el in left_items if el < 0]
    right_items = [el for el in right_items if el < 0]

if sum(left_items) >= sum(right_items):
    print(f"Left - {sum(left_items)}")
else:
    print(f"Right - {sum(right_items)}")