import pygame
import random

pygame.init()

HEIGHT = 500
WIDTH = 500
TITLE = "BOOF's Cool Animation"
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

#Initialize changing variables
x = 0
y = 0
dx = 2
dy = 3
going_left = False
going_up = False

bouncing = False

frame_ndx = 0
color_ndx = 0
shape_ndx = 0

height = 50
width = 50

colors = []
colors.append((255,0,0))
colors.append((255,165,0))
colors.append((255,255,0))
colors.append((0,255,0))
colors.append((0,255,255))
colors.append((0,165,255))
colors.append((0,0,255))

running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Do variable changing here
    frame_ndx = frame_ndx + 1

    if frame_ndx % 10 == 0:
        color_ndx = (color_ndx + 1) % len(colors)

    if x > WIDTH-width:
        going_left = True
        bouncing = True
    elif x < 0:
        going_left = False
        bouncing = True
    if y > HEIGHT-height:
        going_up = True
        bouncing = True
    elif y < 0:
        going_up = False
        bouncing = True

    if going_left:
        x = x - dx
    else:
        x = x + dx

    if going_up:
        y = y - dy
    else:
        y = y + dy

    if bouncing:
        shape_ndx = (shape_ndx + 1) % 3
        bouncing = False

#Do screen clearing here
    screen.fill((255,255,255))        
#Do drawing here
    if shape_ndx == 0:
        pygame.draw.rect(screen,colors[color_ndx],(x,y,width,height))
    elif shape_ndx == 1:
        pygame.draw.circle(screen,colors[color_ndx],(x,y),int(width/2))
    elif shape_ndx == 2:
        pygame.draw.polygon(screen,colors[color_ndx],[(x,y+height),(x+int(width/2),y),(x+width,y+height)])


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
