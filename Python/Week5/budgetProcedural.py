#the amount of money we have to spend
funds = 2500
#dictionary of items we are spending budget of
#the key is the name, the value is the budget amount spent
budgets = {}
#a dictionary of the expense of each budgeted item
#the key is the name, the value is the  amount spent
expenses = {}

#Adds an item to the budget dictionary
def AddBudget(name, amount):
    global funds
    if name in budgets: #stops repeat items
        raise ValueError("Budget for item already exists.")
    if amount > funds:
        raise ValueError("No can do brochacho, you're too broke.")
    budgets[name] = amount #Adds the item
    funds = funds - amount #Subtracts amount from funds and sets funds to that value
    expenses[name] = 0 #Adds the budgeted item to the expenses dictionary
    return funds

def Spend(name, amount):
    if name not in expenses: #if the item isnt in the budger
        raise ValueError("Item not in budget")
    expenses[name] += amount #Adds the expense to the budgeted item
    budgeted = budgets[name]
    spent = expenses[name]
    return budgeted - spent

def PrintBudget():
    print("Budget               Budgeted      Spent    Remaining")
    print("----------------------------------------------------------------")
    totalBudgeted = 0
    totalSpent = 0
    totalRemaining = 0
    for name in budgets:
        budgeted = budgets[name]#calculate the amount budgeted
        spent = expenses[name]#calculate the amount spent
        remainingBudget = budgeted - spent #calculate the difference between the two.
        print(f'{name:15s},  {budgeted:10.2f}, {spent:10.2f}, {remainingBudget:10.2f}')
        totalBudgeted += budgeted
        totalSpent += spent
        totalRemaining = remainingBudget

    print(f'{"Total":15s},  {totalBudgeted:10.2f}, {totalSpent:10.2f}, {totalBudgeted - totalSpent:10.2f}')


print("Total Funds: ", funds)
#Add items to the budget

AddBudget("Books", 100)
AddBudget("Rent", 800)
AddBudget("Car note", 200)
#Spend money on the items in our budget

Spend("Books", 20)
Spend("Rent", 800)
Spend("Car note", 200)

#This one is self explanitory. If you can't figure out what it does it's just over for you atp.
PrintBudget()
