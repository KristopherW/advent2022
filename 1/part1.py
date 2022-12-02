import sys

input = None
try:
    input = open(sys.argv[1], "r")
except:
    print("No input file provided")

elves = input.read().splitlines()
total_calories = []
current_sum = 0

for cal in elves:
    if cal != '':
        current_sum += int(cal)
    else:
        total_calories.append(current_sum)
        current_sum = 0

print(max(total_calories))