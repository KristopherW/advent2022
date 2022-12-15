import sys

# Helper function to determine what char we add to the crt row
def sprite_helper(cycle, register):
    # Each row has 40 elements, but the cycle we're on can go much higher
    # so we do a mod 40 on the cycle count to get its relative position in each
    # crt row.  This if checks to make sure we arent at the end of the row.
    if cycle % 40 != 0:
        # Checking if our three pixel sprite is overlapping the current cycle position.
        # The math on the register seems weird because of where we start our cycle count.
        if (register) <= (cycle % 40) <= (register + 2):
            return "#"
        else:
            return "."
    else:
        # If we are at the end of the row, the mod calculation returns 0 which we cant work with
        # so this special case handles that situation
        if (register) <= 40 <= (register + 2):
            return "#"
        else:
            return "."

# Helper function to update the crt rows.  Just figures out which row we need to update
# based on the current cycle and calls the sprite_helper to figure out what char to add
def update_crt(crt, cycle, register):
    if cycle < 41:
        crt[0] += sprite_helper(cycle, register)
    elif cycle < 81:
        crt[1] += sprite_helper(cycle, register)
    elif cycle < 121:
        crt[2] += sprite_helper(cycle, register)
    elif cycle < 161:
        crt[3] += sprite_helper(cycle, register)
    elif cycle < 201:
        crt[4] += sprite_helper(cycle, register)
    elif cycle <= 240:
        crt[5] += sprite_helper(cycle, register)
    
    return crt


input = open(sys.argv[1], 'r').read().splitlines()

# Set up our tracking vars
x_register = 1
cycle = 1
signal_strength_sum = 0
crt = ["#", "", "", "", "", ""]

# Loop through input
for i, line in enumerate(input):
    print(i+1)
    # If noop, we bump the cycle and update the crt
    if line == "noop":
        cycle += 1
        crt = update_crt(crt, cycle, x_register)
    
    # If updating the register, bump the cycle, update the crt, update the register, 
    # bump the cycle, and update the crt again
    elif line.startswith("addx"):
        line = line.split(" ")
        cycle += 1
        crt = update_crt(crt, cycle, x_register)
        x_register += int(line[1])
        cycle += 1
        crt = update_crt(crt, cycle, x_register)

# Print out the crt "display"
for row in crt:
    print(row)