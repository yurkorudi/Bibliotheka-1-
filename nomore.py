
class No_more:
    def __init__(self, max, min):
        self.max = max
        self.min = min 
        self.chek()





    def chek(self):    
        self.a = input("Enter: ")
        if type(self.a) == int:
            if self.a >= self.min and self.a <= self.max:
                pass
            else:
                print("Wrong answer. Try again")
                self.chek()
        else:
            print("Mistake answer. Try some int")
            self.chek()








### доробити ####################################################################################################################################################################################





