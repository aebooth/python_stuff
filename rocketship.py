
def top(size):
    for row in range(size - 2):
        for i in range(size - 2 - row):
            print(" ", end="")
        for i in range(row + 1):
            print("/", end="")
        print("**", end="")
        for i in range(row + 1):
            print("\\", end="")
        print()

top(6)
