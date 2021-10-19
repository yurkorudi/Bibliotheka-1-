import json



class User:
    id = ''
    first_name = ''
    last_name = ''
    age = ''
    adress = ''
    number = ''
    books = ''

    def __init__(self, id, first_name, last_name, age, adress, number, books):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.adress = adress
        self.number = number
        self.books = books


    # def create_line(self):
    #     book = ''
    #     for i in self.books:
    #         book = book + str(i) + ' '

    #     return str(self.id) + '|' + self.first_name + '|' + self.last_name + '|' + str(self.age) + '|' + str(self.adress) + '|' + str(self.number) + '|' + book


    def print_user(self):
        print(str(self.id) + '    ' + self.first_name + ' ' + self.last_name + ' ' + str(self.age) + ' ' + str(self.adress) + '|' + str(self.number))











class Users:

    users_list = []

    def __init__(self, book, ask):
        self.load_from_file()
        self.book = book
        self.ask = ask



    
    def load_from_file(self):
        pass
        lines = []

        file = open('user.txt')
        data = json.load(file)  

        for obg in data:


            user = User(obg["id"], obg["first_name"], obg["last_name"], obg["age"],obg["adress"], obg["nomber"], obg["books"])
            self.users_list.append(user)


    def user_menu(self):
        print('##    Menu:   ##')
        print('   0: Add user')
        print('   1: Delete user')
        print('   2: Change user')
        print('   3: Print list user')
        print('   4: Print list user > book')
        print('   5: EXIT')

        try:
            self.menu_answer = int(input('>   '))
        except ValueError:
            print('''NO-NO-NO, it's not an answer!''')
            self.user_menu()


        if self.menu_answer <= 5 and self.menu_answer >= 0:

            if self.menu_answer == 0:
                self.add_user()
            
            if self.menu_answer == 1:
                self.del_user()

            if self.menu_answer == 2:
                self.change_user()

            if self.menu_answer == 3:
                self.print_user()
                self.user_menu()

            if self.menu_answer == 4:
                self.show_users_books()

            if self.menu_answer == 5:
                return
        
        else:
            print('''NO-NO-NO, it's not an answer!''')
            self.user_menu()





    def add_user(self):
        id = len(self.users_list) + 1
        list_to_exit = []

        first_name = str(input('Enter first name:  or to exit enter 0:  '))
        try:
            if int(first_name) == 0:
                self.user_menu()
        except ValueError:
            pass
        last_name = str(input('Enter last name:  '))
        print('Enter age:  ')
        age = self.ask.func_()
        adress = str(input('Enter adress:  '))
        print('Enter number:   ')
        number = self.ask.func_()
        books = str(input('Id of books (if not, press enter)'))

        if books == '/n':
            books = []

        if books != []:
            books = books.split(' ')


        
        
        

        user = User(id, first_name, last_name, age, adress, number, books)
        self.users_list.append(user)
        self.save_users()
        self.user_menu()




        

    def del_user(self):
        self.print_user()
        print('Enter number of element you want to delete> or to exit enter 0:  ')
        number = self.ask.func_()
        try:
            if int(number) == 0:
                return
        except ValueError:
            pass
        del self.users_list[number-1]
        self.save_users()
        self.user_menu()

    def change_user(self):
        pass



    def insert(self, s, index, value):
        return  s[:index] + value + s[index:]



    def print_user(self):

        self.line =  '------------------------------------------------------------------------------------'
        self.line = self.insert(self.line, 0, '+')
        self.line = self.insert(self.line, 15, '+')
        self.line = self.insert(self.line, 30, '+')
        self.line = self.insert(self.line, 45, '+')
        self.line = self.insert(self.line, 60, '+')
        self.line = self.insert(self.line, 75, '+')
        self.line = self.insert(self.line, 90, '+')
        print(self.line)


        self.line =  '                                                                                '
        self.line = self.insert(self.line, 0, '+')
        self.line = self.insert(self.line,1, 'id')
        self.line = self.insert(self.line, 15, '+')
        self.line = self.insert(self.line, 16, 'first name')
        self.line = self.insert(self.line, 30, '+')
        self.line = self.insert(self.line, 31, 'second name')
        self.line = self.insert(self.line, 45, '+')
        self.line = self.insert(self.line, 46, 'age')
        self.line = self.insert(self.line, 60, '+')
        self.line = self.insert(self.line, 61, 'adress')
        self.line = self.insert(self.line, 75, '+')
        self.line = self.insert(self.line, 76, 'number')
        self.line = self.insert(self.line, 90, '+')
        print(self.line)



        self.line =  '------------------------------------------------------------------------------------'
        self.line = self.insert(self.line, 0, '+')
        self.line = self.insert(self.line, 15, '+')
        self.line = self.insert(self.line, 30, '+')
        self.line = self.insert(self.line, 45, '+')
        self.line = self.insert(self.line, 60, '+')
        self.line = self.insert(self.line, 75, '+')
        self.line = self.insert(self.line, 90, '+')
        print(self.line)

        for user in self.users_list:

            self.line =  '                                                                                '
            self.line = self.insert(self.line, 0, '+')
            self.line = self.insert(self.line,1, (str(user.id)))
            self.line = self.insert(self.line, 15, '+')
            self.line = self.insert(self.line, 16, user.first_name)
            self.line = self.insert(self.line, 30, '+')
            self.line = self.insert(self.line, 31, user.last_name)
            self.line = self.insert(self.line, 45, '+')
            self.line = self.insert(self.line, 46, str(user.age))
            self.line = self.insert(self.line, 60, '+')
            self.line = self.insert(self.line, 61, str(user.adress))
            self.line = self.insert(self.line, 75, '+')
            self.line = self.insert(self.line, 76, str(user.number))
            self.line = self.insert(self.line, 90, '+')
            print(self.line)




        self.line =  '------------------------------------------------------------------------------------'
        self.line = self.insert(self.line, 0, '+')
        self.line = self.insert(self.line, 15, '+')
        self.line = self.insert(self.line, 30, '+')
        self.line = self.insert(self.line, 45, '+')
        self.line = self.insert(self.line, 60, '+')
        self.line = self.insert(self.line, 75, '+')
        self.line = self.insert(self.line, 90, '+')
        print(self.line)
                
    def save_users(self):    
        user_dict = []

        for user in self.users_list:
            user_dict.append(user.__dict__)

        with open('user.txt', 'w') as outfile:
            json.dump(user_dict, outfile)


        # with open('user.txt', 'w') as file:
        #     for user in self.users_list:
        #         file.write(user.create_line() + '\n')

        # file.close()

    def split(self, word):
        return [char for char in word]


    def show_users_books(self):
        self.print_user()
        answer = None
        answer_list = []



        print('Enter user id, or enter 0 to skip>')
        answer = self.ask.func_()

        if int(answer) == 0:
            answer = None
            self.user_menu()




        for us in self.users_list:
            if us.id == answer:
                if len(us.books) > 0:
                    for id_book in us.books:
                        id_book = list(id_book.split(","))
                        for obj1 in self.book.books:
                            for var in id_book:
                                try:
                                    if obj1.id == int(var):
                                        print('Here you have: ' + obj1.name)
                                except ValueError:
                                    print('This user is empty')

                else:
                    print('This user is empty')
            


        self.user_menu()