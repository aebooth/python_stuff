from enum import Enum,auto

class Input:
    def __init__(self,prompt):
        self.prompt = prompt + " "
        self.ready = False
        self.value = None

    def run(self):
        self.value = input(self.prompt)
        self.ready = True
            
class NumberType(Enum):
    FLOAT = auto()
    INTEGER = auto()

class NumberInput(Input):
    def __init__(self,prompt,num_type=NumberType.FLOAT):
        self.type = num_type
        Input.__init__(self,prompt + " ")

    def run(self):
        self.value = input(self.prompt)
        input_is_num = False
        while(not input_is_num):
            try:
                if self.type == NumberType.FLOAT:
                    self.value = float(self.value)
                else:
                    self.value = int(self.value)
                input_is_num = True
            except:
                if self.type == NumberType.FLOAT:
                    print("Your response could not be converted into a floating point number. Please try again!")
                else:
                    print("Your response could not be converted into a integer number. Please try again!")             
        self.ready = True

class FlagInput(Input):
    def __init__(self,prompt,flags):
        self.flags = []
        for flag in flags:
            self.flags.append(flag)
        Input.__init__(self,prompt + " ")

    def run(self):
        is_flag = False
        while not is_flag:
            response = input(self.prompt)
            if response in self.flags:
                is_flag = True
                self.value = response
                self.ready = True
            else:
                print("That is not a valid response--please try one of the following flags: ",end = "")
                for num in range(len(self.flags)-1):
                    print(self.flags[num],end = " ")
                print(self.flags[len(self.flags)-1])

                
