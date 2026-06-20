class ATM:

    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def login(self):
        entered_pin = input("Enter your PIN: ")

        if entered_pin == self.pin:
            print("Login Successful!")
            return True
        else:
            print("Invalid PIN!")
            return False

    def check_balance(self):
        print("Current Balance: ₹", self.balance)

    def deposit(self):
        amount = float(input("Enter amount to deposit: ₹"))

        if amount > 0:
            self.balance += amount
            print("Amount Deposited Successfully!")
            print("Updated Balance: ₹", self.balance)
        else:
            print("Invalid Amount!")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount > self.balance:
            print("Insufficient Balance!")
        elif amount <= 0:
            print("Invalid Amount!")
        else:
            self.balance -= amount
            print("Withdrawal Successful!")
            print("Remaining Balance: ₹", self.balance)

    def menu(self):
        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.check_balance()

            elif choice == "2":
                self.deposit()

            elif choice == "3":
                self.withdraw()

            elif choice == "4":
                print("Thank You For Using ATM!")
                break

            else:
                print("Invalid Choice!")


user1 = ATM("1234", 5000)

if user1.login():
    user1.menu()