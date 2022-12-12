import sys

input = open(sys.argv[1], 'r').read().splitlines()

# Turn the input into a 2D array for easier traversal
input_array = []
for line in input:
    input_array.append(list(map(int, [char for char in line])))

best_tree = []

# Start working our way through each tree in the array
for x, row in enumerate(input_array):
    for y, tree in enumerate(row):
    
        # Set up some vars to assist us with our traversal
        north, south = y, y
        east, west = x, x
        n_count, s_count, e_count, w_count = 0, 0, 0, 0
        
        # Check all the trees to the north, counting each tree till we either
        # hit an edge or a tree of equal or greater height
        while north > 0:
            if input_array[x][north-1] < tree:
                n_count += 1
                north += -1
            else:
                n_count += 1
                break

        while south < len(input_array)-1:
            if input_array[x][south+1] < tree:
                s_count += 1
                south += 1
            else:
                s_count += 1
                break

        while east < len(input_array)-1:
            if input_array[east+1][y] < tree:
                e_count += 1
                east += 1
            else:
                e_count += 1
                break

        while west > 0:
            if input_array[west-1][y] < tree:
                w_count += 1
                west += -1
            else:
                w_count += 1
                break

        # Calculate score
        best_tree.append(n_count * e_count * s_count * w_count)

print(max(best_tree))