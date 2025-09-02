#!/usr/bin/python3

class Checkbook:
    """
    A simple checkbook class for managing a bank account balance.
    
    Function Description:
    This class simulates a basic checkbook that allows users to deposit money,
    withdraw money, and check their current balance. It maintains a running
    balance and provides appropriate feedback for all transactions.
    
    Attributes:
    balance (float): The current account balance, initialized to 0.0
    """
    
    def __init__(self):
        """
        Initialize a new Checkbook instance.
        
        Function Description:
        Constructor that creates a new checkbook with a starting balance of zero.
        
        Parameters:
        None
        
        Returns:
        None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Function Description:
        Adds the specified amount to the current balance and displays
        the deposited amount and new balance to the user.
        
        Parameters:
        amount (float): The amount of money to deposit. Should be positive.
        
        Returns:
        None: Prints deposit confirmation and updated balance.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        
        Function Description:
        Attempts to withdraw the specified amount from the current balance.
        If sufficient funds are available, the withdrawal is processed.
        Otherwise, an insufficient funds message is displayed.
        
        Parameters:
        amount (float): The amount of money to withdraw. Should be positive.
        
        Returns:
        None: Prints withdrawal confirmation and updated balance, or
              insufficient funds message if balance is too low.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
            
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current account balance.
        
        Function Description:
        Shows the current balance in the account formatted as currency.
        
        Parameters:
        None
        
        Returns:
        None: Prints the current balance to the console.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def get_positive_amount(prompt):
    """
    Get a positive numeric amount from user input with error handling.
    
    Function Description:
    Continuously prompts the user for a numeric input until a valid
    positive number is entered. Handles ValueError exceptions for
    non-numeric input.
    
    Parameters:
    prompt (str): The message to display when asking for input.
    
    Returns:
    float: A positive numeric value entered by the user.
    """
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be positive. Please try again.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """
    Main program loop for the checkbook application.
    
    Function Description:
    Provides a command-line interface for users to interact with their
    checkbook. Supports deposit, withdraw, balance check, and exit operations.
    Includes error handling for invalid commands and numeric inputs.
    
    Parameters:
    None
    
    Returns:
    None: Runs until user chooses to exit.
    """
    cb = Checkbook()
    print("Welcome to your Checkbook Manager!")
    print("Available commands: deposit, withdraw, balance, exit")
    
    while True:
        try:
            action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ").strip()
            
            if action.lower() == 'exit':
                print("Thank you for using Checkbook Manager. Goodbye!")
                break
            elif action.lower() == 'deposit':
                amount = get_positive_amount("Enter the amount to deposit: $")
                cb.deposit(amount)
            elif action.lower() == 'withdraw':
                amount = get_positive_amount("Enter the amount to withdraw: $")
                cb.withdraw(amount)
            elif action.lower() == 'balance':
                cb.get_balance()
            else:
                print("Invalid command. Please try again.")
                print("Available commands: deposit, withdraw, balance, exit")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()
