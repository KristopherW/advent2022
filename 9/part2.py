# Ended up making part two a bit cleaner, solution to part one wasnt 
# going to work well with more than two knots

import sys


input = open(sys.argv[1], 'r').read().splitlines()

# Helper function to update the tail after the head moves
def updateTail(knots):
    # Using a for loop and grabbing the knots in groups of twos moving one over each loop
    for x in range(len(knots)-1):
        # Special case for when a knot is two moves in both x and y coordinates
        if abs((knots[x][0]) - knots[x+1][0]) > 1 and abs((knots[x][1]) - knots[x+1][1]) > 1:
            knots[x+1][0] += int((knots[x][0] - knots[x+1][0]) / 2)
            knots[x+1][1] += int((knots[x][1] - knots[x+1][1]) / 2)
        
        # Need to break things down if we're moving two moves on only one axis
        # Might be cleaner way to do this but this is what came to mind first
        elif abs((knots[x][0]) - knots[x+1][0]) > 1 or abs((knots[x][1]) - knots[x+1][1]) > 1:
            if knots[x][0] - knots[x+1][0] == 2:
                knots[x+1][0] += int((knots[x][0] - knots[x+1][0]) / 2)
                knots[x+1][1] += knots[x][1] - knots[x+1][1]

            elif knots[x][0] - knots[x+1][0] == -2:
                knots[x+1][0] += int((knots[x][0] - knots[x+1][0]) / 2)
                knots[x+1][1] += knots[x][1] - knots[x+1][1]

            elif knots[x][1] - knots[x+1][1] == 2:
                knots[x+1][0] += knots[x][0] - knots[x+1][0]
                knots[x+1][1] += int((knots[x][1] - knots[x+1][1]) / 2)

            elif knots[x][1] - knots[x+1][1] == -2:
                knots[x+1][0] += knots[x][0] - knots[x+1][0]
                knots[x+1][1] += int((knots[x][1] - knots[x+1][1]) / 2)
    
    return knots
            
# Set our starting positions
knots = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

# We only need to count if we've visited a space once, so use a set to remove dupes
visited_spaces = set()

for move in input:
    move = move.split(" ")
   # Process the move commands
    match move[0]:
        case "R":
            for i in range(int(move[1])):
                # Move the head
                knots[0][0] += 1
                # Update the rest of the knots
                knots = updateTail(knots)
                # Add the location of the tail knot to the list of visited spaces
                visited_spaces.add("[" + str(knots[-1][0]) + ", " + str(knots[-1][1]) + "]")

        case "L":
            for i in range(int(move[1])):
                knots[0][0] += -1
                knots = updateTail(knots)
                visited_spaces.add("[" + str(knots[-1][0]) + ", " + str(knots[-1][1]) + "]")

        case "U":
            for i in range(int(move[1])):
                knots[0][1] += 1
                knots = updateTail(knots)
                visited_spaces.add("[" + str(knots[-1][0]) + ", " + str(knots[-1][1]) + "]")

        case "D":
            for i in range(int(move[1])):
                knots[0][1] += -1
                knots = updateTail(knots)
                visited_spaces.add("[" + str(knots[-1][0]) + ", " + str(knots[-1][1]) + "]")

# Print number of unique spaces visited
print(len(visited_spaces))