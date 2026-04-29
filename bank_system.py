class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ₹{amount}")
        else:
            print("❌ Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Invalid amount")
        elif amount > self.balance:
            print("❌ Insufficient balance")
        else:
            self.balance -= amount
            print(f"✅ Withdrawn ₹{amount}")

    def check_balance(self):
        print(f"💰 Current Balance: ₹{self.balance}")


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        name = input("Enter Name: ")
        acc_no = input("Enter Account Number: ")

        if acc_no in self.accounts:
            print("❌ Account already exists!")
        else:
            self.accounts[acc_no] = BankAccount(name, acc_no)
            print("✅ Account created successfully")

    def get_account(self):
        acc_no = input("Enter Account Number: ")
        return self.accounts.get(acc_no)

    def deposit(self):
        account = self.get_account()
        if account:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        else:
            print("❌ Account not found")

    def withdraw(self):
        account = self.get_account()
        if account:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        else:
            print("❌ Account not found")

    def check_balance(self):
        account = self.get_account()
        if account:
            account.check_balance()
        else:
            print("❌ Account not found")


def main():
    bank = BankSystem()

    while True:
        print("\n===== BANK MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            bank.create_account()
        elif choice == '2':
            bank.deposit()
        elif choice == '3':
            bank.withdraw()
        elif choice == '4':
            bank.check_balance()
        elif choice == '5':
            print("👋 Thank you for using the system")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()