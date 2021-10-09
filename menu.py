

class Menu:
    def __init__(self):
        self.book_or_us = None

    def main_menu(self, book, users):
        while True:
            print('##   Main Menu   ##')
            print('  0: users')
            print('  1: books')
            try:
                self.book_or_us = int(input('>  '))
            except ValueError:
                print('''NO-NO-NO, it's not an answer!''')
                self.main_menu(book, users)
                break                
            if type(self.book_or_us) == int:
                self.book_or_us = int(self.book_or_us)
                if self.book_or_us == 1 or self.book_or_us == 0:
                    if self.book_or_us == 1:
                        book.book_menu()
                    else:
                        users.user_menu()
                else:
                    print('''NO-NO-NO, it's not an answer!''')
                    self.main_menu(book, users)
                    break
            else:
                print('''NO-NO-NO, it's not an answer!''')
                self.main_menu(book, users)
                break
            







