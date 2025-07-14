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
backpack = {"Pencils", "Books", "Computer", "Charger", "Folder"}
for item in backpack:
    print(item)

print("Scenario 5: Look up Student emails by their names.")
print("A dicionary would be best, as names are paired with emails.")

emails = {
    "Avery": "avery.garner@wccschools.org",
    "Camryn": "camryn.garner@wccschools.org",
    "Lucas": "lucas.atalkiti@wccschools.org"
}
for name, email in emails.items():
    print(name, ": ", email )

print("Scenario 6: A shopping cart of groceries.")
print("A set would work, the items are in no particular order.")
cart = {"Milk", "Eggs", "Bacon", "Salt"}
for item in cart:
    print(item)

print("Scenario 7: Tickets in a hat for a raffle.")
print("A set is best, since there is no indexing you can't rig it as easily")

hat = {"Avery", "Kauri", "Marshawn", "Semaj", "Jeffrey", "Joaquin", "Cyrus"}
for person in hat:
    print(person)



