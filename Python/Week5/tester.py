import budget

myBudget = budget.BudgetManager(2500)
print("Total Funds: ", myBudget.funds)
#Add items to the budget

myBudget.AddBudget("Books", 100)
myBudget.AddBudget("Rent", 800)
myBudget.AddBudget("Car note", 200)
#Spend money on the items in our budget

myBudget.Spend("Books", 20)
myBudget.Spend("Rent", 800)
myBudget.Spend("Car note", 200)

#This one is self explanitory. If you can't figure out what it does it's just over for you atp.
myBudget.PrintBudget()
