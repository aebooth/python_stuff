import pygame

pygame.init()

HEIGHT = 500
WIDTH = 700
TITLE = "BOOF's Cool Animation"
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Do variable changing here

    #Do screen clearing here

    #Do drawing here


    pygame.display.flip()
    clock.tick()

pygame.quit()
