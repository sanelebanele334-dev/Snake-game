import random
import pygame

pygame.init()

width = 600
height = 600

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake game")

snake = [[200,300]]
snake_size = 20

speed = 20 

dx = speed
dy = 0

food_x = random.randrange(0,width,snake_size)
food_y = random.randrange(0,height,snake_size)

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dx = speed
                dy = 0
            if event.key == pygame.K_LEFT:
                dx = -speed
                dy = 0
            if event.key == pygame.K_UP:
                dx = 0
                dy = -speed
            if event.key == pygame.K_DOWN:
                dx = 0
                dy = speed

    head_x = snake[0][0]
    head_y = snake[0][1]

    new_head = [head_x + dx,head_y + dy]

    snake.insert(0,new_head)

    if food_x == snake[0][0] or food_y == snake[0][1]:
        food_x = random.randrange(0,width,snake_size)
        food_y = random.randrange(0,height,snake_size)
    else:
        snake.pop()

    screen.fill((0,0,0))

    for segment in snake:
        pygame.draw.rect(screen,(0,255,0),(segment[0],segment[1],snake_size,snake_size))

    pygame.draw.rect(screen,(255,0,0),(food_x,food_y,snake_size,snake_size))

    pygame.display.update()

    clock.tick(10)

pygame.quit()

