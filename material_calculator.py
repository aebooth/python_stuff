from checked_input import *

def get_stock_lengths():
    stock_lengths = []

    keep_going_prompt = FlagInput("Would you like to add another piece of stock?",["y","n"])
    what_stock_length_prompt = NumberInput("What is the length of your stock in inches?")
    is_this_right_prompt = FlagInput("Is this right?",["y","n"])
    
    taking_input = True
    while taking_input:
        what_stock_length_prompt.run()
        stock_lengths.append(what_stock_length_prompt.value)
        keep_going_prompt.run()
        if keep_going_prompt.value == "n":
            print("So the lengths you want to use are: " + str(stock_lengths))
            is_this_right_prompt.run()
            if is_this_right_prompt.value == "y":
                print("Great!")
                return stock_lengths
            else:
                print("Oh no! Let's start over...")
                del stock_lengths[:]

get_stock_lengths()
