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

    # def create_line(self):
    #     a = {"id" : str(self.id), "name" : self.name,  "publisher" : self.publisher, "date" : str(self.date), "autors" : self.autors}
    #     return json.dumps(a, indent=4, sort_keys=True)
    
    def insert(self, s, index, value):
        return  s[:index] + value + s[index:]







class Books:

    books = [] # Book

    def __init__(self, ask):
        self.text = []
        self.ask = ask
        self.load_from_file()






    def load_from_file(self):

        lines = []
        file = open('book.txt')
        data = json.load(file)
      
        for obg in data:

            book = Book(obg["id"], obg["name"], obg["publisher"], obg["date"], obg["autors"])
            self.books.append(book)


    def insert(self, s, index, value):
        return  s[:index] + value + s[index:]




    def print_book(self):


        self.line =  '---------------------------------------------'

        self.line = self.insert(self.line, 0, '+')
        self.line = self.insert(self.line, 10, '+')
        self.line = self.insert(self.line, 20, '+')
        self.line = self.insert(self.line, 30, '+')
        self.line = self.insert(self.line, 40, '+')
        self.line = self.insert(self.line, 51, '+')

        print(self.line)



        self.line =  '                    '

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

        print(self.line)



        self.line =  '---------------------------------------------'

        self.line = self.insert(self.line, 0, '+')
        self.line = self.insert(self.line, 10, '+')
        self.line = self.insert(self.line, 20, '+')
        self.line = self.insert(self.line, 30, '+')
        self.line = self.insert(self.line, 40, '+')
        self.line = self.insert(self.line, 51, '+')

        print(self.line)
        #+rrr
        for book in self.books:
            bookwithn = book.autors
            bookwithn = bookwithn.strip('\n')
            self.line =  '                                 '

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

            print(self.line)

        self.line =  '---------------------------------------------'

        self.line = self.insert(self.line, 0, '+')
        self.line = self.insert(self.line, 10, '+')
        self.line = self.insert(self.line, 20, '+')
        self.line = self.insert(self.line, 30, '+')
        self.line = self.insert(self.line, 40, '+')
        self.line = self.insert(self.line, 51, '+')

        print(self.line)

        
            #print(str(book.id) + ":     " + book.name + " " + book.publisher + " " + str(book.date) + " " + book.autors)
        #self.book_menu()



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
            json.dump(books_dic, outfile)


    def book_menu(self):
        global menu
        print('##   Menu  ###')
        print('  0: List of books')
        print('  1: Add book')
        print('  2: Change book')
        print('  3: Delete')
        print('  4: EXIT')

        try:
            self.menu_answer = int(input(">  "))
        except ValueError:
            print('''Maybe you entered some str symbol's, try with out it''')
            self.book_menu()

        if self.menu_answer <= 4 and self.menu_answer >= 0:
            if self.menu_answer == 0:
                self.print_book()
                self.book_menu()
            
            if self.menu_answer == 1:
                self.add_book()

            if self.menu_answer == 2:
                self.edit()

            if self.menu_answer == 3:
                self.del_book()

            if self.menu_answer == 4:
                return

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
        publisher = str(input('enter publisher: '))
        date_publish = str(input('enter date: '))
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