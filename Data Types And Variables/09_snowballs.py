number_snowballs = int(input())
max_snowball = -999999999999999
snow = ''
time = ''
quality = ''

for snowball in range(1, number_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > max_snowball:
        max_snowball = snowball_value
        snow = snowball_snow
        time = snowball_time
        quality = snowball_quality
print(f'{snow} : {time} = {max_snowball:.0f} ({quality})')