class Book(object):
    author = ""
    title = ""

    def __init__(self, author="", title=""):
        self.author = author
        self.title = title

    def display(self):
        print("{0}, written by {1}".format(self.title, self.author))


if __name__ == "__main__":
    book1 = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
    book2 = Book("Walter Scott", "Ivanhoe: A Romance")

    book1.display()
    book2.display()