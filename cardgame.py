from random import randint

#Alex please add the comments
class Card:
    def __init__(self,data):
        self.idCard = data[0]
        self.num = data[1]
        self.suit = data[2]
        self.coast = data[3]
        self.status = data[4]

class GameBatch:
    def __init__(self):
        self.cardBatchDict = {}
        counter = 0
        for tps in "♥♦♣♠":
            coast = iter([2,3,4,11])
            for n in (1,2,3,4,5,6,7,8,9,10,'V','D','K','T'):
                counter += 1
                if str(n) in "VDKT":
                    self.cardBatchDict[counter] = Card([counter,n,tps,next(coast),True])
                else:
                    self.cardBatchDict[counter] = Card([counter,n,tps,n,True])

    def getCard(self):
        while True:
            rnd = randint(1,54)
            if self.cardBatchDict[rnd].status:
                self.cardBatchDict[rnd].status = False
                return  self.cardBatchDict[rnd]

    def printCard(self,obj):
        print (" _______\n|{}\t|\n|       |\n|       |\n|      {}|\n|_______|".format(obj.num,obj.suit))




if __name__ == '__main__':
    user = GameBatch()
    user.printCard(user.getCard())