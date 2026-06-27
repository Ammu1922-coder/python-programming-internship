class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: ₹"))

            if amount <= 0:
                raise ValueError("Amount should be greater than 0.")

            self.balance += amount
            print("Amount Deposited Successfully!")

        except ValueError as e:
            print(e)

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: ₹"))

            if amount <= 0:
                raise ValueError("Amount should be greater than 0.")

            if amount > self.balance:
                raise ValueError("Insufficient Balance!")

            self.balance -= amount
            print("Withdrawal Successful!")

        except ValueError as e:
            print(e)

    def display_balance(self):
        print("Current Balance: ₹", self.balance)


account = BankAccount("Ammu", 5000)

while True:

    print("\n1.Deposit")
    print("2.Withdraw")
    print("3.Display Balance")
    print("4.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        account.deposit()

    elif choice == "2":
        account.withdraw()

    elif choice == "3":
        account.display_balance()

    elif choice == "4":
        break

    else:
        print("Invalid Choice!")