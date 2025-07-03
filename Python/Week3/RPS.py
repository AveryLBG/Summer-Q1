#Build a rock paper scissors game
#2 Players
#Each player pick rock, paper, or scissors
#Rock > Scissors
#Scissors > Paper
#Paper > Rock

#0. Prompt players for their names
#1. Prompt player 1 for rock paper or scissors
#2. Prompt player 2 for rock paper or scissors
#3. Compare their choices.

#FIXES:
#Check for valid responses
#Hide player input
#Refactor code
def RPS():

    #Get player names
    player1 = input("Welcome to RPS, Player 1, please enter your name.")
    player2 = input ("Welcome to RPS, Player 2, please enter your name.")

    #Get player choices
    p1_Choice = input(f"{player1}, choose rock, paper, or scissors.").lower()

    while not IsValidMove(p1_Choice):
        print("Invalid move, try again")
        p1_Choice = input(f"{player1}, choose rock, paper, or scissors.").lower()

    p2_Choice = input(f"{player2}, choose rock, paper, or scissors.").lower()
    
    while not IsValidMove(p2_Choice):
        print("Invalid move, try again")
        p2_Choice = input(f"{player2}, choose rock, paper, or scissors.").lower()



    #compare player moves
    if  p1_Choice == p2_Choice:
        print("It's a draw!")
    elif p1_Choice == "rock" and p2_Choice == "scissors":
        print(f"Rock beats scissors, {player1} wins")
    elif p1_Choice == "paper" and p2_Choice == "rock":
        print(f"Paper beats rock, {player1} wins")
    elif p1_Choice == "scissors" and p2_Choice == "paper":
        print(f"Scissors beats paper, {player1} wins")
    
    elif p1_Choice == "scissors" and p2_Choice == "rock":
        print(f"Rock beats scissors, {player2} wins")
    elif p1_Choice == "rock" and p2_Choice == "paper":
        print(f"Paper beats rock, {player2} wins")
    elif p1_Choice == "paper" and p2_Choice == "scissors":
        print(f"Scissors beats paper, {player2} wins")


def IsValidMove(playerMove):
    validMoves = ["rock", "paper", "scissors"]
    if playerMove in validMoves:
        return True
    else:
        return False



RPS()