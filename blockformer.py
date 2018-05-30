import pygame
import blockformer_core as bc
import blockformer_setup as bs

pygame.init()

window = bc.Window(1400,500,300,300,60,"Blockformer")

#initialize variables

#Landscape(self,color,x,y,width=20,height=20)
landscape = bc.Landscape(window,(0,255,0),0,0,window.width,100)
window.background.add(landscape.drawable_sprite)

sprite = bc.SmartSprite(window,0,100,20,20,10)
window.sprites.add(sprite.drawable_sprite)

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
