import pygame as pg

# Init Pygame
pg.init()

# Display Surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Feed the dragon!")

# Game speed
FPS = 60
clock = pg.time.Clock()

# Load game values
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 5
COIN_STARTING_VELOCITY = 5
COIN_ACCELERATION = 0.5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

# Set Colors
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Set fonts
font = pg.font.Font("./assets/AttackGraffiti.ttf", 32)

# Set text
score_text = font.render("Score: " + str(score), True, GREEN, DARK_GREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = font.render("Feed the dragon", True, GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH // 2
title_rect.y = 10

lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARK_GREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH, 0)

game_over_text = font.render("Game Over", True, GREEN, DARK_GREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT, 2)


continue_text = font.render("Press any key to play again", True, GREEN, DARK_GREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 32)

# Load character images
dragon_image = pg.image.load("./assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25, 25)

coin_image = pg.image.load("./assets/coin.png")
coin_rect = coin_image.get_rect()
coin_rect.topright = (25, 25)

# Load sound effects
coin_sound = pg.mixer.Sound("./assets/coin_sound.wav")
miss_sound = pg.mixer.Sound("./assets/miss_sound.wav")
miss_sound.set_volume(1)
pg.mixer.music.load("./assets/ftd_background_music.wav")

# Set images

# Main loop game
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Display text items
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(score_text, score_rect)

    # Display Characters
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)

    # Update display
    pg.display.update()

    # Tick the clock
    clock.tick(FPS)
# End Game
pg.quit()
