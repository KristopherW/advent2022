import sys

"""
Rock     = 1 = A/X
Paper    = 2 = B/Y
Scissors = 3 = C/Z

Win = 6     Draw = 3    Loss = 0
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
            total_points += 4
        elif moves[1] == "Y":
            total_points += 8
        else:
            total_points += 3

    elif moves[0] == "B":
        if moves[1] == "X":
            total_points += 1
        elif moves[1] == "Y":
            total_points += 5
        else:
            total_points += 9

    else:
        if moves[1] == "X":
            total_points += 7
        elif moves[1] == "Y":
            total_points += 2
        else:
            total_points += 6

print(total_points)