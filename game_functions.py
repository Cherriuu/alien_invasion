import sys
import pygame
from bullet import Bullet
from mouse import Mouse

def check_event(cat, ai_settings, screen, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # for every action the user takes (clicking the right arrow, hitting space, etc..)
            sys.exit() # system call to exit the game
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, cat, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, cat)

def check_keydown_events(event, cat, ai_settings, screen, bullets): # when a user presses a key
    if event.key == pygame.K_RIGHT:
        cat.moving_right = True
    elif event.key == pygame.K_LEFT:
        cat.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(cat, ai_settings, screen, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, cat): # when a user releases a key
    if event.key == pygame.K_RIGHT:
        cat.moving_right = False
    elif event.key == pygame.K_LEFT:
        cat.moving_left = False

def update_screen(ai_settings, screen, cat, mouses, bullets):
    screen.fill(ai_settings.bg_color) # redraw the screen during each iteration
    cat.blitme()
    mouses.draw(screen)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    pygame.display.flip() # updates the screen to the latest

def update_bullets(bullets):
    bullets.update()

    for bullet in bullets.copy(): # delete bullets once they go off screen to reduce memory usage
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(cat, ai_settings, screen, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, cat)
            bullets.add(new_bullet)

def create_fleet(ai_settings, screen, mouses):
    mouse = Mouse(ai_settings, screen)
    mouse_width = mouse.rect.width
    available_space_x = ai_settings.screen_width - 2 * mouse_width
    number_mouse_x = int(available_space_x / (1.5 * mouse_width))

    for mouse_number in range(number_mouse_x):
        mouse = Mouse(ai_settings, screen)
        mouse.x = mouse_width + 1.5 * mouse_width * mouse_number
        mouse.rect.x = mouse.x
        mouses.add(mouse)
