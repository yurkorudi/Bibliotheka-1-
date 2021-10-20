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


    def print_user(self):
        a = (str(self.id) + '    ' + self.first_name + ' ' + self.last_name + ' ' + str(self.age) + ' ' + str(self.adress) + '|' + str(self.number))
        print(json.dumps(a, indent=4, sort_keys=True))



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


            user = User(obg["id"], obg["first_name"], obg["last_name"], obg["age"],obg["adress"], obg["number"], obg["books"])
            self.users_list.append(user)


    def user_menu(self):
        print('##    Menu:   ##')
        print('   0: EXIT')
        print('   1: Delete user')
        print('   2: Change user')
        print('   3: Print list user')
        print('   4: Print list user > book')
        print('   5: Add user')

        try:
            self.menu_answer = int(input('>   '))
        except ValueError:
            print('''NO-NO-NO, it's not an answer!''')
            self.user_menu()


        if self.menu_answer <= 5 and self.menu_answer >= 0:

            if self.menu_answer == 0:
                return
            
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
                self.add_user()
        
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
        print('Enter phone number:   ')
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
        self.print_user()
        number = self.ask.func_()
        try:
            if int(number) == 0:
                return
        except ValueError:
            pass


        first_name_int = self.users_list[number-1].first_name
        name = str(input('enter new first name (old name {}): '.format(first_name_int)))
        if len(name) != 0:
            first_name_int = name


        last_name_int = self.users_list[number-1].last_name
        name = str(input('enter new last name (old name {}): '.format(last_name_int)))
        if len(name) != 0:
            last_name_int = name


        age_int = self.users_list[number-1].age
        try:
            age = int(input('enter new age (old name {}): '.format(age_int)))
        except ValueError:
            print("wrong age. Enter real!")
            self.change_user()
        if len(age) != 0:
            age_int = age


        adress_int = self.users_list[number-1].adress
        adress = str(input('enter new adress (old name {}): '.format(first_name_int)))
        if len(name) != 0:
            adress_int = adress

        
        number_int = self.users_list[number-1].number
        try:
            number = int(input('enter new phone number (old name {}): '.format(number_int)))
        except ValueError:
            print("wrong number. Enter real!")
            self.change_user()
        if len(number) != 0:
            number_int = number


        books_int = self.users_list[number-1].books
        books = str(input('enter new books (old name {}): '.format(books_int)))
        if len(books) != 0:
            books_int = books


        user = User(id, first_name_int, last_name_int, age_int, adress_int, number_int, books_int)
        self.users_list.append(user)
        self.save_users()
        self.user_menu()


    def insert(self, s, index, value):
        if len(value) > 9:
            value = value[0:9]
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
        self.line = self.insert(self.line, 76, 'phone number')
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

            self.line =  '                                                                                 '
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
            json.dump(user_dict, outfile, indent=4)


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