import math
import random

class Character:
    def __init__(self,name,hp,magic,strength,defense,level):
        self.name = name
        self.hp = hp
        self.MAX_HP = hp
        self.magic = magic
        self.MAX_MAGIC = magic
        self.strength = strength
        self.defense = defense
        self.level = level

    def take_damage(self,attack_force):
        damage = attack_force - self.defense*self.level
        if damage <= 0:
            damage = 1
        elif damage >= self.hp:
            damage = self.hp
        self.hp = self.hp - damage
        return damage

    def attack(self,target,using_magic=False):
        attack = Attack(self,using_magic)
        return target.take_damage(attack.get_attack_force())

    def print_stats():
        print("Current Stats for " + self.name + ":")
        print("HP: " + str(self.hp) + " / " + str(self.MAX_HP))
        print("MAGIC: " + str(self.magic) + " / " + str(self.MAX_MAGIC))
        print("HP: " + str(self.hp) + " / " + str(self.MAX_HP))
        print("HP: " + str(self.hp) + " / " + str(self.MAX_HP))
        print("HP: " + str(self.level))

class Hero(Character):
    def __init__(self,name,hp=20,magic=10,defense=10,strength=10,level=1):
        Character.__init__(self,name,hp,magic,strength,defense,level)
        self.experience = 0

    def level_up(self):
        self.level = self.level + 1
        self.MAX_HP = self.MAX_HP*1.5
        self.strength = self.strength + random.randint(2,5)
        self.MAX_MAGIC = self.MAX_MAGIC + random.randint(2,5)
        self.defense = self.defense + random.randint(2,5)

    def gain_experience(self, amount):
        self.experience = self.experience + amount
        if self.experience >= math.floor(self.level*20*1.5**self.level):
            self.level_up()


class BadGuy(Character):
    def __init__(self,name,hp=20,magic=0,strength=5,defense=5,level=1):
        Character.__init__(self,name,hp,magic,strength,defense,level)


class Attack:
    def __init__(self,attacker,is_magic=False):
        self.attacker = attacker
        self.is_magic = is_magic
        self.chance = random.random()

    def get_attack_force(self):
        force = self.attacker.level * self.attacker.strength
        if self.is_magic:
            self.attacker.magic = self.attacker.magic - 1
            if self.chance >= 0.75:
                force = force*2
            elif self.chance >= 0.5:
                force = force*1.5
        return force
