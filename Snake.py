import random
import pygame

pygame.init()

clock = pygame.time.Clock()

# WIDTH AND HIEGHT OF THE WINDOW CONSTANTS
WIDTH = 600
HIEGHT = 400
screen = pygame.display.set_mode((WIDTH, HIEGHT))

#Window title
pygame.display.set_caption("Snake Game")

#Game loop the game will run until the user closes the window
running = True

#Snake position and size
snake_x = 300
snake_y = 200
snake_width = 20
snake_height = 20

speed = 20

dx = speed
dy = 0

while running:

    snake_x += dx
    snake_y += dy
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -speed
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = speed
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -speed
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = speed

    #Fill the screen with black
    screen.fill((0,0,0))

    #drawing the snake
    pygame.draw.rect(
        screen, #Where to draw the rectangle
        (0,255,0), #Color of rectangle
        #Green
        (snake_x,snake_y,snake_width,snake_height) #position and size of rectangle
    )

    clock.tick(10) #FPS of the game

    #Show everything on the screen
    pygame.display.update()

#Close Pygame
pygame.quit()
