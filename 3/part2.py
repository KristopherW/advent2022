import sys

input = open(sys.argv[1], "r")

# Need to split sacks into groups of three sets
rucksacks = input.read().splitlines()
groups = []

for x in range(int(len(rucksacks) / 3)):
    y = 0
    group = []
    while y != 3:
        group.append(set(rucksacks.pop(0)))
        y += 1
    
    groups.append(group)

# Go through each group and find the common object using set intersection
objects = []
for group in groups:
    s1s2_common = group[0].intersection(group[1])
    objects.append(s1s2_common.intersection(group[2]))

# Calculate the total priority of the objects
total_priority = 0

# Check if char is upper or lower case and then use some math to get its
# value based on its ascii value so we dont need a big table of values
for object in objects:
    for char in object:
        if char.islower():
            total_priority += (ord(char) - 96)
        else:
            total_priority += (ord(char) - 38)

print(total_priority)