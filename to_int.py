class To_int_ask:
    def __init__(self):
        pass
        



    def func_(self):
        try:
            self.a = int(input('>   '))
            return self.a
        except ValueError:
            print('''Maybe you entered some str symbol's, try with out it''')
            ret = self.func_()
            return ret


            

    