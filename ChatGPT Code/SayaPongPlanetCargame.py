import pygame
import random

# Initialize Pygame and create the game window
pygame.init()
screen = pygame.display.set_mode((1920, 1080))

# Set the title and icon for the game window
pygame.display.set_caption("Saya's Pong-style Game with Cars and a Red Planet")
icon = pygame.image.load('planet.png')
pygame.display.set_icon(icon)

# Create the player car (Saya) and the red planet
player_car_image = pygame.image.load('player_car.png')
planet_image = pygame.image.load('planet.png')
player_car_rect = player_car_image.get_rect()
planet_rect = planet_image.get_rect()

# Set the initial position of the player car and the red planet
player_car_rect.x = 400
player_car_rect.y = 550
planet_rect.x = random.randint(0, 750)
planet_rect.y = random.randint(0, 550)

# Set the initial speed of the red planet
planet_speed = [2, 2]

# Set the initial color of the player car
player_car_color = (255, 0, 0)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the red planet
    planet_rect = planet_rect.move(planet_speed)
    if planet_rect.left < 0 or planet_rect.right > 800:
        planet_speed[0] = -planet_speed[0]
    if planet_rect.top < 0 or planet_rect.bottom > 600:
        planet_speed[1] = -planet_speed[1]

    # Check for collision between the red planet and the player car
    if player_car_rect.colliderect(planet_rect):
        player_car_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the player car and the red planet on the screen
    player_car = pygame.Surface((50, 100))
    player_car.fill(player_car_color)
    screen.blit(player_car, player_car_rect)
    screen.blit(planet_image, planet_rect)

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()