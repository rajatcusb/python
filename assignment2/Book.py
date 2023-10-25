class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPrice: ${self.price:.2f}"

    def apply_discount(self, discount_percentage):
        if discount_percentage >= 0 and discount_percentage <= 100:
            self.price -= (self.price * discount_percentage / 100)

class EBook(Book):
    def __init__(self, title, author, price, format):
        super().__init__(title, author, price)
        self.format = format

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPrice: ${self.price:.2f}\nFormat: {self.format}"

# Create a Book object
book1 = Book("Python Programming", "John Smith", 29.99)

# Display the book's information and apply a discount
print("Book Information:")
print(book1.display_info())
book1.apply_discount(20)
print("\nBook Information after Discount:")
print(book1.display_info())

# Create an EBook object
ebook1 = EBook("Advanced Python", "Alice Johnson", 19.99, "PDF")

# Display the ebook's information (overrides the method in the parent class)
print("\nEBook Information:")
print(ebook1.display_info())
