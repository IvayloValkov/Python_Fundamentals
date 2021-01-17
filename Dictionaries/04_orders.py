def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value

def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))

product = input()
prices = {}
quantities = {}

while not product == "buy":
    name = product.split()[0]
    price = float(product.split()[1])
    quantity = int(product.split()[2])

    prices[name] = price

    if name not in quantities:
        quantities[name] = 0

    quantities[name] += quantity

    product = input()

for (key, price) in prices.items():
    total_sum = price * quantities[key]
    print(f'{key} -> {total_sum:.2f}')
