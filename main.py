import pygame as pg

# Init Pygame
pg.init()

# Display Surface

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Main loop game
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

# End Game
pg.quit()
