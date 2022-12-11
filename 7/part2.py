import sys


input = open(sys.argv[1], 'r').read().splitlines()

# Making this a set because we only need to keep track of each dir once
directories = set()

# Making this a dict so that we can key each file using its path
files_seen = {}

# Keep track of current directory
current_dir = []

for line in input:
    line = line.split(" ")

    # Check and see if we're moving directories
    if line[1] == "cd":
        # Dont care about root dir
        if line[2] == "/":
            continue
        # Check if we're moving up a directory and pop if the list is long enough to allow
        elif line[2] == ".." and current_dir:
            current_dir.pop(-1)
        # Otherwise add the dir name to our current dir list
        else:
            current_dir.append(line[2])
    # Ignore ls commands
    elif line[1] == "ls":
        continue
    else:
        # Ignore dir commands
        if line[0] == "dir":
            continue
        # If we got here then we're looking at a file, record its size and key based on its path
        else:
            files_seen["/".join(current_dir + [line[1]])] = int(line[0])
    
    # After everything, take the current dir path and add it to our list of directories if 
    # it doesnt already exist
    directories.add("/".join(current_dir))

# Get a list of each dir and their size
dir_sizes = []
for dir in directories:
    file_size = 0
    for file in files_seen:
        # Check if the file path we're looking at is in our master list of directories
        # and add to our running total if it is.  This gets all files in each path.
        if str(file).startswith(dir):
            file_size += files_seen[file]
            
    dir_sizes.append(file_size)

# Need to figure out which dir to delete to free up enough space
# Get the current amount of free space
current_space = 70000000 - max(dir_sizes)

# Sort the list from least to greatest, we want to delete the first dir that gets 
# us the space we need
dir_sizes.sort()

# Loop through the dirs till we find one that when deleted makes enough space
for dir in dir_sizes:
    if current_space + dir >= 30000000:
        print(dir)
        break