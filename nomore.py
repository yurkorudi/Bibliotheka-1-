
class No_more:
    def __init__(self):
        self.special_list = ['age', 'date', 'none']

    def chek(self, min, max, special):
        self.min = min
        self.max = max
        self.special = special
        if self.special == self.special_list[0]:
            self.age()

        elif self.special == self.special_list[1]:
            self.date()


    def age(self):
        self.variable = None
        print('Enter number from 0 - 125:')
        try:
            self.variable = int(input('>   '))

            if self.variable > 0 and self.variable <= 125:
                return self.variable

            else:
                print("It's a false age. Please try to enter real age.")
                self.age()

        except ValueError:
            print("It's not an age.Pleasy try again with real age.")
            self.age()


    def date(self):
        pass

### доробити ####################################################################################################################################################################################





