# can only go down or left 
def paths_through_maze(maze):
    if maze[0][0] != 0: return 0 # no solution
    if maze[-1][-1] != 0: return 0 # no solution
    width, height = len(maze[0]), len(maze)
    for y in range(height):
        for x in range(width):
            cell = maze[y][x]
            numer_of_ways_to_reach = 0
            if cell == 0: # not a wall
                numer_of_ways_to_reach += maze[y - 1][x] if y > 0 else 0
                numer_of_ways_to_reach += maze[y][x - 1] if x > 0 else 0
            if x == 0 and y == 0:
                numer_of_ways_to_reach = 1
            maze[y][x] = numer_of_ways_to_reach
    return maze[-1][-1]
