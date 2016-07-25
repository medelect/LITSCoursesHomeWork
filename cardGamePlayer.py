from cardgame import GameBatch
import os

class GamePlayer:
    def __init__(self,name, batch):
        self.batch = batch
        self.playerName = name
        self.playerSum = 0

    def play(self):
        print("ALL SUM", self.playerName ,"IS ", self.playerSum )
        ask = input("Do you want extra card press y/n " )
        if ask == 'y':
            obj = self.batch.getCard()
            self.batch.printCard(obj)
            self.playerSum += obj.coast
            return False
        elif ask == "n":
            return True

if __name__ == "__main__":
    user = GameBatch()
    party = [GamePlayer("Bob",user), GamePlayer("Mark", user), GamePlayer("Brad",user)]
    for item in party:
        while True:
            if item.playerSum < 22:
                if item.play():
                    break
            else:
                print(item.playerName, " you LOSE")
                break
    for item in party:
        print(item.playerName, " Have ", item.playerSum)
    print("Greating WINNER!!!")


#os.system('clear')