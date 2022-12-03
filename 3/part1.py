import sys

input = open(sys.argv[1], "r")

rucksacks = input.read().splitlines()

# Get list of common object in each sack
objects = []

for sack in rucksacks:
    # Get sack size and split it into its two compartments
    sack_size = len(sack)
    compartments = []
    compartments.append(sack[0 : int(sack_size/2)])
    compartments.append(sack[int(sack_size/2) : sack_size])

    # Start searching for the common object
    match_found = False
    common_object = None
    for object_x in compartments[0]:
        for object_y in compartments[1]:
            if object_x == object_y:
                match_found = True
                common_object = object_x

        # Only need to find one match so break out when one is found        
        if match_found:
            match_found = False
            objects.append(common_object)
            common_object = None
            break
            
# Calculate the total priority of the objects
total_priority = 0

# Check if char is upper or lower case and then use some math to get its
# value based on its ascii value so we dont need a big table of values
for object in objects:
    if object.islower():
        total_priority += (ord(object) - 96)
    else:
        total_priority += (ord(object) - 38)

print(total_priority)