class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity

class Bill:

    TAX = 0.18

    def __init__(self):
        self.products = []

    def add_product(self):

        name = input("Product Name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        self.products.append(Product(name, price, quantity))

    def generate_bill(self):

        print("\n---------------------------------------------")
        print("{:<15}{:<10}{:<10}{:<10}".format(
            "Product", "Price", "Qty", "Total"))
        print("---------------------------------------------")

        subtotal = 0

        for product in self.products:

            total = product.total()
            subtotal += total

            print("{:<15}{:<10}{:<10}{:<10}".format(
                product.name,
                product.price,
                product.quantity,
                total))

        tax = subtotal * Bill.TAX
        grand_total = subtotal + tax

        print("---------------------------------------------")
        print("Subtotal :", subtotal)
        print("Tax (18%):", tax)
        print("Grand Total:", grand_total)
        print("---------------------------------------------")


bill = Bill()

while True:

    print("\n1.Add Product")
    print("2.Generate Bill")
    print("3.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        bill.add_product()

    elif choice == "2":
        bill.generate_bill()

    elif choice == "3":
        break

    else:
        print("Invalid Choice!")
