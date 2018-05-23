import pygame
import blockformer_classes as bc

pygame.init()

window = bc.Window(1400,500,300,300,60,"Blockformer")

#initialize variables

#Landscape(self,color,x,y,width=20,height=20)
landscape = bc.Landscape(window,(0,255,0),0,0,window.width,100)
window.add_sprite(landscape)
running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Do variable changing here

    #Do screen clearing here
    window.clear()
    
    #Do drawing here
    window.draw()

    #Finish up frame
    window.advance_frame()

pygame.quit()
