import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen = pygame.display.set_mode((800, 600))

# Set caption and icon
pygame.display.set_caption("Two Player Pong")
icon = pygame.image.load('planet.png')
pygame.display.set_icon(icon)

# Define the paddles and ball
paddle1 = pygame.Rect(10, 250, 20, 100)
paddle2 = pygame.Rect(770, 250, 20, 100)
ball = pygame.Rect(390, 290, 20, 20)

# Define ball speed
ball_speed = [16, 16]

# Define colors
white = (255, 255, 255)

# Start the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle2.y -= 5
    if keys[pygame.K_DOWN]:
        paddle2.y += 5
    if keys[pygame.K_w]:
        paddle1.y -= 5
    if keys[pygame.K_s]:
        paddle1.y += 5

    # Ensure paddles stay on screen
    if paddle1.y < 0:
        paddle1.y = 0
    if paddle1.y > 500:
        paddle1.y = 500
    if paddle2.y < 0:
        paddle2.y = 0
    if paddle2.y > 500:
        paddle2.y = 500

    # Update ball position
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Check for ball collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] = -ball_speed[0]

    # Check for ball collision with walls
    if ball.y <= 0 or ball.y >= 580:
        ball_speed[1] = -ball_speed[1]
    if ball.x <= 0 or ball.x >= 780:
        ball_speed = [2, 2]
        ball.center = (390, 290)

    # Clear screen and draw objects
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, white, paddle1)
    pygame.draw.rect(screen, white, paddle2)
    pygame.draw.rect(screen, white, ball)
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()