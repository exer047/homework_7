class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        self.review = {}

    def __eq__(self, other):
        if \
                [
                    self.name,
                    self.author,
                    self.year
                ] == [other.name,
                      other.author,
                      other.year
                      ]:
            return True
        else:
            return False

    def add_review(self, number, text):
        self.review[number] = text

    def show_reviews(self):
        for i in self.review:
            print(i, self.review[i])

    def delete_review(self, number):
        del self.review[number]


if __name__ == '__main__':
    book1 = Book("Generation P", "Viktor Pelevin", 1999)
    book2 = Book("Generation P", "Viktor Pelevin", 1999)
    book3 = Book("Nineteen Eghty-Four", "George Orwell", 1949)

    print(book1 == book3)
    print()

    book1.add_review(1, "Cool!")
    book1.add_review(2, "Not bad!")
    book1.show_reviews()
    book1.delete_review(1)
    print()
    book1.show_reviews()
    book3.add_review(1, "Great!")
    print()
    book3.show_reviews()
    book2.show_reviews()
