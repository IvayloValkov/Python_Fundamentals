line = input()
total_power = 0
i = 0
while i < len(line):
    ch = line[i]

    if ch == ">":
        power = int(line[i+1])
        total_power += power
    else:
        if total_power > 0:
            line = line[:i] + line[i+1:]
            total_power -= 1
            continue
    i += 1

print(line)