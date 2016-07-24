#  #!/usr/bin/python3
from random import randint

class Card:

    def __init__(self,data):
        self.idCard = data[0]
        self.num = data[1]
        self.suit = data[2]
        self.coast = data[3]
        self.status = data[4]

class GameBatch:

    def __init__(self):
        self.cardBatch = []		#change in dict type
        self.cardBatchDict = {}
        counter = 0
        for tps in "♥♦♣♠":
            
            coast = iter([2,3,4,11])
            for n in (1,2,3,4,5,6,7,8,9,10,'V','D','K','T'):
                counter += 1
                if str(n) in "VDKT":
                    #self.cardBatch.append(Card([counter,n,tps,next(coast),True]))
                    self.cardBatchDict[counter] = Card([counter,n,tps,next(coast),True])
                else:
                    #self.cardBatch.append(Card([counter,n,tps,n,False]))
                    self.cardBatchDict[counter] = Card([counter,n,tps,n,True])


    def getCard(self):
        while True:
            rnd = randint(1,54)
            if self.cardBatchDict[rnd].status:
                self.cardBatchDict[rnd].status = False
#            for objCard in self.cardBatch:	#simple choose in key of dict
#                if objCard.status:
#                    objCard.status = False
#                    #return objCard
#                     print(" ____\n|",objCard.num,"\t|\n|    |\n|   ",objCard.suit,"|\n|____|")
                sT = " " # temp spaces amount
                if self.cardBatchDict[rnd].num == 10: sT = ""
                print(" ____\n|",self.cardBatchDict[rnd].num,sT,"|\n|    |\n| ",self.cardBatchDict[rnd].suit,"|\n|____|")
                break

    def printCard(self,printedCard):
        print(" ____\n|",printedCard.num,"\t|\n|    |\n|   ",printedCard.suit,"|\n|____|")




user = GameBatch()
user.getCard()