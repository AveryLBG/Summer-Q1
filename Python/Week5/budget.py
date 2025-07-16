#Convert a program into a class
#1. Define the class
#2.Create __init__()
#Create instance variable
#Refactor code into a class
class BudgetManager:
    def __init__(self, amount): #Self is so that methods/attributes in objects know which object they're in so they dont get mixed up with other objects
            #amount is the amount of funds the object will start with
            #the amount of money we have to spend
            #Cake metaphor: object = cake, class = recipe, self = label 
            self.funds = amount
        #dictionary of items we are spending budget of
        #the key is the name, the value is the budget amount spent
            self.budgets = {}
        #a dictionary of the expense of each budgeted item
        #the key is the name, the value is the  amount spent
            self.expenses = {}

   



    #Adds an item to the budget dictionary
    def AddBudget(self, name, amount):
        if name in self.budgets: #stops repeat items
            raise ValueError("Budget for item already exists.")
        if amount > self.funds:
            raise ValueError("No can do brochacho, you're too broke.")
        self.budgets[name] = amount #Adds the item
        fundsn = self.funds - amount #Subtracts amount from funds and sets funds to that value
        self.expenses[name] = 0 #Adds the budgeted item to the expenses dictionary
        return self.funds

    def Spend(self, name, amount):
        if name not in self.expenses: #if the item isnt in the budger
            raise ValueError("Item not in budget")
        self.expenses[name] += amount #Adds the expense to the budgeted item
        budgeted = self.budgets[name]
        spent = self.expenses[name]
        return budgeted - spent

    def PrintBudget(self):
        print("Budget               Budgeted      Spent    Remaining")
        print("----------------------------------------------------------------")
        totalBudgeted = 0
        totalSpent = 0
        totalRemaining = 0
        for name in self.budgets:
            budgeted = self.budgets[name]#calculate the amount budgeted
            spent = self.expenses[name]#calculate the amount spent
            remainingBudget = budgeted - spent #calculate the difference between the two.
            print(f'{name:15s},  {budgeted:10.2f}, {spent:10.2f}, {remainingBudget:10.2f}')
            totalBudgeted += budgeted
            totalSpent += spent
            totalRemaining = remainingBudget

        print(f'{"Total":15s},  {totalBudgeted:10.2f}, {totalSpent:10.2f}, {totalBudgeted - totalSpent:10.2f}')
        

    
