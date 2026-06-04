import pygame
import game_functions as gf
from pygame.sprite import Group

from settings import Settings
from cat import Cat

from mouse import Mouse

def run_game():
    pygame.init() # creates the blank slate and initiates needed settings
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # sets the screen size, this is called a surface
    pygame.display.set_caption("Cat Invasion")

    cat = Cat(screen, ai_settings)
    bullets = Group()
    mouses = Group()

    gf.create_fleet(ai_settings, screen, mouses)

    while True: # surface is redrawn through every iteration of this
        # this is called an event loop that will perform a task based off the kind of event that has occured

        gf.check_event(cat, ai_settings, screen, bullets)

        cat.update()

        gf.update_bullets(bullets)

        gf.update_screen(ai_settings, screen, cat, mouses, bullets)


run_game()