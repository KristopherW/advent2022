import sys

"""
Rock = 1 = A   Paper = 2 = B  Scissors = 3 = C
Lose = 0 = X    Draw = 3 = Y   Win = 6 = Z
"""

input = None

try:
    input = open(sys.argv[1], "r")
except:
    print("You forgot the input you silly goose")

rounds = input.read().splitlines()
total_points = 0

for round in rounds:
    moves = round.split(" ")

    if moves[0] == "A":
        if moves[1] == "X":
            total_points += 3
        elif moves[1] == "Y":
            total_points += 4
        else:
            total_points += 8

    elif moves[0] == "B":
        if moves[1] == "X":
            total_points += 1
        elif moves[1] == "Y":
            total_points += 5
        else:
            total_points += 9

    else:
        if moves[1] == "X":
            total_points += 2
        elif moves[1] == "Y":
            total_points += 6
        else:
            total_points += 7

print(total_points)