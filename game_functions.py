import sys
import pygame

def check_event(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # for every action the user takes (clicking the right arrow, hitting space, etc..)
            sys.exit() # system call to exit the game
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color) # redraw the screen during each iteration
    ship.blitme()
            
    pygame.display.flip() # updates the screen to the latest