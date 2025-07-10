class BankAccount:
    '''
    class representing a bank account

    manages an account with a name, account number, and balance, with the ability to withdraw and deposit money
    '''
    def __init__(self, name: str, account_number: str, balance: float):
        '''
        Makes bankaccount object.
        parameters: 
        name (string): name of the account being created
        account_number(string): identifying number for an account, stored as a string in case of leading zeroes
        balance(float): a users current balance
        '''
        self.balance = balance
        self.name = name
        self.account_number = account_number
    
    def print_current_balance(self):
        print (f"Your current balance is: {self.balance}")
        return self.balance
    
    def withdraw_amount(self, amount):
        '''
        withdraws an amount specified by the user
        checks for the amount being zero or negative, being bigger than the balance, and if it isn't a number
        '''

        if not isinstance(amount, (int, float)):
             raise TypeError("Withdrawal amount must be a number.")
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        if amount > self.balance:
            raise ValueError(f"You're too broke. Thoust shall not go into debt.")
        
        self.balance -= float(amount)
        print(f"\n\nHooray, you withdrew ${amount}. New balance: ${self.balance}")
        
        

    def deposit_amount(self, amount):
        '''
        read withdraw, its the same thing except adding
        '''

        if not isinstance(amount, (int, float)):
             raise TypeError("Deposit amount must be a number.")
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        if amount >= 10000:
            raise ValueError("You is not that rich bro")
        
        self.balance += float(amount)
        print(f"\n\nHooray, you deposited ${amount}. New balance: ${self.balance}")

print("===================Testing===================")
try:
    my_account = BankAccount(name="John Doe", account_number="2099", balance=500.0)
    print("Balance test:\n")
    my_account.print_current_balance()
except Exception as e:
    print(f"An unexpected error occurred during creation: {e}")


print("\nDeposit test")
try:
    my_account.deposit_amount(250.50)
    my_account.print_current_balance()
except (ValueError, TypeError) as e:
    print(f"Error during deposit: {e}")


print("\nWithdraw test")
try:
    my_account.withdraw_amount(100)
    my_account.print_current_balance()
except (ValueError, TypeError) as e:
    print(f"Error during withdrawal: {e}")


print("\nTesting deposit >= 10000")
try:
    my_account.deposit_amount(15000)
except ValueError as e:
    print(f"Caught expected error: {e}")


print("\nTesting withdraw if you have enough money in account")
try:
    print(f"Withdrawing $1000 from a balance of ${my_account.balance}")
    my_account.withdraw_amount(1000)
except ValueError as e:
    print(f"Caught expected error: {e}")


print("\nTesting deposit negative number")
try:
    my_account.deposit_amount(-50)
except ValueError as e:
    print(f"Caught expected error: {e}")

print("\nTesting withdraw negative number")
try:
    my_account.withdraw_amount(-100)
except ValueError as e:
    print(f"Caught expected error: {e}")


print("\nTesting deposit of string")
try:
    my_account.deposit_amount("one hundred")
except TypeError as e:
    print(f"Caught expected error: {e}")


