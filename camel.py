import random

camel_health = 10
player_distance_travelled = 0
bad_guy_distance_travelled = -30



print(""""Welcome to the Camel Game! You are an intrepid explorer
    in the great Mobi desert area. You were captured by a tribe of cannibals,
    but you escaped! You are now running from them with the help of
    your trusty camel. You must use your energy wisely to make it 100 miles across
    the desert or your ARE DOOMED!
    Good Luck! ;)""")

running = True
while running:
    print("What would you like to do?")
    print("a) travel normal speed")
    print("b) travel at ludicrous speed")
    print("c) rest")
    print("d) quit and get eaten")

    answer = input(">>> ").lower()

    #pertains to USER variables
    if answer == "a":
        pass
    elif answer == "b":
        pass
    elif answer == "c":
        pass
    elif answer == "d":
        print("Thanks for playing!")
        break
    else:
        print("That's not a valid choice!")
        continue

    bad_guy_distance_travelled += random.randint(8,12)

    print("You have travelled " + str(player_distance_travelled) + " miles")
    print("The cannibals are " + str(player_distance_travelled - bad_guy_distance_travelled) + " miles behind you")
    print("Your camel has " + str(camel_health) + " health")
