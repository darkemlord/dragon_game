import pygame as pg
import random

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
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)


continue_text = font.render("Press any key to play again", True, GREEN, DARK_GREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 32)

# Load character images
dragon_image = pg.image.load("./assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.left = 32
dragon_rect.centery = WINDOW_HEIGHT // 2

coin_image = pg.image.load("./assets/coin.png")
coin_rect = coin_image.get_rect()
coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

# Load sound effects
coin_sound = pg.mixer.Sound("./assets/coin_sound.wav")
miss_sound = pg.mixer.Sound("./assets/miss_sound.wav")
miss_sound.set_volume(1)
pg.mixer.music.load("./assets/ftd_background_music.wav")

# Main loop game
pg.mixer.music.play(-1, 0.0)
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Check to see if the user wants to move
    keys = pg.key.get_pressed()
    if keys[pg.K_UP] and dragon_rect.top > 64:
        dragon_rect.y -= PLAYER_VELOCITY
    if keys[pg.K_DOWN] and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += PLAYER_VELOCITY

    # Move the coin
    if coin_rect.x < 0:
        # player miss the coin
        player_lives -= 1
        miss_sound.play()
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
    else:
        # Move coin
        coin_rect.x -= coin_velocity

    # Check for collision
    if dragon_rect.colliderect(coin_rect):
        score += 1
        coin_sound.play()
        coin_velocity += COIN_ACCELERATION
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

    # Update HUD
    score_text = font.render("Score: " + str(score), True, GREEN, DARK_GREEN)
    lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARK_GREEN)

    # Check for game over
    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pg.display.update()

        # Pause the game until player presses a key, the reset game
        pg.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pg.event.get():
                # The player wants to play again
                if event.type == pg.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    dragon_rect.y = WINDOW_HEIGHT // 2
                    coin_velocity = COIN_STARTING_VELOCITY
                    pg.mixer.music.play(-1, 0.0)
                    is_paused = False
                # The player wants to quit
                if event.type == pg.QUIT:
                    is_paused = False
                    running = False
    # Fill surface and remove duplicated images
    display_surface.fill(BLACK)

    # Display text items
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(score_text, score_rect)
    pg.draw.line(display_surface, WHITE, (0, 64), (WINDOW_WIDTH, 64), 2)

    # Display Characters
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)

    # Update display
    pg.display.update()

    # Tick the clock
    clock.tick(FPS)
# End Game
pg.quit()
