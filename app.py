from users_file import Users 
from books_file import Books 
from menu  import Menu
from to_int import To_int_ask


def main():
    ask = To_int_ask()
    books = Books(ask)
    users = Users(ask)
    books.set_user(users)
    users.set_books(books)
    

    menu = Menu()
    menu.main_menu(books, users)

if __name__ == "__main__":
    main()