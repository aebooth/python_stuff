import pygame

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
        self.background.draw(self.screen)
        self.platforms.draw(self.screen)
        self.sprites.draw(self.screen)
        self.foreground.draw(self.screen)

    def update(self,*args):
        self.sprites.update(args)

    def scroll(self,dx,dy):
        for sprite in self.background.sprites():
            sprite.rect.move(dx,dy)
        for sprite in self.background.sprites():
            sprite.rect.move(dx,dy)
        for sprite in self.background.sprites():
            sprite.rect.move(dx,dy)
        for sprite in self.background.sprites():
            sprite.rect.move(dx,dy)

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


    def __init__(self, Window, color, x, y, width=20, height=20):
        Landscape.__init__(self, Window, color, x, y, width, height)

    def move(self,x,y):
        self.rect.move_ip(x,y)

    def get_collision_direction(self):
        pygame.sprite.spritecollideany(self,)


class SmartSprite(pygame.sprite.Sprite):
    N = 0
    NE = 1
    E = 3
    SE = 4
    S = 5
    SW = 6
    W = 7
    NW = 8

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sides_in_collision = []

    def collide(self,others):
        collider_directions = []
        self.sides_in_collision.clear()
        collisions = pygame.sprite.spritecollide(self,others,False)
        for i in range(len(collisions)):
            collider_directions[i] = self.get_direction_to(others[i])
        return collider_directions

    """
    Returns a tuple with the following make-up (top left corner code , bottom right corner code)
    
           0     1     2     3
        -------------------------
    0   | 00  | 01  | 02 | 03  |
        ------=============------
    1   | 10  [ 11  | 12  ] 13  |
        -------------------------
    2   | 20  [ 21  | 22  ] 23  |
        ------=============------
    3   | 30  | 31  | 32  | 33  |
        -------------------------
    
    The codes produced by this method are based on the box above. Codes 11,12,21,22 are within the 
    actual rect of the sprite
   
    """

    def get_relative_position(self,other):
        x = -1
        y = -1

        if other.rect.left > self.rect.right:
            x = 3
        elif other.rect.left <= self.rect.right and other.rect.left > self.rect.centerx:
            x = 2
        elif other.rect.left <= self.rect.centerx and other.rect.left > self.rect.left:
            x = 1
        else:
            x = 0

        if other.rect.top > self.rect.bottom:
            y = 30
        elif other.rect.top <= self.rect.bottom and other.rect.top > self.rect.centery:
            y = 20
        elif other.rect.top <= self.rect.centery and other.rect.top > self.rect.top:
            y = 10
        else:
            y = 0

        tl = y+x

        x = -1
        y = -1

        if other.rect.right > self.rect.right:
            x = 3
        elif other.rect.right <= self.rect.right and other.rect.right > self.rect.centerx:
            x = 2
        elif other.rect.right <= self.rect.centerx and other.rect.right > self.rect.left:
            x = 1
        else:
            x = 0

        if other.rect.bottom > self.rect.bottom:
            y = 30
        elif other.rect.bottom <= self.rect.bottom and other.rect.bottom > self.rect.centery:
            y = 20
        elif other.rect.bottom <= self.rect.centery and other.rect.bottom > self.rect.top:
            y = 10
        else:
            y = 0

        br = y+x

        return (tl,br)

    def get_direction_to(self,other):
        (tl,br) = self.get_relative_position(other)
        if (tl / 10 <= 1 and tl % 10 <= 1) and (br / 10 <= 1 and br % 10 <= 1):
            return SmartSprite.NW
        elif (tl / 10 >= 2 and tl % 10 >= 2) and (br / 10 >= 2 and br % 10 >= 2):
            return SmartSprite.SE
        elif (tl / 10 >= 2 and tl % 10 <= 1) and (br / 10 >= 2 and br % 10 <= 1):
            return SmartSprite.SW
        elif (tl / 10 <= 1 and tl % 10 >= 2) and (br / 10 <= 1 and br % 10 >= 2):
            return SmartSprite.NE
        elif tl / 10 <= 1 and br / 10 <= 1:
            return SmartSprite.N
        elif tl / 10 >= 2 and br / 10 >= 2:
            return SmartSprite.S
        elif tl % 10 <= 1 and br % 10 <= 1:
            return SmartSprite.W
        elif tl % 10 >= 2 and br % 10 >= 2:
            return SmartSprite.E
        else:
            return -1
