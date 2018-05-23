import pygame
from ctypes import windll, Structure, c_long, byref #windows only

class RECT(Structure):
    _fields_ = [
    ('left',    c_long),
    ('top',     c_long),
    ('right',   c_long),
    ('bottom',  c_long),
    ]
    def width(self):  return self.right  - self.left
    def height(self): return self.bottom - self.top


def onTop(window):
    SetWindowPos = windll.user32.SetWindowPos
    GetWindowRect = windll.user32.GetWindowRect
    rc = RECT()
    GetWindowRect(window, byref(rc))
    SetWindowPos(window, -1, rc.left, rc.top, 0, 0, 0x0001)

def main():
    pygame.init()
    
    HEIGHT = 70
    WIDTH = 500

    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Currently Pressed Key")

    clock = pygame.time.Clock()
    time = 0
    has_letter = False
    running = True
    while(running):
        onTop(pygame.display.get_wm_info()['window'])
        key = "NONE"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                continue

        #Do screen clearing here
        if time % 30 == 0:
            screen.fill(WHITE)
        #Do drawing here
        if key != "NONE":
            if has_letter:
                has_letter = False
                screen.fill(WHITE)
            has_letter = True
            screen.blit(pygame.font.SysFont("Tahoma",56).render(key,False,BLACK),(15,0))


        pygame.display.flip()
        time = time + 1
        clock.tick(60)

    pygame.quit()

main()

