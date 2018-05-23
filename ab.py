def optionB(a_count,b_count):
    done = False
    while not done:
        print("C or D?")
        banswer = input(">>> ")
        if banswer == "C":
            a_count = a_count + 1
        elif banswer == "D":
            b_count = b_count + 1
        else:
            return

a_count = 0
b_count = 0
done = False
while not done:
    print("A or B?")
    answer = input(">>> ")

    if answer == "A":
        a_count = a_count + 1
    elif answer == "B":
        b_count = b_count + 1
        optionB(a_count,b_count)
    else:
        print("I didn't get that--what?")

    print("a_count = " + str(a_count) + ", b_count = " + str(b_count))



                
