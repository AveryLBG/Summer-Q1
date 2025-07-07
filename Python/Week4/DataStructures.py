#create a list of 5 of your favorite snacks
#create a tuple of 5 colleges you want to attend
#create a set of 5 of whatever you want
#Create a dictionary on a car's attributes

#Change mutable data types
#print data

favSnacks = ["Doritos", "Granola Bars", "Swedish Fish", "Fruit Snacks", "Grapes"]
plannedColleges = ("UCLA", "UC Davis", "UC Santa Cruz", "CIT", "UC Berkeley")
peakGames = {"Ultrakill", "Rain World", "Roblox", "Minecraft", "Celeste"}
carAttributes = {"brand": "Toyota",
                 "model": "Corrola",
                 "year": 2020,
                 "Engine": "4-Cylinder",
                 "WheelSize": "18in"}
carAttributes["color"] = "Blue"
carAttributes.update({"year" : 2023})
peakGames.add("Terraria")
favSnacks[1] = "Lays BBQ Chips"





for snack in favSnacks:
    print(snack)
print()

for college in plannedColleges:
    print(college)
print()

for attribute in carAttributes:
    print(carAttributes.get(attribute))
print()

for game in peakGames:
    print(game)
print()