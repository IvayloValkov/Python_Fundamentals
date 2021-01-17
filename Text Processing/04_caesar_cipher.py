word_to_encrypt = input()

for ch in word_to_encrypt:
   print(chr(ord(ch) + 3), end="")
