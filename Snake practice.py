import random
import pygame

pygame.init()

width = 600
height = 400

screen = pygame.display.set_mode((width, height))
#pygame.display is the module that allows us to control the window and its properties. set_mode() is a function that sets the size of the window. It takes a tuple as an argument, which contains the width and height of the window.

pygame.display.set_caption("Snake Game")
#set_caption() is a function that sets the title of the window. It takes a string as an argument, which is the title of the window.


snake = [[300, 200]]
snake_size = 20
#The snake's position is represented by the variables snake_x and snake_y, which are initialized to 300 and 200 respectively. The snake's size is represented by the variable snake_size, which is initialized to 20.

speed = 20
#This stores how many pixels the snake will move each time.

dx = speed
dy = 0

clock = pygame.time.Clock()
#pygame.time is pygames time module. Clock() is a class that allows us to control the frame rate of the game. It has a method called tick() that takes an integer as an argument, which is the number of frames per second (FPS) that we want the game to run at.

running = True
#This variable decides whether the should continue running or not.

food_x = random.randrange(0, width, snake_size)
food_y = random.randrange(0, height, snake_size)
#Generate a random position for the food.

score = 0

#=====================================================Handle events========================================================
while running:

    #This is called a game loop. It is a loop that runs continuously until the user closes the window. It is used to update the game state and redraw the screen.
    for event in pygame.event.get():
        #pygame is the library, event is the module, and get() is a function that returns a list of all the events that have occurred since the last time it was called. An event is an action that occurs in the game, such as a key press or a mouse click.
        if event.type == pygame.QUIT:
            #pygame.QUIT is an event that occurs when the user closes the window. It is used to exit the game loop and close the window. Type is an attribute of the event object that stores the type of event that occurred.
            running = False
        if event.type ==pygame.KEYDOWN:
            #pygame.KEYDOWN is an event that occurs when the user presses a key on the keyboard. It is used to change the direction of the snake. Keydown is an attribute of the event object that stores the key that was pressed.
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


#=====================================================Update the snake's position========================================================

    #Get the current head
    head_x = snake[0][0]
    head_y = snake[0][1]

    #Calculate the new head position based on the current direction
    new_head = [head_x + dx, head_y + dy]

    #Add the new head to the front of the snake
    snake.insert(0,new_head)

    if snake[0][0] == food_x and snake[0][1] == food_y:
        food_x = random.randrange(0, width, snake_size)
        food_y = random.randrange(0, height, snake_size)
        score += 1
        #If the snake's position is the same as the food's position, generate a new position for the food and increment the score by 1. 
    else:
        snake.pop()
        #If the snake's position is not the same as the food's position, remove the last segment of the snake to keep its length constant. This is done by calling the pop() method on the snake list, which removes the last element from the list.


#=====================================================Draw the snake and food========================================================
    screen.fill((0,0,0))
    #Fill the screen with black.

    for segment in snake:
        pygame.draw.rect(screen,(0,255,0),(segment[0],segment[1],snake_size,snake_size))

    pygame.draw.rect(screen, (255,0,0), (food_x, food_y, snake_size, snake_size))
    #pygame.draw is a module rect() draw a rectengle on the screen. It takes four arguments: the surface to draw on, the color of the rectangle, and a tuple that contains the position and size of the rectangle. The position is represented by the variables snake_x and snake_y, which are updated each time the game loop runs. The size is represented by the variable snake_size, which is constant.

    font = pygame.font.SysFont(None, 36)
    text = font.render(f"score: {score}",True,(0,0,255))
    screen.blit(text, (10, 10))
    #Set the font style (font.SysFont()) and creates that text (render) then puts it on screen (blit)


    pygame.display.update()
    #pygame.display is the module that allows us to control the window and its properties. update() is a function that updates the contents of the window. It is called after all the drawing functions have been called, so that the changes are visible on the screen.

    clock.tick(10)
    #This tells the game to run at 10 frames per second.

#======================================================Wall collision=======================================================================
    if head_x >= width or head_x < 0 or head_y >= height or head_y < 0:
        running = False

#======================================================Self collision=======================================================================
    for snakepiece in snake[1:]:
        if snakepiece == snake[0]:
            running = False

pygame.quit()
#Should be called when the game is over. It is used to close the window and exit the game loop.


            
