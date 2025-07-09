class BankAccount:
    def __init__(self, balance, name, account_number, withdraw_amount, deposit_amount):
        self.balance = balance
        self.name = name
        self.account_number = account_number
        self.withdraw_amount = withdraw_amount
        self.deposit_amount = deposit_amount
    
    def print_current_balance(self):
        print (f"Your current balance is: {self.balance}")
        return self.balance
    
    def withdraw_amount(self): #could return true false, raise error, trycatch for raising errors
        if self.balance - self.withdraw_amount < 0:
            print("Your too broke. You shall not make a bad financial decision.")
        elif self.balance - self.withdraw_amount == 0:
            print("You have $0. How silly.")
        else:
            self.new_balance = self.balance - self.withdraw_amount
            print(f"Current Balance: {self.balance}\nWithdrawn Amount: {self.withdraw_amount}\nNew Balance: {self.new_balance}")

    def deposit_amount(self):
        pass





tester = BankAccount(5.00, "John, 1234567890, 3.00, 0")

tester.withdraw_amount()

        
 
        

        