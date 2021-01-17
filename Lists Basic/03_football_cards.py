# cards_new = input()
#
# cards_as_list = cards_new.split()
# cards = len(cards_as_list)
#
# a_team = 11
# b_team = 11
#
# for card in range(len(cards_as_list)):
#     if cards_as_list[0][0] == "A":
#         a_team -= 1
#     elif cards_as_list[0][0] == "B":
#         b_team -= 1
#
#
# if a_team < 7 or b_team < 7:
#     print(f'Team A - {a_team}; Team B - {b_team}')
#     print('Game was terminated')
#
# if cards == 0:
#     print(f'Team A - {a_team}; Team B - {b_team}')

team_A = 11
team_B = 11

cards_raw = input()
cards = cards_raw.split()
cards_left = len(cards)

for card in cards:
    if 'A' in card:
        team_A -= 1
    if 'B' in card:
        team_B -= 1
    cards_left -= 1
    if team_A < 7 or team_B < 7:
        print(f"Team A - {team_A}; Team B - {team_B}\nGame was terminated")
        break
    if cards_left == 0:
        print(f"Team A - {team_A}; Team B - {team_B}")
