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
	counter = 0
	for tps in "♥♦♣♠":
	    counter += 1
	    coast = iter([2,3,4,11])
	    for n in (1,2,3,4,5,6,7,8,9,10,'V','D','K','T'):
		if str(n) in "VDKT":
		    self.cardBatch.append(Card([counter,n,tps,next(coast),True]))
		else:
		    self.cardBatch.append(Card([counter,n,tps,n,False]))


    def getCard(self):
	while True:
	    rand = randint(1,54)
	    for objCard in self.cardBatch:	#simple choose in key of dict
		if objCard.status:
		    objCard.status = False
		    #return objCard
		    print(" ____\n|",objCard.num,"\t|\n|    |\n|   ",objCard.suit,"|\n|____|")

    def printCard(self,printedCard):
	print(" ____\n|",printedCard.num,"\t|\n|    |\n|   ",printedCard.suit,"|\n|____|")



user = GameBatch()
user.getCard()