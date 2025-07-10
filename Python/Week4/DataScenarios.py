#Your task today is to identify what is the best data structure for each given scenario, and provide sample code that implements that logic.
#1. A restaurant menu with prices for each item


#2. High scores to an arcade game

#3. All of the months of the year

#4. All the items in your backpack

#5. Look up Student emails by their names

#6. A shopping cart of groceries 

#7. [Add a scenario of your own]
#Items are lists, tuples, dictionaries, and sets.

print("Scenario 1:  A restaurant menu with prices for each item")
print("The best data structure for this is a dictionary, as it can pair foods with prices.")
menu = {
    "French Toast":12,
    "Grand Slam":12,
    "Steak":18,
    "Avocado Toast":15
}
for key, item in menu.items():
    print( key, ": ", item)

print("Scenario 2: High scores to an arcade game.")
print("It must be mutable")
highScores = [
    105,
    100,
    130,
    123
]
highScores.sort()
highScores.reverse
for score in highScores:
    print(score)

print("Scenario 3:  All of the months of the year")
print("Tuples are best because they don't change.")
months = (
    'January',
    'February',
    'March',
    "April",
    'May',
    'June,',
    'July',
    'August',
    "September",
    "November",
    "December"
)
for month in months:
    print(month)

print("Scenario 4: All the items in your backpack")
print("A set would be best, the items are in no particular order")
backpack ={"Pencils", "Books", "Computer", "Charger", "Folder"}
for item in backpack:
    print(item)
prin


