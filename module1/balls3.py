import random

import pygame


# Define some colors
BACKGROUND_COLOR = (255, 255, 255)
BALL_COLOR = (0, 0, 0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


class Ball:
    def __init__(self, x, y, radius, color, dx, dy):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = dx
        self.dy = dy


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Balls3")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    balls = []
    for i in range(1, 5):
        balls.append(Ball(100*i, 100*i, random.randint(15, 45), (random.randint(0, 255), random.randint(0, 255),
                                                                 random.randint(0, 255)),
                          random.randint(-3, 3), random.randint(-3, 3)))

    # Loop until the user clicks the close button or ESC.
    done = False
    while not done:
        # Limit number of frames per second
        clock.tick(60)

        # Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                # elif event.key == pygame.K_DOWN:
                #     dy
                # elif event.key == pygame.K_UP:
                #     dy
                # elif event.key == pygame.K_SPACE:
                #     dy = 0
                #     dx = 0
                # elif event.key == pygame.K_LEFT:
                #     dx
                # elif event.key == pygame.K_RIGHT:
                #     dx
                
        for ball in balls:
            min_y = ball.radius
            max_y = SCREEN_HEIGHT - ball.radius
            ball.y = constrain(min_y, ball.y + ball.dy, max_y)
            min_x = ball.radius
            max_x = SCREEN_WIDTH - ball.radius
            ball.x = constrain(min_x, ball.x + ball.dx, max_x)
        # Draw everything
        screen.fill(BACKGROUND_COLOR)

        for ball in balls:
            pygame.draw.circle(screen, ball.color,
                               (ball.x, ball.y), ball.radius)

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
