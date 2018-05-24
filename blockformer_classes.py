import pygame

#HELLO EVERYONE

class Window:
    def __init__(self,width=700,height=500,screen_width=700,screen_height=500,frames_per_second=60,title="my game"):
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption(title)
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height= screen_height
        self.left_bound = 0
        self.lower_bound = 0
        self.clock = pygame.time.Clock()
        self.frames_per_second = frames_per_second
        self.landscape = {}
        self.background = pygame.sprite.Group()
        self.foreground = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()

    def get_screen_x(self,x):
        return x - self.left_bound

    def get_screen_y(self,y):
        return self.screen_height-(y-self.lower_bound)

    def advance_frame(self):
        pygame.display.flip()
        self.clock.tick(self.frames_per_second)

    def clear(self):
        self.screen.fill((255,255,255))

    def draw(self):
        self.sprites.draw(self.screen)

    def update(self,*args):
        self.sprites.update(args)

    def scroll(self,dx,dy):
        pass

class Landscape(pygame.sprite.Sprite):
    def __init__(self,Window,color,x,y,width=20,height=20):
        pygame.sprite.Sprite.__init__(self)
        self.window = Window
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        #Docs say we need image and rect in order to be visible and collide
        self.image = pygame.Surface([width,height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect().move(self.window.get_screen_x(x),self.window.get_screen_y(y)-self.height)

    def update(self,color):
        self.color = color
        self.image.fill(self.color)


class Platform(Landscape):
    BOTTOM = 0
    LEFT = 1
    TOP = 3
    RIGHT = 4

    def __init__(self, Window, color, x, y, width=20, height=20):
        Landscape.__init__(self, Window, color, x, y, width, height)

    def move(self,x,y):
        self.rect.move_ip(x,y)

    def get_collision_direction(self):
        pygame.sprite.spritecollideany(self,)
