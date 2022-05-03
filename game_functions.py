import pygame
import sys
from alien import Alien
from bullets import Bullets

def check_events(settings, screen, ship, bullets):
    """checks for key/ mouse events and responds"""
    # loop to check keypress events
    for event in pygame.event.get():
        # if escape key is pressed we end game
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            if event.key == pygame.K_UP:
                ship.moving_up = True
            if event.key == pygame.K_DOWN:
                ship.moving_down = True
            if event.key == pygame.K_SPACE:
                if len(bullets) < settings.bullet_limit:
                    new_bullet = Bullets(settings, screen, ship)
                    bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            if event.key == pygame.K_UP:
                ship.moving_up = False
            if event.key == pygame.K_DOWN:
                ship.moving_down = False


def update_screen(settings,screen,ship, aliens, bullets, play_button):
    # color screen with background color
    screen.fill(settings.bg_color)
    if not settings.game_active:
        play_button.draw_button()
    limit_bullets(bullets)
    for bullet in bullets.sprites():
        bullet.draw_bullets()
        bullet.update()


    # draw ship on screen
    ship.blitme()
    ship.update()
    # draw fleet of aliens
    aliens.update()

    aliens.draw(screen)
    # update_fleet(settings, screen, aliens)
    # updating the display
    check_collision(bullets,aliens)
    pygame.display.flip()

def create_fleet(settings, screen, ship, aliens):
    """create a fleet of aliens"""
    alien = Alien(settings, screen)
    number_of_aliens = get_number_of_aliens(settings, alien.rect.width)
    number_of_rows = get_number_rows(settings, alien.rect.height, ship.rect.height)

    for row_number in range(number_of_rows):
        for alien_number in range(number_of_aliens):
            create_alien(settings, screen, aliens, alien_number, row_number)



def get_number_of_aliens(settings, alien_width):
    """Determine the number of aliens that fit in a row """
    available_space_x = settings.screen_width - 2 * alien_width
    number_of_aliens = int(available_space_x/(2*alien_width))
    return number_of_aliens

def get_number_rows(settings, alien_height, ship_height):
    available_space_y = settings.screen_height - 3 * alien_height - ship_height
    number_of_rows = int(available_space_y/(2*alien_height))
    return number_of_rows


def create_alien(settings, screen, aliens, alien_number, row_number):
    """create an alien and place it on a row"""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = 2 * alien_width * alien_number
    alien.rect.x = alien.x

    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def update_fleet(settings, screen, aliens):
    for alien in aliens:
        alien = Alien(settings, screen)
        if alien.check_wall:
            alien.direction *= -1


def check_collision(bullets, aliens):
    pygame.sprite.groupcollide(bullets, aliens, True, True)

def limit_bullets(bullets):
    for bullet in bullets:
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)