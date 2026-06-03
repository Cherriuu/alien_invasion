import sys
import pygame

def check_event(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # for every action the user takes (clicking the right arrow, hitting space, etc..)
            sys.exit() # system call to exit the game

        elif event.type == pygame.KEYDOWN: # detects any key pressed
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

        elif event.type == pygame.KEYUP: # detects when a key is released
            ship.moving_right = False

def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color) # redraw the screen during each iteration
    ship.blitme()
            
    pygame.display.flip() # updates the screen to the latest