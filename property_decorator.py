class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self._price = price

    @property
    def price(self):
        """The getter for the price property."""
        print("Getting the price...")
        return self._price

    @price.setter
    def price(self, new_price: float):
        """The setter for the price property, with validation."""
        print("Setting the price...")
        if not isinstance(new_price, (int, float)) or new_price <= 0:
            raise ValueError("Price must be a positive number.")
        self._price = new_price

    @price.deleter
    def price(self):
        """The deleter for the price property."""
        print("Deleting the price...")
        del self._price

book = Product("Cookbook", 45.0)

print(f"Product name: {book.name}, price: ${book.price}")

book.price = 50.0
print(f"Updated price: {book.price}")

try:
    book.price = -10.0
except ValueError as e:
    print(f"Error: {e}")

del book.price

try:
    print(book.price)
except AttributeError as e:
    print(f"Error: {e}")