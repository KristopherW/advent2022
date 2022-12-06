import sys

input = open(sys.argv[1], 'r').read().splitlines()

# Lets get the number of stacks we're dealing with and 
# the index for the row containing the bottom of the stack
num_stacks = 0
stack_bottom = 0

for id, row in enumerate(input):
    if row.startswith(" 1"):
        num_stacks = int(row[-2])
        stack_bottom = id
        break

# Do some likely unnecessary work to clean up the input to
# make it a bit easier to build the stacks
cleaned_input = []

for row in reversed(input[:stack_bottom]):
    if row.startswith(" 1"):
        break
    else:
        # Take each row and chunk it up into the individual stack elements
        crates = []

        for i in range(0, len(row), 4):
            crates.append(row[i:i+4].strip(' []'))
        
        cleaned_input.append(crates)

# Lets build the stacks
stacks = []

for i in range(num_stacks):
    stacks.append([crate[i] for crate in cleaned_input if crate[i] != ""])

# Alright now we can start moving things around
for move in input[stack_bottom + 2:]:
    # Isolate the important information from the move string
    # move_info[1] = number of crates to move
    # move_info[3] = from stack
    # move_info[5] = to stack
    move_info = move.split(' ')
    num_crates = int(move_info[1])

    while num_crates > 0:
        stacks[int(move_info[5]) - 1].append(stacks[int(move_info[3]) - 1].pop())
        num_crates -= 1
    
# Stacks should be in their final positions so lets grab the top from each
top_crates = ""
for stack in stacks:
    top_crates += stack[-1]

print(top_crates)