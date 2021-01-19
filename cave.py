import pygame
from random import randint

# Map generation
x, y = 50, 50

def generate_cave():
    '''
    Returns an array of bools. True represents a wall, False is open space.
    Cellular automata is used to produce more natural caves
    '''
    # Generate initial cave
    cave = []
    for i in range(y):
        row = []
        if i == 0 or i == y - 1:
            for _ in range(x):
                row.append(True)
        else:
            for j in range(x):
                if j == 0 or j == x - 1:
                    row.append(True)
                else:
                    row.append(True if randint(0, 1) else False)
        cave.append(row)
    # update cave using cellular automata to make it more player friendly
    birth_limit, death_limit = 5, 4
    new_cave = cave
    for i in range(x):
        for j in range(y):
            # if a cell has too few neighbors, then it "dies" and becomes a wall
            if count_neighbors(i, j, cave) < death_limit:
                new_cave[i][j] = False
            # if a cell has lots of air around it, that cell is set to air
            elif count_neighbors(i, j, cave) > birth_limit:
                new_cave[i][j] = True


def count_neighbors(x_in, y_in, cave):
    '''
    returns count of how many neighbors given cell has
    '''
    neighbors = 0
    if x_in == 0 or y_in == 0 or x_in == x - 1 or y_in == y - 1:
        # edges should always stay solid, so let's give them the max possible neighbors
        neighbors = 8
    else:
        for i in range(-1, 2):
            for j in range(-1, 2):
                # check all cells that are surrounding the center (1, 1) and if they are True, +1 neighbors
                if not i == 1 and not j == 1:
                    if cave[x_in + i][y_in + j]:
                        neighbors += 1

    return neighbors




def print_cave(cave):
    for row in cave:
        for i in row:
            char = '##' if i else '  '
            print(char, end='')
        print("")

generate_cave()

