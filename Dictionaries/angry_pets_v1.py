items = list(map(int, input().split()))
penultimate = int(input())
items_to_break = input()
price_rating = input()

entry_point_price = items[penultimate]
half_list = (len(items) - 1) / 2
left_list = items[:penultimate]
right_list = items[penultimate + 1:]

if items_to_break == "cheap":
    left_list = [int(el) for el in left_list if int(el) < entry_point_price]
    right_list = [int(el) for el in right_list if int(el) < entry_point_price]
elif items_to_break == "expensive":
    left_list = [int(el) for el in left_list if int(el) >= entry_point_price]
    right_list = [int(el) for el in right_list if int(el) >= entry_point_price]

if price_rating == "positive":
    left_list = [int(el) for el in left_list if int(el) > 0]
    right_list = [int(el) for el in right_list if int(el) > 0]
elif price_rating == "negative":
    left_list = [int(el) for el in left_list if int(el) < 0]
    right_list = [int(el) for el in right_list if int(el) < 0]
elif price_rating == "all":
    left_list = [int(el) for el in left_list]
    right_list = [int(el) for el in right_list]

damage_left = sum(left_list)
damage_right = sum(right_list)

if damage_left == damage_right:
    print(f"Left - {damage_left}")
elif damage_left > damage_right:
    print(f"Left - {damage_left}")
else:
    print(f"Right - {damage_right}")