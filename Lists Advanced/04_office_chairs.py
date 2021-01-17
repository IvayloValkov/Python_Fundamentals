rooms = int(input())
free_chairs = 0
enough_chairs = 0
#has_enough_chairs = True
for room in range(1, rooms + 1):
    chairs, people = input().split()
    people = int(people)
    #room_data = input().split()
    #chairs_count = len(room_data[0])
    #number_of_people = int(room_data[1])

    if len(chairs) >= people:
        free_chairs += len(chairs) - people
        enough_chairs += 1

    elif len(chairs) < people:
        #has_enough_chairs = False
        print(f'{people - len(chairs)} more chairs needed in room {room}')


if enough_chairs == rooms:
#has_enough_chairs = True
    print(f"Game On, {free_chairs} free chairs left")


