import pygame
from random import randint

class Cell:
    def __init__(self, x_in, y_in, sprite_in = ''):
        self.x = x_in
        self.y = y_in
        self.sprite = sprite_in

class Cave:
    def __init__(self, columns, rows):
        self.cave = generate_cave(columns, rows)
        self.sprites = []
        for y in range(len(self.cave)):
            row = []
            for x in range(len(self.cave[0])):
                if self.cave[y][x]:  # rock wall
                    row.append(Cell(x, y, "resources\\floor_tiles\\dirt\\dark.png"))
                elif self.cave[y-1][x] and self.cave[y][x-1]:  # top left
                    row.append(Cell(x, y, "resources\\floor_tiles\\dirt\\top_left.png"))
                elif self.cave[y-1][x] and self.cave[y][x+1]:  # top right
                    row.append(Cell(x, y, "resources\\floor_tiles\\dirt\\top_right.png"))
                elif self.cave[y-1][x]:  # top middle
                    row.append(Cell(x, y, "resources\\floor_tiles\\dirt\\top_middle.png"))
                elif self.cave[y][x-1] and self.cave[y+1][x]:  # bottom left
                    row.append(Cell(x, y, "resources\\floor_tiles\\dirt\\bottom_left.png"))
                elif self.cave[y][x+1] and self.cave[y+1][x]:  # bottom right
                    row.append(Cell(x, y, "resources\\floor_tiles\\dirt\\bottom_right.png"))
                elif self.cave[y+1][x]:  # bottom middle
                    row.append(Cell(x, y, "resources\\floor_tiles\\dirt\\bottom_middle.png"))
                elif self.cave[y][x-1]:  # middle left
                    row.append(Cell(x, y, "resources\\floor_tiles\\dirt\\middle_left.png"))
                elif self.cave[y][x+1]:  # middle right
                    row.append(Cell(x, y, "resources\\floor_tiles\\dirt\\middle_right.png"))
                else:  # middle middle
                    row.append(Cell(x, y, "resources\\floor_tiles\\dirt\\middle_middle.png"))
            self.sprites.append(row)


        

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
