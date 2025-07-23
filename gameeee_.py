import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BALL_SIZE = 20
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Create the paddle
paddle = pygame.Rect(0, SCREEN_HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create a list to store falling balls
balls = []

# Set up a clock for controlling the frame rate
clock = pygame.time.Clock()

# Game variables
score = 0
level = 1
lives = 3

# Create fonts for displaying text
font = pygame.font.Font(None, 36)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddle with the mouse
    mouse_x = pygame.mouse.get_pos()[0]
    paddle.centerx = mouse_x

    # Add new balls
    if random.random() < 0.02 + (level - 1) * 0.005:
        ball = pygame.Rect(random.randint(0, SCREEN_WIDTH - BALL_SIZE), 0, BALL_SIZE, BALL_SIZE)
        balls.append(ball)

    # Move the balls
    for ball in balls:
        ball.move_ip(0, 5)

    # Remove balls that are out of the screen
    balls = [ball for ball in balls if ball.y < SCREEN_HEIGHT]

    # Check for collisions
    for ball in balls:
        if paddle.colliderect(ball):
            balls.remove(ball)
            score += 1

    # Check for game over
    if lives <= 0:
        game_over_text = font.render("Game Over", True, BLUE)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
        pygame.display.flip()
        pygame.time.delay(2000)  # Display game over message for 2 seconds
        pygame.quit()
        sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the paddle
    pygame.draw.rect(screen, BLUE, paddle)

    # Draw the balls
    for ball in balls:
        pygame.draw.ellipse(screen, BLUE, ball)

    # Draw score and lives
    score_text = font.render(f"Score: {score}", True, BLUE)
    level_text = font.render(f"Level: {level}", True, BLUE)
    lives_text = font.render(f"Lives: {lives}", True, BLUE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (SCREEN_WIDTH - 120, 10))
    screen.blit(lives_text, (10, SCREEN_HEIGHT - 40))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)

    # Check for level up
    if score >= level * 10:
        level += 1

    # Check for losing a life
    if len(balls) > 0 and balls[-1].y >= SCREEN_HEIGHT:
        lives -= 1
