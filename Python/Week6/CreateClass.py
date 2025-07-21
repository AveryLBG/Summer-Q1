#1. Create a class to represent a video game or movie collection
#2. Create a constructor method __init__()
#3. Create a list for video games and movies each
#4. Create an instance variable for the user's favorite video game and movie
#5. Create the following function
#- A function to display the movies.
#- A function to display the video games.
#- A function to add something.
#- A function to remove something.
#- A function to display a favorite video game/movie.
#6. A file to test the function

class Collection:
    def __init__(self, movieList, gameList):
        self.movieList = []
        self.gameList = []


        self.movieList = movieList
        self.gameList = gameList
        self.favGame = ''
        self.favMovie = ''

    def setFavM(self, movie):
        if movie not in self.movieList:
            self.movieList.append(movie)
        self.favMovie = movie
    

    def setFavG(self, game):
        if game not in self.gameList:
            self.gameList.append(game)
        self.favGame = game

    def printMovies(self):
        for x in self.movieList:
            print(x)

    def printGames(self):
        for x in self.gameList:
            print(x)

    def printFavM(self):
            print(f'Fav Movie: {self.favMovie}')
        
    def printFavG(self):
        print(f'Fav Game: {self.favGame}')

    def addMovie(self, item):
        if item in self.movieList:
            print("Movie is already in the collecion.")
        else:
            self.movieList.append(item)

    def addGame(self, item):
        if item in self.movieList:
            print("Game is already in the collection.")
        else:
            self.gameList.append(item)

    def removeMovie(self, item):
        if item not in self.movieList:
            print("Movie Not Found")
        else:
            self.movieList.remove(item)

    def removeGame(self, item):
        if item not in self.gameList:
            print("Game Not Found")
        else:
            self.gameList.remove(item)
    def displayCollection(self):
        self.printGames()
        self.printFavG()
        self.printMovies()
        self.printFavM()
