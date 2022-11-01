from math import prod


class ProductInformation:

    # The following defines the constructor
    def __init__(self, IDnumber, name, price, quantity):
        self.IDnumber = IDnumber
        self.name = name
        self.price = price
        self.quantity = quantity

    # Determines if there is available stock
    def in_stock(self, quantity):
        return self.quantity >= quantity

    # Subtracts quantity purchased from the old quantity before purchase to get updated quantity after purchase
    def updated_stock(self, quantity):
        self.quantity -= quantity

    # Multiples the price by product quantity purchased to get subtotal
    def prod_cost(self):
        return self.price * self.quantity

# Lists the information for each product (i.e. Product ID, Item Name, Price, Quantity)


prod1 = ProductInformation(0, "Lithium polymer battery", 8.99, 8)
prod2 = ProductInformation(1, "Laser range finder", 149.99, 2)
prod3 = ProductInformation(2, "Microcontroller Board", 34.95, 7)
prod4 = ProductInformation(3, "Servo controller", 44.95, 5)
prod5 = ProductInformation(4, "Servo Motor", 14.99, 10)
prod6 = ProductInformation(5, "Ultrasonic range finder", 2.50, 4)

products = [prod1, prod2, prod3, prod4, prod5, prod6]


def print_stock():
    print("\nAvailable Products")
    print("-------------")
    for i in range(0, len(products)):
        if products[i].quantity > 0:
            print(
                f"{str(i)}) {products[i].name}, ${products[i].price}, {products[i].quantity} left in stock")
    print()

    # Input cash amount
    # Enter product ID and quantity of product you want


def main():
    cash = float(input("How much money would you like to deposit? $"))
    while cash > 0:
        print_stock()
        vals = input(
            "Enter product ID and quantity you wish to buy. Separate the values with a semicolon: ").split(";")
        if vals[0] == "quit":
            break

        prod_id = int(vals[0])
        count = int(vals[1])

        product = None
        for i in products:
            if i.IDnumber == prod_id:
                product = i

        # Only products with valid ID number are found. If not, print the message below.
        if product == None:
            print("Product with ID {prod_id} not found.")
            continue

        # Low inventory notice for customer
        if not product.in_stock(count):
            print("Not enough inventory available for purchase!")
            continue

        # Calculates price by utilizing product * quantity
        price = product.price * count

        # Insufficient funds notice
        if cash < price:
            print("Sorry, balance is insufficient.")

        # Updates the stock quantity after purchase
        # Subtracts the price from remaining cash
        product.updated_stock(count)
        cash -= price

        print("You have $", "{0:.2f}".format(cash), "remaining.")


main()
