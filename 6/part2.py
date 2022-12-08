import sys

# Read in the input as a single string
input = open(sys.argv[1], 'r').read()

# Look at groups of 4 chars, moving one char to the right on each loop
for i in range(len(input)-13):
    # Since sets cant contain duplicates, set the string of the four current chars to a set
    temp_chars = set(input[i:i+14])

    # If the length of the set is 4, we know theres no duplicates.  Return the index of the last char.
    if len(temp_chars) == 14:
        print(i+14)
        break