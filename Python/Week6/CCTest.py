import CreateClass

c = CreateClass.Collection(['The Mario Movie', 'The Lion King', 'Aladdin', 'Spider-Man: Into The Spider-Verse'], ['Ultrakill', 'Rain World', 'Minecraft', 'PEAK'])
c.setFavM('Spider-Man: Across The Spider-Verse')
c.removeMovie('The Mario Movie')
c.addMovie('A Minecraft Movie')
c.addMovie('A Minecraft Movie')



c.setFavG('Rain World')
c.removeGame('PEAK')
c.addGame('Your Only Move is HUSTLE')
c.removeGame('Celeste')

c.displayCollection()
