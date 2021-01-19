import pygame
from random import randint


def generate_cave(x, y):
    '''
    Returns an array of bools. True represents a wall, False is open space.
    Cellular automata is used to produce more natural caves
    '''
    # Generate initial cave
    cave = []
    for i in range(x):
        row = []
        if i == 0 or i == x - 1:
            for _ in range(y):
                row.append(True)
        else:
            for j in range(y):
                if j == 0 or j == y - 1:
                    row.append(True)
                else:
                    row.append(True if randint(0, 1) else False)
        cave.append(row)

    # update cave using cellular automata to make it more player friendly
    birth_limit, death_limit = 3, 3
    new_cave = []
    for i in range(x):
        row = []
        for j in range(y):
            # if a cell has too few neighbors, then it "dies" and becomes a wall
            if cave[i][j]:
                if count_neighbors(i, j, cave, x, y) < death_limit:
                    row.append(False)
                else:
                    row.append(True)
            # if a cell has lots of air around it, that cell is set to air
            else:
                if count_neighbors(i, j, cave, x, y) > birth_limit:
                    row.append(True)
                else:
                    row.append(False)
        new_cave.append(row)
    return new_cave


def count_neighbors(x_in, y_in, cave, x, y):
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
    '''
    Prints the cave into the terminal. Used for debugging.
    '''
    for row in cave:
        for i in row:
            char = '*' if i else ' '
            print(char, end='')
        print("")