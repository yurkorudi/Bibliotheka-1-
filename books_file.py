import json
from to_int import To_int_ask
to_int = To_int_ask()

class Book:
    id = ""
    name = ""
    publisher = ""
    date = ""
    autors = ""

    def __init__(self, id, name, publisher, date, autors):
        self.id = id
        self.name = name
        self.publisher = publisher
        self.date = date
        self.autors = autors

    def insert(self, s, index, value):
        return  s[:index] + value + s[index:]

class Books:

    books = [] # Book

    def __init__(self, ask):
        self.text = []
        self.ask = ask
        self.publisher_list = []
        self.load_from_file()


    def load_from_file(self):

        lines = []
        file = open('book.txt')
        data = json.load(file)
      

        for obg in data:

            book = Book(obg["id"], obg["name"], obg["publisher"], obg["date"], obg["autors"])
            self.books.append(book)



        lines = []
        file = open('publisher.txt')
        data = json.load(file)

        for obj in data['publishers']:
            self.publisher_list.append(obj)
        





    def set_user(self, user):
        self.user = user




    def insert(self, s, index, value):
        if len(value) > 9:
            value = value[0:9]
        return  s[:index] + value + s[index:]


    def print_book(self):


        self.line =  '------------------------------------------------------'

        self.line = self.insert(self.line, 0, '+')
        self.line = self.insert(self.line, 10, '+')
        self.line = self.insert(self.line, 20, '+')
        self.line = self.insert(self.line, 30, '+')
        self.line = self.insert(self.line, 40, '+')
        self.line = self.insert(self.line, 50, '+')
        self.line = self.insert(self.line, 61, '+')

        print(self.line)



        self.line =  '                                  '

        self.line = self.insert(self.line, 0, '|')
        self.line = self.insert(self.line, 1, 'id')
        self.line = self.insert(self.line, 10, '|')
        self.line = self.insert(self.line, 11, 'name')
        self.line = self.insert(self.line, 20, '|')
        self.line = self.insert(self.line, 21, 'publisher')
        self.line = self.insert(self.line, 30, '|')
        self.line = self.insert(self.line, 31, 'date')
        self.line = self.insert(self.line, 40, '|')
        self.line = self.insert(self.line, 41, 'autors')
        self.line = self.insert(self.line, 50, '|')
        self.line = self.insert(self.line, 51, 'Owner')
        self.line = self.insert(self.line, 60, '|')

        print(self.line)



        self.line =  '------------------------------------------------------'

        self.line = self.insert(self.line, 0, '+')
        self.line = self.insert(self.line, 10, '+')
        self.line = self.insert(self.line, 20, '+')
        self.line = self.insert(self.line, 30, '+')
        self.line = self.insert(self.line, 40, '+')
        self.line = self.insert(self.line, 50, '+')
        self.line = self.insert(self.line, 61, '+')

        print(self.line)
        #+rrr
        for book in self.books:
            bookwithn = book.autors
            bookwithn = bookwithn.strip('\n')
            self.line =  '                                                         '

            self.line = self.insert(self.line, 0, '+')
            self.line =self.insert(self.line,  1, str(book.id))
            self.line =self.insert(self.line, 10, '+')
            self.line =self.insert(self.line, 11, book.name)
            self.line =self.insert(self.line, 20, '+')
            self.line =self.insert(self.line, 21, book.publisher)
            self.line =self.insert(self.line, 30, '+')
            self.line =self.insert(self.line, 31, book.date)
            self.line =self.insert(self.line, 40, '+')
            self.line =self.insert(self.line, 41, book.autors)
            self.line =self.insert(self.line, 50, '+')
            self.line =self.insert(self.line, 51, self.look_for_table(book))
            self.line =self.insert(self.line, 60, '+')

            print(self.line)

        self.line =  '------------------------------------------------------'

        self.line = self.insert(self.line, 0, '+')
        self.line = self.insert(self.line, 10, '+')
        self.line = self.insert(self.line, 20, '+')
        self.line = self.insert(self.line, 30, '+')
        self.line = self.insert(self.line, 40, '+')
        self.line = self.insert(self.line, 50, '+')
        self.line = self.insert(self.line, 60, '+')

        print(self.line)


    def find_book(self, id):
        answer = []
        for book in self.books:
            for i in id:
                if book.id == i:
                    answer.append(book.name)
        answer = str(answer)
        answer.strip()
        return answer
        

    def save_to_file(self):


        books_dic = []

        for book in self.books:
            books_dic.append(book.__dict__)

        with open('book.txt', 'w') as outfile:
            json.dump(books_dic, outfile, indent=4)


    def book_menu(self):
        global menu
        print('##   Menu  ###')
        print('  0: EXIT')
        print('  1: Add book')
        print('  2: Change book')
        print('  3: Delete')
        print('  4: List of books')
        print('  5: look user')

        try:
            self.menu_answer = int(input(">  "))
        except ValueError:
            print('''Maybe you entered some str symbol's, try with out it''')
            self.book_menu()

        if self.menu_answer <= 4 and self.menu_answer >= 0:
            if self.menu_answer == 0:
                return
            
            if self.menu_answer == 1:
                self.add_book()

            if self.menu_answer == 2:
                self.edit()

            if self.menu_answer == 3:
                self.del_book()

            if self.menu_answer == 4:
                self.print_book()
                self.book_menu()



        else:
            print('''NO-NO-NO, it's not an answer!''')
            self.book_menu()
        

    def add_book(self):
        id = len(self.books) + 1

        name = str(input('enter name: or to exit enter 0:  '))
        try:
            if int(name) == 0:
                return
        except ValueError:
            pass
        publisher = self.publisher_input()
        date_publish = self.date_input()
        autors = str(input('enter autor: '))
        book = Book(id, name, publisher, date_publish, autors)
        self.books.append(book)

        self.save_to_file()
        self.book_menu()


    def edit(self):
        self.print_book()
        print('Enter number of book to edit> or to exit enter 0:  ')
        number = self.ask.func_()
        try:
            if int(number) == 0:
                return
        except ValueError:
            pass
        name_int = self.books[number-1].name
        name = str(input('enter new name (old name {}): '.format(name_int)))
        if len(name) != 0:
            name_int = name
        
        publisher_int = self.books[number-1].publisher
        publisher = str(input('enter new publisher (old publisher {}): '.format(publisher_int)))
        if len(publisher) != 0:
            publisher_int = publisher

        date_publish_int = self.books[number-1].date
        date_publish = str(input('enter new date (old date {}): '.format(date_publish_int)))
        if len(date_publish) != 0:
            date_publish_int = date_publish

        autors_int = self.books[number-1].autors
        autors = str(input('enter new autor (old autors {}): '.format(autors_int)))
        if len(autors) != 0:
            autors_int = autors
        

        book = Book(number, name_int, publisher_int, date_publish_int, autors_int)
        self.books[number-1] = book
        self.save_to_file()
        self.book_menu()


    def del_book(self):
        self.print_book()

        print('Enter number of element you want to delete> or to exit enter 0>  ')
        number = self.ask.func_()
        try:
            if int(number) == 0:
                return
        except ValueError:
            pass
        del self.books[number-1]
        self.save_to_file()
        self.book_menu()
        self.book_menu()


    def date_input(self):
        cycle = True
        error = 0
        while cycle:
            try:
                day = int(input("Enter day>   "))
                month = int(input('Enter month>   '))
                year = int(input('Enter year>   '))
                error = 0
            except ValueError:
                print('Wrong date.')
                error += 1

            if error == 0:
                if day > 31 or day < 1:
                    print("Wrong day")
                    error += 1
                if month > 12 or month < 1:
                    print("Wrong month")
                    error += 1
                if year < 1600 or year > 2021:
                    print("Wrong year")
                    error+=1


            if error == 0:
                return str(day) + ' ' + str(month) + ' ' + str(year)
            else:
                print("Try again!")


    def look_for_table(self, book):
        resoult = ' '
        target = book
        
        id = self.books[target.id-1].id

        for us in self.user.users_list:
            us.books = list(us.books[0].split(","))
            for chek in us.books:
                if chek != '':
                    if int(chek) == id:
                        resoult = resoult + us.first_name + ' ' + us.last_name
                
        
        if resoult == ' ':
            resoult = 'Nobody'

        return resoult



    def publisher_input(self):
        cycle = 0
        print("choose one of given publishers")
        for obj in self.publisher_list:
            print(str(cycle)+') ' + obj)
            cycle += 1


        cycle = True
        while True:
            try:
                answer = int(input("Enter answer>   "))
                if answer > len(self.publisher_list) or answer < 0:
                    print("Wrong answer. Try real")
                else:
                    return self.publisher_list[answer]
            except ValueError:
                print("Wrong answer. Try real")







