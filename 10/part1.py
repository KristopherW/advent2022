import sys

# Helper function to check if we're on a cycle where we need to update the signal strength
def cycle_check(num_cycles, register):
    # Check if its a cycle we care about
    if num_cycles in [20, 60, 100, 140, 180, 220]:
        # Do the signal strength math
        return num_cycles * register
    else:
        return 0


input = open(sys.argv[1], 'r').read().splitlines()

# Set up our tracking vars
x_register = 1
cycle = 1
signal_strength_sum = 0

# Loop through input
for i, line in enumerate(input):
    # If noop, we bump the cycle and check if we need to update signal strength
    if line == "noop":
        cycle += 1
        signal_strength_sum += cycle_check(cycle, x_register)
    
    # If we are updating the register
    elif line.startswith("addx"):
        line = line.split(" ")
        # Bump the cycle and check if we need to update signal strength
        cycle += 1
        signal_strength_sum += cycle_check(cycle, x_register)
        # Update the register
        x_register += int(line[1])
        # Bump the cycle and check if we need to update signal strength
        cycle += 1
        signal_strength_sum += cycle_check(cycle, x_register)

print(signal_strength_sum)