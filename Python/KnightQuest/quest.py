import pgzrun


GRID_WIDTH = 16 #game width in tiles
GRID_HEIGHT = 12 #game height in tiles
GRID_SIZE = 50 # the size of each tile in pixels

WIDTH = GRID_WIDTH * GRID_SIZE # The width of a tile
HEIGHT = GRID_HEIGHT * GRID_SIZE # the height of a tile

MAP = [
    'WWWWWWWWDWWWWWWW',
    'W              W',
    'W       K      W',
    'W       G      W',
    'WG  WWWWWWWW  GW',
    'W              W',
    'W       K      W',
    'W   WWWWWWWW   W',
    'W              W',
    'W              W',
    'W      P       W',
    'WWWWWWWWWWWWWWWW',
]
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
    player = pgzrun.Actor("player", anchor=("left", "top")) #Create an actor (moving object), and set its anchor (idk)
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

def draw(): #Draws everything USE 'draw', not 'Draw', 'draw' is built in
    DrawBackground()
    DrawScenery()
    SetupGame()


pgzrun.go()