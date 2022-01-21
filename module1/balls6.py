import random

import pygame
from pygame.constants import *

# Define some colors
BACKGROUND_COLOR = (255, 255, 255)
BALL_COLOR = (0, 0, 0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        Ball.randomize(self)

    def randomize(self):
        self.dx = random.randint(-3, 3)
        self.dy = random.randint(-3, 3)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


class Player:
    def __init__(self):
        self.x = 20
        self.y = 20
        self.radius = 15


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Balls5")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    balls = []
    for i in range(1, 5):
        balls.append(Ball(100 * i, 100 * i, random.randint(25, 45)))

    player = Player()


    # Loop until the user clicks the close button or ESC.
    done = False
    while not done:
        # Limit number of frames per second
        clock.tick(60)

        up = pygame.key.get_pressed()[K_UP]
        down = pygame.key.get_pressed()[K_DOWN]
        left = pygame.key.get_pressed()[K_LEFT]
        right = pygame.key.get_pressed()[K_RIGHT]
        escape = pygame.key.get_pressed()[K_ESCAPE]
        color_randomizer = pygame.key.get_pressed()[K_r]
        new_ball = pygame.key.get_pressed()[K_a]

        if escape:
            done = True
        if color_randomizer:
            balls.append(Ball(SCREEN_HEIGHT/2, SCREEN_WIDTH/2, random.randint(45, 55)))
        if new_ball:
            balls.append(Ball(SCREEN_HEIGHT/2, SCREEN_WIDTH/2, random.randint(45, 55)))
        if up:
            player.y -= 1
        if down:
            player.y += 1
        if left:
            player.x -= 1
        if right:
            player.x += 1

        # Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        for ball in balls:
            min_y = ball.radius
            max_y = SCREEN_HEIGHT - ball.radius
            ball.y = constrain(min_y, ball.y + ball.dy, max_y)
            min_x = ball.radius
            max_x = SCREEN_WIDTH - ball.radius
            ball.x = constrain(min_x, ball.x + ball.dx, max_x)
            if ball.x in (min_x, max_x):
                ball.dx = -ball.dx
            if ball.y in (min_y, max_y):
                ball.dy = -ball.dy

        min_p_y = player.radius
        max_p_y = SCREEN_HEIGHT - player.radius
        player.y = constrain(min_p_y, player.y, max_p_y)
        min_p_x = player.radius
        max_p_x = SCREEN_WIDTH - player.radius
        player.x = constrain(min_p_x, player.x, max_p_x)

        # Draw everything
        screen.fill(BACKGROUND_COLOR)

        for ball in balls:
            pygame.draw.circle(screen, ball.color,
                               (ball.x, ball.y), ball.radius)

        pygame.draw.circle(screen, (23, 45, 55), (player.x, player.y), player.radius)

        # Update the screen
        pygame.display.flip()

    # Close everything down
    pygame.quit()


def constrain(small, value, big):
    """Return a new value which isn't smaller than small or larger than big"""
    # TODO: Should use "small" as well.
    maxvalue = max(small, value)
    return min(maxvalue, big)


if __name__ == "__main__":
    main()
