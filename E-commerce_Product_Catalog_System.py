class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")

class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")

class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):
        super().display_info()
        print(f"Specifications: {self.specs}")

class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")

# Example usage
print("Displaying Generic Product Info:")
generic_product = Product("001", "Generic Product", 19.99)
generic_product.display_info()
print()

print("Displaying Book Info:")
book = Book("123", "Python Essentials", 29.99, "J. Doe")
book.display_info()
print()

print("Displaying Electronic Info:")
electronic = Electronic("456", "Smartphone", 699.99, "64GB, 4GB RAM")
electronic.display_info()
print()

print("Displaying Clothing Info:")
clothing = Clothing("789", "T-Shirt", 19.99, "M")
clothing.display_info()
print()
