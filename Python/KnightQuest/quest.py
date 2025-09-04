import pgzrun
import time 
import random
img2 = False
level = 0
staggerchance = 1
GRID_WIDTH = 27 #game width in tiles OG WIDTH = 16
GRID_HEIGHT = 17 #game height in tiles OG HEIGHT = 12
GRID_SIZE = 50 # the size of each tile in pixels
GUARDMOVEINTERVAL = 0.25 #The interval at which each guard moves
PLAYERMOVEINTERVAL = 0.001

WIDTH = GRID_WIDTH * GRID_SIZE # The width of a tile
HEIGHT = GRID_HEIGHT * GRID_SIZE # the height of a tile
BACKGROUND_SEED = 12345
MAPS = [
    
     [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWW',            
    'W                      !!!W',
    'W!!                      !!',
    'W!!!!                     !',
    'W!!!                      !',
    'W            K            W',
    'WG?         W?W         ?GW',
    'W??         W W         ??W',
    'W           ! !           W',
    'W           ! !           W',
    'W           ! !B          W',
    'WWWWWWWWWWW ! !WWWWWWWWWWWW',
    'W           ! !           W',
    'W           ! !           W',
    'W           ! !           W',
    'W K          P          K W',
    'WWWWWWWWWWWWWDWWWWWWWWWWWWW',],
    [
    'WWWWWWWWWWWWWDWWWWWWWWWWWWW',            
    'W                      G  W',
    'W                         W',
    'W                         W',
    'W              G          W',
    'W  G                      W',
    'W                  ???K   W',
    'W                  ?      W',
    'W                  ?  ?   W',
    'W  K???????????????????   W',
    'W             ?           W',
    'W     G       ?           W',
    'W      G      ?       G   W',
    'W            ?P??         W',
    'W       G    ???          W',
    'W  G         ????????????KW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWW',],

    [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWW',            
    'W        ?       K        W',
    'W        ?                W',
    'W !!!!!!!!WWWD!!!!!!!!!!!!W',
    'W   B               !!!!!!W',
    'W                        !W',
    'W!!!!!                !!!!W',
    'W!!!!!!!!!!!   !!!!!!!!!!!W',
    'W!!!!    ?????????????????W',
    'W!!!!!!!!!!!!!!!!!!!      W',
    'W            B            W',
    'W????????????          !!!W',
    'W      !!!!!!!!!!!!!!!!!!!W',
    'W             P          KW',
    'W          ???????????????W',
    'W             G           W',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWW',],
    [
    'WWWWWWWWWWWWWDWWWWWWWWWWWWW',            
    'WWWWWWWWWWWW   WWWWWWWWWWWW',
    'W                         W',
    'W  ?????????????????????  W',
    'W  ?                   ?  W',
    'W W?                   ?W W',
    'W  ?                   ?  W',
    'WW ?                   ? WW',
    'W  ?                   ?  W',
    'WKG?                   ?GKW',
    'WWWWWWWWWWWWW WWWWWWWWWWWWW',
    'W                         W',
    'W                         W',
    'W                         W',
    'W                         W',
    'W            P            W',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWW',],
[
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
    'W W        ?   ?        W W',
    'W W?????????   ?????????W W',
    'W WWWWWWWWWW   WWWWWWWWWW W',
    'WK           P           KW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWW',],
    [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWW',            
    'WP  WK                    W',
    'W   W   WWWWWWWW          W',
    'W ??W   WK     ?          W',
    'W   WW  W      ?          W',
    'W  WGW  W      ?          W',
    'W  W W  W      ?          W',
    'W       W WWWWW?          W',
    'W  W    W     G?  B       W',
    'WWWWWWWWWWWWWWWWWWWWWWW   W',
    'WG?                   WWW W',
    'WG? ?                   G W',
    'WG? ?                  WWWW',
    'WG? ?                     W',
    'WG? ?                     W',
    'WK  ?                     D',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWW',],
    [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWW',            
    'WP                        W',
    'W                         W',
    'W?????????????????????????W',
    'W?                   G K  W',
    'W?????????????????????????W',
    'W      K            ?    GW',
    'W?????????????????????????W',
    'W               B         W',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WG       W                W',
    'WG       W                W',
    'WG       W                W',
    'WG      BWB               W',
    'W????????W                W',
    'WK       W                D',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWW',],

]
MAP = MAPS[level]


    
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
    random.seed(BACKGROUND_SEED)
    for y in range (GRID_HEIGHT): #loops through each row
        for x in range(GRID_WIDTH): #loops through each column
            if x % 2 == y % 2:
                screen.blit("floor1_grayscale", GetScreenCoords(x, y)) #Draws the image at the given position
            else:
                screen.blit("floor2_grayscale", GetScreenCoords(x, y)) #Draws the image at the given position


def SetupGame():
    global player #define player as global
    global keysToCollect #A variable to to store the keys that the player must collect
    global gameOver 
    global guards
    global playerWon
    global MAP
    global level


    player = Actor("player1", anchor=("left", "top")) #Create an actor for any moving objects player
    keysToCollect = []
    guards = []
    gameOver = False
    playerWon = False
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
            n = random.randint(0, 99) #Chooses a number between 0 and 99
            if square == "W":
                screen.blit("wall", GetScreenCoords(x, y))
                if n < 7:
                    screen.blit('crack1', GetScreenCoords(x, y))
                elif n < 15:
                    screen.blit('crack2', GetScreenCoords(x, y))
            elif square == "D":
                screen.blit("door", GetScreenCoords(x, y))
            elif square == "?":
                screen.blit("gonly_wall", GetScreenCoords(x, y))
            elif square == "!":
                screen.blit("hole", GetScreenCoords(x, y))
            elif square == "B":
                screen.blit("bpad", GetScreenCoords(x, y))

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
    global playerWon
    global img2

    if gameOver: #if the game is over
        #stop the player from moving by breaking the function
        return
    (x, y) = GetActorGridPos(player) #gets the player position
    if MAP[y][x] == 'B':
        x += dx*2 #adds the inputted move to the current coords
        y += dy*2 #adds the inputted move to the current coords
    else:
        x += dx #adds the inputted move to the current coords
        y += dy #adds the inputted move to the current coords
    square = MAP[y][x]#Makes sure the player doesn't go through a wall/door
    if square == "W": # if the player tries to move into a wall, don't let the player through
        return
    elif square == "!":
        return
    elif square == "D": # if the list of keys left to collect, there are keys left to collect, don't let the player through.
        if  len(keysToCollect) > 0:
            return
        else:
            gameOver = True
            playerWon = True
    for key in keysToCollect:
        (keyX, keyY) = GetActorGridPos(key)#get the grid position of the current key
        if x ==keyX and y == keyY: #Checks if the player is touching the key
            keysToCollect.remove(key)
            break
        #animate(player, pos=GetScreenCoords(x,y), duration=PLAYERMOVEINTERVAL/5)
    player.pos = GetScreenCoords(x,y) #Prints the player at their new coordinate
    

def on_key_down(key):
    global player
    global MAP
    global level
    if key == keys.SPACE and gameOver:#restart the game
        if not playerWon:
            SetupGame()
        else:
            level += 1
            MAP = MAPS[level]
            DrawScenery()
            DrawActors()
            SetupGame()
            
    if key == keys.LEFT:
        MovePlayer(-1, 0)
        player.image = 'player3'
    elif key == keys.UP:
        MovePlayer(0, -1)
        player.image = 'player2'
    elif key == keys.RIGHT:
        MovePlayer(1, 0)
        player.image = 'player4'
    elif key == keys.DOWN:
        MovePlayer(0, 1)
        player.image = 'player1'

def DrawGameOver():
    #Calculate and store the middle pos of the screen
    screenMiddle = (WIDTH/2, HEIGHT/2)
    #Draw game over
    if playerWon:
        screen.draw.text("YOU WIN", midbottom = screenMiddle, fontsize = GRID_SIZE*2, color="green", owidth=1)
        screen.draw.text("continue?", midtop = screenMiddle, fontsize = GRID_SIZE*2, color="white", owidth=1)
    else:
        screen.draw.text("YOU LOSE", midbottom = screenMiddle, fontsize = GRID_SIZE*2, color="red", owidth=1)
        screen.draw.text("try again?", midtop = screenMiddle, fontsize = GRID_SIZE*2, color="white", owidth=1)
def MoveGuard(guard):
    global gameOver
    if gameOver:
        return
    
    (playerX, playerY) = GetActorGridPos(player)#Get the positions of the guard and player.
    (guardX, guardY) = GetActorGridPos(guard)
    
    #Check which direction the player is, and if there is a wall in the way
    if playerX > guardX and MAP[guardY][guardX+1] != 'W' and MAP[guardY][guardX+1] != '?':
        guardX += 1
        guard.image = 'guard3'

    if playerX < guardX and MAP[guardY][guardX-1] != 'W' and MAP[guardY][guardX-1] != '?':
        guardX -= 1
        guard.image = 'guard2'
    if playerY > guardY and MAP[guardY+1][guardX] != 'W' and MAP[guardY+1][guardX] != '?':
        guardY += 1
        guard.image = 'guard'
    if playerY < guardY and MAP[guardY-1][guardX] != 'W' and MAP[guardY-1][guardX] != '?':
        guardY -= 1
        guard.image = 'guard1'


    
    #update the guard position on screen and animate him
    animate(guard, pos=GetScreenCoords(guardX, guardY), duration=GUARDMOVEINTERVAL/2)
    #guard.pos = GetScreenCoords(guardX, guardY)
    #Check if the guard and player are in the same position
    if guardX == playerX and guardY == playerY:
        gameOver = True

def MoveGuards():
    global GUARDMOVEINTERVAL
    gframe = 1
    for guard in guards:
        MoveGuard(guard)
        if gframe == 1:
            gframe = 0
            guard.image
        else:
            gframe = 1

        
        
       
        


SetupGame()
clock.schedule_interval(MoveGuards, GUARDMOVEINTERVAL)
pgzrun.go()