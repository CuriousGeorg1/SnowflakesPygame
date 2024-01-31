import pygame
import random

black = 0, 0, 0
window_x = 700
window_y = 600
fps = pygame.time.Clock()

lumihiutale1 = pygame.image.load("lumihiutale1.png")
lumihiutale2 = pygame.image.load("lumihiutale2.png")
lumihiutale3 = pygame.image.load("lumihiutale3.png")

'''Snowflake positions, speed and sizes. Nested dictionary with list for position on x axis (y is always same)
, randomized speed (int), randomized size(int) and appointed lumihiutale1-3.png. keywords for later use: position, speed, size and image'''
lumihiutaleet = {
    1: {'position': [random.randint(0, window_x), 2], 'speed': random.randint(1, 15), 'size': random.randint(40,100), 'image': lumihiutale1},
    2: {'position': [random.randint(0, window_x), 2], 'speed': random.randint(1, 15), 'size': random.randint(40,100), 'image': lumihiutale2},
    3: {'position': [random.randint(0, window_x), 2], 'speed': random.randint(1, 15), 'size': random.randint(40,100), 'image': lumihiutale3},
    4: {'position': [random.randint(0, window_x), 2], 'speed': random.randint(1, 15), 'size': random.randint(40,100), 'image': lumihiutale1},
    5: {'position': [random.randint(0, window_x), 2], 'speed': random.randint(1, 15), 'size': random.randint(40,100), 'image': lumihiutale2},
    6: {'position': [random.randint(0, window_x), 2], 'speed': random.randint(1, 15), 'size': random.randint(40,100), 'image': lumihiutale3},
    7: {'position': [random.randint(0, window_x), 2], 'speed': random.randint(1, 15), 'size': random.randint(40,100), 'image': lumihiutale1},
    8: {'position': [random.randint(0, window_x), 2], 'speed': random.randint(1, 15), 'size': random.randint(40,100), 'image': lumihiutale2},
    9: {'position': [random.randint(0, window_x), 2], 'speed': random.randint(1, 15), 'size': random.randint(40,100), 'image': lumihiutale3},
    10: {'position': [random.randint(0, window_x), 2], 'speed': random.randint(1, 15), 'size': random.randint(40,100), 'image': lumihiutale1},
}

def initialise():
    '''initialise screen and return game window'''
    pygame.init()
    game_window = pygame.display.set_mode((window_x, window_y))
    return game_window

screen = initialise()
screen.fill(black)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Make it rain
    for flake_id, flake in lumihiutaleet.items():
        flake['position'][1] += flake['speed']

        # Reset snowflake (and randomize again)
        if flake['position'][1] > window_y:
            flake['position'][1] = 0
            flake['position'][0] = random.randint(0, window_x)

    # Draw the screen
    screen.fill(black)
    for flake_id, flake in lumihiutaleet.items():
        # Resize the snowflake image based on the 'size' key
        resized_snowflake = pygame.transform.scale(flake['image'], (flake['size'], flake['size']))
        screen.blit(resized_snowflake, flake['position'])

    pygame.display.flip()
    fps.tick(60)
