import pgzrun


GRID_WIDTH = 28 #game width in tiles OG WIDTH = 16
GRID_HEIGHT = 17 #game height in tiles OG HEIGHT = 12
GRID_SIZE = 50 # the size of each tile in pixels

WIDTH = GRID_WIDTH * GRID_SIZE # The width of a tile
HEIGHT = GRID_HEIGHT * GRID_SIZE # the height of a tile

MAP = [  
    'WWWWWWWWWWWWWWDWWWWWWWWWWWWW',            
    'W                          W',
    'W                          W',
    'W                          W',
    'W    WWWWWWWW K WWWWWWWW   W',
    'W                          W',
    'W    G                 G   W',
    'W    WWWWWWWWWWWWWWWWWWW   W',
    'W                          W',
    'W                          W',
    'W                          W',
    'W                          W',
    'W                          W',
    'W                          W',
    'W          W    W          W',
    'W       G  W  P W  G       W',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWW',]


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
    player = Actor("player", anchor=("left", "top")) #Create an actor (moving object), and set its anchor (idk)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]#Gets the character from the MAP var
            if square == 'P':
                player.pos = GetScreenCoords(x, y)

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

def draw(): #Draws everything USE 'draw', not 'Draw', 'draw' is built in
    screen.clear()
    DrawBackground()
    DrawScenery()
    DrawActors()

def MovePlayer(dx, dy):
    (x, y) = GetActorGridPos(player) #gets the player position
    x += dx #adds the inputted move to the current coords
    y += dy #adds the inputted move to the current coords
    square = MAP[y][x]#Makes sure the player doesn't go through a wall/door
    if square == "W": 
        return
    elif square == "D":
        return
    player.pos = GetScreenCoords(x,y) #Prints the player at their new coordinate

def on_key_down(key):
    if key == keys.LEFT:
        MovePlayer(-1, 0)
    elif key == keys.UP:
        MovePlayer(0, -1)
    elif key == keys.RIGHT:
        MovePlayer(1, 0)
    elif key == keys.DOWN:
        MovePlayer(0, 1)

SetupGame()
pgzrun.go()