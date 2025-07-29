import pgzrun
import time 
import random


GRID_WIDTH = 27 #game width in tiles OG WIDTH = 16
GRID_HEIGHT = 17 #game height in tiles OG HEIGHT = 12
GRID_SIZE = 50 # the size of each tile in pixels
GUARDMOVEINTERVAL = 0.22 #The interval at which each guard moves

WIDTH = GRID_WIDTH * GRID_SIZE # The width of a tile
HEIGHT = GRID_HEIGHT * GRID_SIZE # the height of a tile

MAP = [
    'WWWWWWWWWWWWWDWWWWWWWWWWWWW',            
    'W                         W',
    'W                         W',
    'W                         W',
    'W                         W',
    'W  GWWWWWWWW   WWWWWWWWG  W',
    'W                         W',
    'W WWWWWWWWWWWWWWWWWWWWWWW W',
    'W W                     W W',
    'W W                     W W',
    'WGW          K          WGW',
    'W W                     W W',
    'W W                     W W',
    'W W                     W W',
    'W WWWWWWWWWW   WWWWWWWWWW W',
    'WK           P           KW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWW',]


#OG MAP =[
#    'WWWWWWWWDWWWWWWW',
#    'W              W',
#    'W       K      W',
#    'W       G      W',
#    'WG  WWWWWWWW  GW',
#    'W              W',
#    'W       K      W',
#    'W   WWWWWWWW   W',
#    'W              W',
#    'W              W',
#    'W      P       W',
#    'WWWWWWWWWWWWWWWW',
#]
#Converts grid position to screen coordinates
def GetScreenCoords(x, y):
    return(x * GRID_SIZE, y * GRID_SIZE)

#This draws the floor as a background
def DrawBackground():
    for y in range (GRID_HEIGHT): #loops through each row
        for x in range(GRID_WIDTH): #loops through each column
            screen.blit("floor1", GetScreenCoords(x, y)) #Draws the image at the given position

def SetupGame():
    global player #define player as global
    global keysToCollect #A variable to to store the keys that the player must collect
    global gameOver 
    global guards
    player = Actor("player", anchor=("left", "top")) #Create an actor for any moving objects player
    keysToCollect = []
    guards = []
    gameOver = False
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]#Gets the character from the MAP var
            if square == 'P':
                player.pos = GetScreenCoords(x, y)
            elif square == 'K':
                #Create actor for the key
                key = Actor("key", anchor=("left","top"))
                #Set key pos to this space
                key.pos = GetScreenCoords(x, y)
                #Add key to list
                keysToCollect.append(key)
            elif square == 'G':
                #Create actor for the guard
                guard = Actor("guard", anchor=("left","top"), pos = GetScreenCoords(x, y))
                #Add guard to list
                guards.append(guard)

#Draw walls
def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "W":
                screen.blit("wall", GetScreenCoords(x, y))
            elif square == "D":
                screen.blit("door", GetScreenCoords(x, y))

def GetActorGridPos(actor): #gets the actor as an argument and finds its position on the grid
    return (round(actor.x/GRID_SIZE)), (round(actor.y/GRID_SIZE)) #divides pixel coords by grid conversion number

def DrawActors():#Draw entities
    player.draw()
    for key in keysToCollect:
        key.draw()
    for guard in guards:
        guard.draw()

def draw(): #Draws everything USE 'draw', not 'Draw', 'draw' is built in
    screen.clear()
    DrawBackground()
    DrawScenery()
    DrawActors()
    if gameOver:
        DrawGameOver()

def MovePlayer(dx, dy):
    global gameOver
    if gameOver: #if the game is over
        #stop the player from moving by breaking the function
        return
    (x, y) = GetActorGridPos(player) #gets the player position
    x += dx #adds the inputted move to the current coords
    y += dy #adds the inputted move to the current coords
    square = MAP[y][x]#Makes sure the player doesn't go through a wall/door
    if square == "W": # if the player tries to move into a wall, don't let the player through
        return
    elif square == "D": # if the list of keys left to collect, there are keys left to collect, don't let the player through.
        if  len(keysToCollect) > 0:
            return
        else:
            gameOver = True
    for key in keysToCollect:
        (keyX, keyY) = GetActorGridPos(key)#get the grid position of the current key
        if x ==keyX and y == keyY: #Checks if the player is touching the key
            keysToCollect.remove(key)
            break
    player.pos = GetScreenCoords(x,y) #Prints the player at their new coordinate

def on_key_down(key):
    dir = ''
    if key == keys.LEFT:
        MovePlayer(-1, 0)
    elif key == keys.UP:
        MovePlayer(0, -1)
    elif key == keys.RIGHT:
        MovePlayer(1, 0)
    elif key == keys.DOWN:
        MovePlayer(0, 1)

def DrawGameOver():
    #Calculate and store the middle pos of the screen
    screenMiddle = (WIDTH/2, HEIGHT/2)
    #Draw game over
    screen.draw.text("Game Over", midbottom = screenMiddle, fontsize = GRID_SIZE*2, color="cyan", owidth=1)

def MoveGuard(guard):
    global gameOver
    if gameOver:
        return
    
    (playerX, playerY) = GetActorGridPos(player)#Get the positions of the guard and player.
    (guardX, guardY) = GetActorGridPos(guard)
    
    #Check which direction the player is, and if there is a wall in the way
    if playerX > guardX and MAP[guardY][guardX+1] != 'W':
        guardX += 1
    if playerX < guardX and MAP[guardY][guardX-1] != 'W':
        guardX -= 1
    if playerY > guardY and MAP[guardY+1][guardX] != 'W':
        guardY += 1
    if playerY < guardY and MAP[guardY-1][guardX] != 'W':
        guardY -= 1
    #update the guard position on screen
    guard.pos = GetScreenCoords(guardX, guardY)
    #Check if the guard and player are in the same position
    if guardX == playerX and guardY == playerY:
        gameOver = True

def MoveGuards():
    global GUARDMOVEINTERVAL
    
    for guard in guards:
        staggerchance = random.randrange(1, 16)
        if staggerchance == 1:
            return

        MoveGuard(guard)
        
       
        


SetupGame()
pgzrun.go()
clock.schedule_interval(MoveGuards, GUARDMOVEINTERVAL)
pgzrun.go()