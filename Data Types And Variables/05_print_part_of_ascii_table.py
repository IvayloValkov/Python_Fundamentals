start_symbol = int(input())
final_symbol = int(input())

for symbol in range(start_symbol, final_symbol + 1):
    print(chr(symbol), end=" ")