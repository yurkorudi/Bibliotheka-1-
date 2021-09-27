from users import Users 
from books import Books 
from menu  import Menu
from to_int import To_int_ask


def main():
    ask = To_int_ask()
    book = Books(ask)
    users = Users(book, ask)
    

    menu = Menu()
    menu.main_menu(book, users)

if __name__ == "__main__":
    main()