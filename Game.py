import pygame
import time

from cave import Cave
from entity import Player
from menu import Button


pygame.init()


screen_height = 600
screen_width = 900

window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dungeon Game")

# Background Creation
class Background:
    def __init__(self, x, y, height, width, path):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.image = pygame.image.load(path)

# Generate inital cave
cave = Cave(screen_height // 15, screen_width // 15)

# Main Menu Aspects
menu_bg = Background(0, 0, screen_height, screen_width, 'resources/menu/menu_bg.png')
start_button = Button(330, 270, 60, 240, 'start_button', 'resources/menu/')
exit_button = Button(330, 360, 60, 240, 'exit_button', 'resources/menu/')

def draw_menu():
    window.blit(menu_bg.image, (menu_bg.x, menu_bg.y))
    window.blit(start_button.image, (start_button.x, start_button.y))
    window.blit(exit_button.image, (exit_button.x, exit_button.y))
    pygame.display.update()


# Character Creation
# Class definition in entity.py
user = Player(450, 350, 13, 30, 100, 5, 3)

# Main Draw function
def redraw():
    for row in cave.sprites:
        for cell in row:
            window.blit(pygame.image.load(cell.sprite), (cell.x * 15, cell.y * 15))
    window.blit(user.still_sprite, (user.x, user.y))
    pygame.display.update()


##################################
# Main Menu
##################################
menu = True
start_button.select()
while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        if start_button.selected:
            run = True
            menu = False
        elif exit_button.selected:
            menu = False
            run = False
    elif keys[pygame.K_UP]:
        if exit_button.selected:
            start_button.select()
            exit_button.unselect()
        elif start_button.selected:
            start_button.unselect()
            exit_button.select()
    elif keys[pygame.K_DOWN]:
        if exit_button.selected:
            start_button.select()
            exit_button.unselect()
        elif start_button.selected:
            start_button.unselect()
            exit_button.select()

    draw_menu()




##################################
# Main loop
##################################
clock = pygame.time.Clock()
while run:
    clock.tick(27)  # change based on number of sprites

    # X button in top right corner of game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if user.x > screen_width // 2 + 3:
            user.x -= user.speed
        elif bg.x + user.speed < 0:
            bg.x += user.speed
        elif not bg.x + user.speed < 0 and user.x - user.speed > 0:
            user.x -= user.speed
        user.left = True
        user.right = False
        user.up = False
        user.down = False
        user.standing = False

    elif keys[pygame.K_d]:
        if user.x < screen_width // 2 - 3:
            user.x += user.speed
        elif bg.x - user.speed > screen_width - bg.width:
            bg.x -= user.speed
        elif not bg.x - user.speed > screen_width - bg.width and user.x + user.width + user.speed < screen_width:
            user.x += user.speed
        user.left = True
        user.right = False
        user.up = False
        user.down = False
        user.standing = False

    elif keys[pygame.K_s]:
        if user.y < screen_height // 2 - 3:
            user.y += user.speed
        elif bg.y - user.speed + bg.height > screen_height:
            bg.y -= user.speed
        elif not bg.y - user.speed + bg.height > screen_height and user.y + user.speed + user.height < screen_height:
            user.y += user.speed
        user.left = True
        user.right = False
        user.up = False
        user.down = False
        user.standing = False

    elif keys[pygame.K_w]:
        if user.y > screen_height // 2 + 3:
            user.y -= user.speed
        elif bg.y + user.speed < 0:
            bg.y += user.speed
        elif not bg.y + user.speed < 0 and user.y - user.speed > 0:
            user.y -= user.speed
        user.left = False
        user.right = False
        user.up = True
        user.down = False
        user.standing = False
    else:
        user.left = False
        user.right = False
        user.standing = True
        user.stepcount = 0




    # End of loop
    redraw()

#win.blit(pygame.image.load(Sprites/'EndGame_.png'),(0,0))
pygame.display.update()
pygame.time.delay(3000)
pygame.quit()
