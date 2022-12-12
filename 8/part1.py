import sys

input = open(sys.argv[1], 'r').read().splitlines()

# Turn the input into a 2D array for easier traversal
input_array = []
for line in input:
    input_array.append(list(map(int, [char for char in line])))

visible_trees = 0

# Start working our way through each tree in the array
for x, row in enumerate(input_array):
    for y, tree in enumerate(row):
    
        # Set up some vars to assist us with our traversal
        north, south = y, y
        east, west = x, x
        n_vis, s_vis, e_vis, w_vis = True, True, True, True
        
        # Check all the trees to the north, if there is a taller tree then
        # set north visibility to false.  If a tree is on an edge then we
        # dont enter the while loop and therefore the visibility is true.
        while north > 0:
            if input_array[x][north-1] >= tree:
                n_vis = False
                break
            north += -1

        # If tree is visible from the north, then we skip because we dont
        # need to verify from each side.  Repeat process for each direction.
        if not n_vis:
            while south < len(input_array)-1:
                if input_array[x][south+1] >= tree:
                    s_vis = False
                    break
                south += 1

        if not s_vis:
            while east < len(input_array)-1:
                if input_array[east+1][y] >= tree:
                    e_vis = False
                    break
                east += 1

        if not e_vis:
            while west > 0:
                if input_array[west-1][y] >= tree:
                    w_vis = False
                    break
                west += -1

        # If the tree is visible from any direction, increment the count
        if n_vis or s_vis or e_vis or w_vis:
            visible_trees += 1
                    
print(visible_trees)