from cardgame import GameBatch
import os

class GamePlayer:
    def __init__(self):
        self.playerName
        self.playerSum

if __name__ == "__main__":
    user = GameBatch()
    sumCoins = 0 
    obj = user.getCard()
    user.printCard(obj)
    sumCoins += obj.coast
    print("ALL SUM IS ", sumCoins )
    ask = input("Do you whant extra card press y/n")
    if ask == 'y':
        obj = user.getCard()
        user.printCard(obj)
        sumCoins += obj.coast
    print("ALL SUM IS ", sumCoins )
    ask = input("Do you whant extra card press y/n")
    if ask == 'y':
        obj = user.getCard()
        user.printCard(obj)
        sumCoins += obj.coast
    print("ALL SUM IS ", sumCoins )
    ask = input("Do you whant extra card press y/n")
    if ask == 'y':
        obj = user.getCard()
        user.printCard(obj)
        sumCoins += obj.coast
    print("ALL SUM IS ", sumCoins )
    ask = input("Do you whant extra card press y/n")
    if ask == 'y':
        obj = user.getCard()
        user.printCard(obj)
        sumCoins += obj.coast
    print("ALL SUM IS ", sumCoins )






#os.system('clear')