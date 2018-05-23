from consoleRPG import *
import random

me = Hero("me")
boss = BadGuy("MegaBad",hp=200,strength=50,defense=50,level=20)

def fight_bad_guy(hero,bad_guy):
    while hero.hp > 0 and bad_guy.hp > 0:
        print("Your stats:")
        print("HP: " + str(hero.hp))
        print("Magic: " + str(hero.magic))  
        print("What do you want to do?")
        print("1) attack")
        print("2) attack with aid of magic")
        print("3) defend")
        answer = input(">>> ")
        if answer == "1":
            damage = hero.attack(bad_guy)
            print("You attacked " + bad_guy.name + " and did " + str(damage) + " damage")
        elif answer == "2":
            if hero.magic > 0:
                damage = hero.attack(bad_guy,True)
                print("You attacked " + bad_guy.name + "with magic and did " + str(damage) + " damage")
            else:
                hero.magic = 0
                damage = hero.attack(bad_guy)
                print("You don't have any magic!")
                print("You attacked " + bad_guy.name + " and did " + str(damage) + " damage")
        elif answer == "3":
            print("Your defense is temporarily increased")
            hero.defense = hero.defense + 0.25 * hero.defense
        else:
            print("That's not an option!")

        damage = bad_guy.attack(me)
        print(bad_guy.name + " attacked and did "+ str(damage) + " damage to you.")

        if answer == 3:
            hero.defense = 0.8*hero.defense

        if bad_guy.hp <= 0:
            if bad_guy.level > hero.level:
                hero.gain_experience((bad_guy.level-hero.level)*100)
            elif bad_guy.level == hero.level:
                hero.gain_experience(50)
            else:
                hero.gain_experience(50/(hero.level - bad_guy.level))
            return True
        elif hero.hp <= 0:
            print(bad_guy.name + " killed you. You Lose.")
            return False
        elif hero.hp <= 0 and bad_guy.hp <= 0:
            print("Good news: You killed " + bad_guy.name + ". Bad News: You died too. Sucks to be you")
            return False

        
def adventure():
    adventuring = True
    while adventuring:
        print("What would you like to do today?")
        print("1) find a bad guy to fight")
        print("2) look for magical treasures")
        answer = input(">>> ")

        chance = random.random()

        if answer == "1":
            if chance <= 0.75:
                baddy = BadGuy("monster")
                return fight_bad_guy(me,baddy)
            else:
                print("You weren't able to find any bad guys")
                return True
        elif answer == "2":
            if chance <= 0.25:
                pass


print("""
    Kill teh monsters so dat you don't die from da BOSS!
   """)

alive = True
day = 1
BOSS_DOOMSDAY = 100
while alive and day < BOSS_DOOMSDAY:
    print("What would you like to do today?")
    print("1) Go out adventuring")
    print("2) Stay home an study the magic tome")
    print("3) Rest/Heal from wounds")
    print("4) Meditate to rejuvenate magic")
    print("5) Go face the evil bad guy now (and most likely die)")
    answer = input(">>> ")

    if answer == "1":
        alive = adventure()
    elif answer == "2":
        pass
    else:
        print("That's not an option")
    
