class Checkbook:
    def __init__(self):
        """
        Initializes a new Checkbook instance with a zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the checkbook.

        Parameters:
            amount (float): The amount to deposit.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the checkbook if funds are sufficient.

        Parameters:
            amount (float): The amount to withdraw.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Displays the current balance.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
