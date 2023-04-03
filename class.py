class game():
    def __init__(self):
        self.__game = 1
    def printingscore(self):
        print(self.__game)
    def updatingscore(self):
        self.__game = self.__game+1
        print(self.__game)
        
player = game()
player.game = 20
player.updatingscore()
