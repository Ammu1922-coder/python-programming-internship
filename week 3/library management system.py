class Library:

    def __init__(self):
        self.books = ["Python", "Java", "C++"]

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(book)

    def add_book(self):
        book = input("Enter book name: ")
        self.books.append(book)
        print("Book Added!")

    def remove_book(self):
        book = input("Enter book name: ")

        if book in self.books:
            self.books.remove(book)
            print("Book Removed!")
        else:
            print("Book Not Found!")

    def issue_book(self):
        book = input("Enter book name: ")

        if book in self.books:
            self.books.remove(book)
            print("Book Issued Successfully!")
        else:
            print("Book Not Available!")

    def return_book(self):
        book = input("Enter returned book: ")
        self.books.append(book)
        print("Book Returned Successfully!")


library = Library()

while True:

    print("\n1.Display Books")
    print("2.Add Book")
    print("3.Remove Book")
    print("4.Issue Book")
    print("5.Return Book")
    print("6.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        library.display_books()

    elif choice == "2":
        library.add_book()

    elif choice == "3":
        library.remove_book()

    elif choice == "4":
        library.issue_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        break

    else:
        print("Invalid Choice!")