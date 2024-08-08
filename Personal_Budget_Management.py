class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__expenses = 0

    # Getter and setter for category name
    @property
    def category_name(self):
        return self.__category_name

    @category_name.setter
    def category_name(self, name):
        self.__category_name = name

    # Getter and setter for allocated budget
    @property
    def allocated_budget(self):
        return self.__allocated_budget

    @allocated_budget.setter
    def allocated_budget(self, budget):
        if budget < 0:
            raise ValueError("Budget should be a positive number")
        self.__allocated_budget = budget

    # Method to add an expense to the category
    def add_expense(self, amount):
        if amount < 0:
            raise ValueError("Expense amount should be a positive number")
        if amount > self.remaining_budget:
            raise ValueError("Expense amount exceeds the remaining budget")
        self.__expenses += amount

    # Property to calculate remaining budget
    @property
    def remaining_budget(self):
        return self.__allocated_budget - self.__expenses

    # Method to display the budget category details
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")
        print(f"Expenses: ${self.__expenses}")
        print(f"Remaining Budget: ${self.remaining_budget}")

# Example usage
food_category = BudgetCategory("Food", 500)
entertainment_category = BudgetCategory("Entertainment", 300)
utilities_category = BudgetCategory("Utilities", 200)
bills_category = BudgetCategory("Bills", 400)

# Adding expenses to categories
food_category.add_expense(100)
entertainment_category.add_expense(50)
utilities_category.add_expense(75)
bills_category.add_expense(200)

# Displaying summaries for each category
food_category.display_category_summary()
entertainment_category.display_category_summary()
utilities_category.display_category_summary()
bills_category.display_category_summary()
