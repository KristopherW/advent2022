import sys

input = open(sys.argv[1], 'r')

elf_pairs = input.read().splitlines()

# Go through each pair and see if there's overlap
total_overlaps = 0

for pair in elf_pairs:
    #Split each pair into the individual elves and split their section into an int list
    elves = pair.split(',')
    elf1 = list(map(int, elves[0].split('-')))
    elf2 = list(map(int, elves[1].split('-')))

    # Do a quick check to see if the sections are an exact match, if so we increment the total.
    if elf1 == elf2:
        total_overlaps += 1   

    else:
        # Do some quick mafs to determine the larger section so that we can compare correctly
        if elf1[1] - elf1[0] > elf2[1] - elf2[0]:
            # Weve determined that elf1 has the larger section, so we check if elf2 fits within
            if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
                total_overlaps += 1  
        else:
            # Weve determined that elf2 has the larger section, so we check if elf1 fits within
            if elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
                total_overlaps += 1
 
print(total_overlaps)