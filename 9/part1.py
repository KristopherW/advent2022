import sys

input = open(sys.argv[1], 'r').read().splitlines()

# Set our starting positions
head = [0, 0]
tail = [0, 0]

# We only need to count if we've visited a space once, so use a set to remove dupes
visited_spaces = set()

for move in input:
    move = move.split(" ")

    # Check which move we're making
    match move[0]:
        case "R":
            # Get the number of moves being made and loop that many times
            for i in range(int(move[1])):
                # Move the head
                head[0] += 1
                # Check if the head is too far away from the tail and if so move the tail
                if abs(head[0] - tail[0]) > 1:
                    # If head and tail are on same row, move to the right
                    if head[1] == tail[1]:
                        tail[0] += 1
                    # If head is a row above the tail, move tail over and up one
                    elif head[1] > tail[1]:
                        tail[0] += 1
                        tail[1] += 1
                    # If the head is a row below the tail, move the tail over and down one
                    elif head[1] < tail[1]:
                        tail[0] += 1
                        tail[1] += -1
                # Once we're done moving around, add the current tail position to our set
                visited_spaces.add("[" + str(tail[0]) + ", " + str(tail[1]) + "]")

        case "L":
            for i in range(int(move[1])):
                head[0] += -1
                if abs(head[0] - tail[0]) > 1:
                    if head[1] == tail[1]:
                        tail[0] += -1
                    elif head[1] > tail[1]:
                        tail[0] += -1
                        tail[1] += 1
                    elif head[1] < tail[1]:
                        tail[0] += -1
                        tail[1] += -1
                visited_spaces.add("[" + str(tail[0]) + ", " + str(tail[1]) + "]")

        case "U":
            for i in range(int(move[1])):
                head[1] += 1
                if abs(head[1] - tail[1]) > 1:
                    if head[0] == tail[0]:
                        tail[1] += 1
                    elif head[0] > tail[0]:
                        tail[0] += 1
                        tail[1] += 1
                    elif head[0] < tail[0]:
                        tail[0] += -1
                        tail[1] += 1
                visited_spaces.add("[" + str(tail[0]) + ", " + str(tail[1]) + "]")

        case "D":
            for i in range(int(move[1])):
                head[1] += -1
                if abs(head[1] - tail[1]) > 1:
                    if head[0] == tail[0]:
                        tail[1] += -1
                    elif head[0] > tail[0]:
                        tail[0] += 1
                        tail[1] += -1
                    elif head[0] < tail[0]:
                        tail[0] += -1
                        tail[1] += -1
                visited_spaces.add("[" + str(tail[0]) + ", " + str(tail[1]) + "]")

# Print length of set to get total number of unique spaces visited
print(len(visited_spaces))