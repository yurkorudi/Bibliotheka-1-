







class Menu:
    def __init__(self):
        self.book_or_us = None

    def main_menu(self):
        global book
        print('0: users')
        print('1: books')
        self.book_or_us = bool(int(input('>  ')))
        if self.book_or_us:
            book.book_menu()
        else:
            users.user_menu()




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

    def create_line(self):
        return str(self.id) + "|" + self.name + "|" + self.publisher + "|" + self.date + "|" + self.autors

    def print_book(self):
        print(self.id + ":     " + self.name + " " + self.publisher + " " + self.date + " " + self.autors)

    


class Books:

    books = [] # Book

    def __init__(self):
        self.text = []
        self.load_from_file()






    def load_from_file(self):
        lines = []
        with open('book.txt', 'r') as file:
            lines = file.readlines()
            
        for line in lines:
            
            fields = line.split("|")
            if '\n' not in fields:
                id = int(fields[0])
                book = Book(id, fields[1], fields[2], fields[3], fields[4])
                self.books.append(book)





    def print_book(self):
        for book in self.books:
            print(str(book.id) + ":     " + book.name + " " + book.publisher + " " + str(book.date) + " " + book.autors)
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

        with open('book.txt', 'w') as file:
            for book in self.books:
                file.write(book.create_line() + '\n')

            file.close()



    def book_menu(self):
        global menu
        print('0: list of books')
        print('1: add book')
        print('2: change book')
        print('3: delete')
        print('4: EXIT')
        self.menu_answer = int(input('>  '))

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
            menu.main_menu()
    
            
        



    def add_book(self):
        id = len(self.books) + 1

        name = str(input('enter name: '))
        publisher = str(input('enter publisher: '))
        date_publish = str(input('enter date: '))
        autors = str(input('enter autor: '))

        book = Book(id, name, publisher, date_publish, autors)
        self.books.append(book)

        self.save_to_file()
        self.book_menu()





    def edit(self):
        self.print_book()
        nomber = int(input('Enter nomber of book to edit>  '))

        print('To skip editing - press enter')
        
        name_int = self.books[nomber-1].name
        name = str(input('enter new name (old name {}): '.format(name_int)))
        if len(name) != 0:
            name_int = name
        
        publisher_int = self.books[nomber-1].publisher
        publisher = str(input('enter new publisher (old publisher {}): '.format(publisher_int)))
        if len(publisher) != 0:
            publisher_int = publisher

        date_publish_int = self.books[nomber-1].date
        date_publish = str(input('enter new date (old date {}): '.format(date_publish_int)))
        if len(date_publish) != 0:
            date_publish_int = date_publish

        autors_int = self.books[nomber-1].autors
        autors = str(input('enter new autor (old autors {}): '.format(autors_int)))
        if len(autors) != 0:
            autors_int = autors
        

        book = Book(nomber, name_int, publisher_int, date_publish_int, autors_int)
        self.books[nomber-1] = book
        self.save_to_file()
        self.book_menu()




    def del_book(self):
        self.print_book()

        nomber = int(input('Enter nomber of element you want to delete>  '))
        del self.books[nomber-1]
        self.save_to_file()
        self.book_menu()




################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################



class User:
    id = ''
    first_name = ''
    last_name = ''
    age = ''
    adress = ''
    nomber = ''
    books = ''

    def __init__(self, id, first_name, last_name, age, adress, nomber, books):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.adress = adress
        self.nomber = nomber
        self.books = books


    def create_line(self):
        book = ''
        for i in self.books:
            book = book + str(i) + ' '

        return str(self.id) + '|' + self.first_name + '|' + self.last_name + '|' + str(self.age) + '|' + str(self.adress) + '|' + str(self.nomber) + '|' + book
            

    def print_user(self):
        print(str(self.id) + '    ' + self.first_name + ' ' + self.last_name + ' ' + str(self.age) + ' ' + str(self.adress) + '|' + str(self.nomber))











class Users:

    users_list = []

    def __init__(self):
        self.load_from_file()



    
    def load_from_file(self):
        lines = []

        with open('user.txt', 'r') as file:
            lines = file.readlines()

        for line in lines:
            fields = line.split('|')

            if '\n' not in fields:
                books = fields[6].split(" ")
                for a in books:
                    if a == '\n':
                        books.remove(a)


                books = [int(b.strip('\n').strip(" ")) for b in books]
                user = User(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], books)
                self.users_list.append(user)


    def user_menu(self):
        print('0: add user')
        print('1: del user')
        print('2: change user')
        print('3: list user')
        print('4: list user > book')
        print('5: EXIT')

        self.menu_answer = int(input('>   '))

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
            menu.main_menu()





    def add_user(self):
        id = len(self.users_list) + 1

        first_name = str(input('first name>  '))
        last_name = str(input('laast name>  '))
        age = int(input('age>  '))
        adress = str(input('adress>  '))
        nomber = int(input('nomber>   '))
        books = str(input('id of books, to cont... enter 0>   '))
        if books != '0':
            books = books.split(' ')
            # books = books.split('@')
            # books_to_print = str(books)
            # books_to_print.strip()
        else:
            books = []
        
        
        

        user = User(id, first_name, last_name, age, adress, nomber, books)
        self.users_list.append(user)
        self.save_users()
        self.user_menu()




        

    def del_user(self):
        self.print_user()

        nomber = int(input('Enter nomber of element you want to delete>  '))
        del self.users_list[nomber-1]
        self.save_users()
        self.user_menu()

    def change_user(self):
        pass

    def print_user(self):
        for user in self.users_list:
            books = str(book.find_book(user.books))
            books = books.strip(']')
            books = books.strip('[')
            books = books.strip("'")
            print(str(user.id) + '    ' + user.first_name + ' ' + user.last_name + ' ' + str(user.age) + ' ' + str(user.adress) + ' ' + str(user.nomber))



    def save_users(self):
        
        with open('user.txt', 'w') as file:
            for user in self.users_list:
                file.write(user.create_line() + '\n')

        file.close()

    def split(self, word):
        return [char for char in word]


    def show_users_books(self):
        self.print_user()
        answer = None
        answer_list = []




        answer = int(input('enter user id, or enter 0 to skip>   '))
        if answer == 0:
            answer = None
            self.user_menu()


        if len(self.users_list[answer - 1].books) == 1:
            print(book.books[self.users_list[answer - 1].books].name)

        elif len(self.users_list[answer - 1].books) > 1:
            for id_book in self.users_list[answer - 1].books:
                for obj1 in book.books:
                    if obj1.id == id_book:
                        print(obj1.name)

        elif len(self.users_list[answer - 1].books) == 0:
            print('this user is empty')




        self.user_menu()








###########
menu = Menu()
book = Books()

users = Users()
##############




menu.main_menu()

