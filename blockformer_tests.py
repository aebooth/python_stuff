import unittest
import pygame
import blockformer_classes as bc

class TestSmartSpriteCollisions(unittest.TestCase):

    def setUp(self):
        self.left = 10
        self.top = 10
        self.width = 10
        self.height = 10
        self.main_sprite = bc.SmartSprite()
        self.main_sprite.rect = pygame.Rect(self.left,self.top,self.width,self.height)

    def test_get_direction_to(self):
        other = bc.SmartSprite()
        other.rect = pygame.Rect(0, 0, 1, 1)
        self.assertEqual(self.main_sprite.get_direction_to(self.other_sprite),bc.SmartSprite.NW,"NW broken")

    def test_get_relative_position(self):
        other = bc.SmartSprite()
        for row in range(6):
            for col in range(6):
                other.rect = pygame.Rect(0,0,col*5,row*5)
                print(self.main_sprite.get_relative_position(other))
                self.assertEqual(self.main_sprite.get_relative_position(other),(0,row*10+col),
                                 "died at width of " + str(other.rect.width) + " and a height of " + str(other.rect.height))