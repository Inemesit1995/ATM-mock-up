class Budget:
    """A simple model of a budget."""
    def __init__(self, food = 500, clothing = 500, entertainment = 500):
        """Initialize attributes of the budget."""
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"I am putting on a {self.clothing.title()} to see a movie about the Rwandan genocide, called {self.entertainment.title()}.\n"
        long_name += f"When i return, i will eat {self.food.title()}."
        return long_name

    def deposit(self):
        """Deposit funds to each of the categories."""
        print("\nPlease deposit money for food, clothing and entertainment.\n")

        deposit_amount = int(input("Enter amount: \n"))
        print(f"You have deposited {deposit_amount} for food, clothing and entertainment.")

    def withdraw(self):
        """Withdraw funds from each of the categories."""

    def balance(self):
        """Compute balance of each category."""

    def transfer(self):
        """transfer balance between categories."""


#instance of the class
my_budget = Budget("rice", "suit", "sometimes in April")
print(my_budget.get_descriptive_name())
my_budget.deposit()
