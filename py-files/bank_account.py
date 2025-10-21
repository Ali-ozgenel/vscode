class BankAccount:
    def __init__(self, account_number, balance):
        self.customer_number = account_number
        self.customer_balance = balance
    
    def deposit_money(self, amount):
        if amount > 0:
            self.customer_balance = self.customer_balance + amount
            print("The deposit was made in a successful way!")
            print("New balance:", self.customer_balance)
        else:
            print("Invalid amount!")
    
    def withdraw_money(self, amount):
        if amount > 0:
            if amount <= self.customer_balance:
                self.customer_balance = self.customer_balance - amount
                print("Withdrawal is successful!")
                print("New balance:", self.customer_balance)
            else:
                print("Insufficient balance!")
        else:
            print("Invalid amount!")
    
    def show_info(self):
        print("Account Number:", self.customer_number)
        print("Balance:", self.customer_balance)


print("Welcome to the Bank account System")
customer_account_number = input("Enter your account number: ")
customer_starting_balance = float(input("Enter starting balance: "))

my_account = BankAccount(customer_account_number, customer_starting_balance)

while True:
    print("\n--- MENU ---")
    print("1 - Deposit Money")
    print("2 - Withdraw Money")
    print("3 - Show Account Info")
    print("4 - Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        money_amount = float(input("Enter amount to deposit: "))
        my_account.deposit_money(money_amount)
    elif choice == "2":
        withdraw_amount = float(input("Enter amount to withdraw: "))
        my_account.withdraw_money(withdraw_amount)
    elif choice == "3":
        my_account.show_info()
    elif choice == "4":
        print("Exiting from your account, goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")