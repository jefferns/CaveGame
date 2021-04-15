
import pygame


class Entity:
    """
    Abstract class
    Purpose: Laying foundation for future concrete entity classes
    """
    def __init__(self, x, y, width, height, max_hp, attack, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attack = attack
        self.speed = speed
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.up = True
        self.still_sprite = pygame.image.load('resources/circle.png')
        self.walk_sprites_right = []
        self.walk_sprites_left = []
    
    def get_cells(self, cave):
        """
        Return list of the current cell and neighbor cells 
        """
        cells = []
        for row in cave.sprites:
            for cell in row:
                if (cell.x*15 in range(self.x - 30, self.x + 30)) and (cell.y*15 in range(self.y - 30, self.y + 30)):
                    cells += [cell]
        return cells



    def move_right():
        """
        Purpose: Step through the entity's right movement sprites
        ** To be defined in a concrete class **
        """
        pass

    def move_left():
        """
        Purpose: Step through the entity's left movement sprites
        ** To be defined in a concrete class **
        """
        pass

    def move_up():
        """
        Purpose: Step through the entity's upwards movement sprites
        ** To be defined in a concrete class **
        """
        pass

    def move_down():
        """
        Purpose: Step through the entity's downwards movement sprites
        ** To be defined in a concrete class **
        """
        pass

    def draw():
        """
        Purpose: Draw the entity's proper sprite
        ** To be defined in a concrete class **
        """
        pass


class Player(Entity):
    """
    User controlled player
    """
    

    def draw(self, window, sprite):
        return
    
    def move_left(self, speed):
        self.x -= speed

    def move_right(self, speed):
        self.x += speed

    def move_up(self, speed):
        self.y -= speed
    
    def move_down(self, speed):
        self.y += speed


class Zombie(Entity):
    """
    Slow-walking, tanky enemy
    """
