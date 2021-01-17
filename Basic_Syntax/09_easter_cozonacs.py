budget = float(input())
flour = float(input())

eggs = flour * 0.75
milk_one_l = flour * 1.25
milk_250 = milk_one_l / 4

one_cozunac_price = flour + eggs + milk_250
cnt = 0
colored_eggs = 0

while budget >= one_cozunac_price:
    cnt += 1
    budget -= one_cozunac_price
    colored_eggs += 3
    if cnt % 3 == 0:
        colored_eggs -= (cnt - 2)
print(f'You made {cnt} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')