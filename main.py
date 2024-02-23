import pygame as pg

# Init Pygame
pg.init()

# Display Surface

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Feed the dragon!")

# Game speed
FPS = 60
clock = pg.time.Clock()

# Load character images

dragon_image = pg.image.load("./assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25, 25)

# Load sound effects

coin_image = pg.image.load("./assets/coin.png")
coin_rect = coin_image.get_rect()
coin_rect.topright = (25, 25)

# Main loop game
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)

    # Update display
    pg.display.update()

    # Tick the clock
    clock.tick(FPS)
# End Game
pg.quit()
