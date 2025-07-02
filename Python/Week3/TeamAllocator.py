#this program will allocate teams randomly from a list of names
#1.import the random module
#2.create a list of every genius
#3.Use random to randomly shuffle the list
#4.Loop through the list and display each team's players
#5.Use an if statement to see if the user is happy with the teams, if not shuffle again, if so, stop
import random

players = ["Avery", "Kauri", "Isaiah",
            "Braylen", "Taymur", "Xavier",
            "Taqari", "Kenlon", "Marshawn",
            "Nahum", "Kamari", "Kristopher", 
            "Joseph", "Darren", "Carl", 
            "Walter", "Jeffery", "Nishad",
            "Maximus", "Ja'Den", "Joaquin", 
            "Jarmauri", "Eustace", "Semaj" ]

def PickTeams(players):     #create our function
    random.shuffle(players) #shuffle the list of players
    team1 = players[:len(players) // 2]
    teamCaptain1 = team1[random.randrange(0,12)] #randomly assigns a team captain
    
    team2 = players[len(players) // 2:]
    teamCaptain2 = team2[random.randrange(0,12)]
    
    print("Team 1:")
    print("Team Captain: " + teamCaptain1)
    for player in team1:
        if player == teamCaptain1:
            continue
        print(player)
         
    print("")
    
    print("Team 2: ")
    print("Team Captain: " + teamCaptain2)
    for player in team2:
        if player == teamCaptain2:
            continue
        print(player)
          
PickTeams(players)