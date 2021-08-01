class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Available books are :")
        for book in self.books:
            print("   \t" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"Your requested book {bookName} has been issued")
            self.books.remove(bookName)
            return True
        else:
            print(f"your requested book {bookName} is not available now")
            return False

    def returnBook(self, bookName):
        print("Thanks for returning the book")
        self.books.append(bookName)

class Student:
    def requestBook(self):
        self.book = input("Please enter the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Please enter the book you want to return: ")
        return self.book


if __name__ == '__main__':
    centralLibrary = Library(["Python", "Java", "C", "c+", "HTML"])
    student = Student()
    #centralLibrary.displayAvailableBooks()
    while(True):
        WelcomeMsg = '''!!!!!!---- WELCOME TO CENTRAL LIBRARY ----!!!!!!
                Please choose an option from below:
                1. List all the Books.
                2. Request a book.
                3. Return a book.
                4. Exit the Library.
                '''
        print(WelcomeMsg)
        a = int(input("Enter the choice:  "))
        if a == 1:
            centralLibrary.displayAvailableBooks()

        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())

        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thank you for using central library.")
            exit()
        else:
            print("Invalid option")

