##def print_name(name):
##    print("My name is " + name)
##
##
##print_name("Boof")

def spire(size):
    for row in range(size):
        for col in range(size*3):
            print(end=" ")
        print("||")

def top(size):
    for row in range(size):
        for col in range((size - row - 1)*3):
            print(end=" ")
        print("__/", end = "")
        for col in range(row*3):
            print(":",end = "")
        print("||", end = "")
        for col in range(row*3):
            print(":",end = "")
        print("\__")

def divider(size):
    print("|", end="")
    for col in range(size*6):
        print("\"",end="")
    print("|")

def bottom(size):
    for row in range(size):
        for col in range(2*row):
            print(end=" ")
        print("\_",end="")
        for col in range(3*size - 1 - 2*row):
            print("/\\",end="")
        print("_/")
    
spire(4)
top(4)
divider(4)
bottom(4)
spire(4)
top(4)
divider(4)
