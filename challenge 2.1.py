class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ₹{amount}. New balance is ₹{self.__account_balance}."
        else:
            return "Invalid deposit amount. Please deposit a positive amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ₹{amount}. New balance is ₹{self.__account_balance}."
        elif amount > self.__account_balance:
            return "Insufficient funds for withdrawal."
        else:
            return "Invalid withdrawal amount. Please withdraw a positive amount."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name} (Account #{self.__account_number}): ₹{self.__account_balance}"

# Create an instance of BankAccount
my_account = BankAccount(311425, "Ahamed", 1000)

# Test deposit and withdrawal functionality
print(my_account.display_balance())
print(my_account.deposit(500))
print(my_account.withdraw(200))
print(my_account.withdraw(1500))