from random import randint

#Alex please add the comments
class Card:				#class-collection for data about one card
    def __init__(self,data):		#hi's havent any methods as u can see
        self.idCard = data[0]
        self.num = data[1]
        self.suit = data[2]
        self.coast = data[3]
        self.status = data[4]

class GameBatch:
    def __init__(self):			# Constructor as u know ,created dict vs all cards,   hi's haven't mention for class user	
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

    def getCard(self):			# first needed methosd hi's run get u one card from batch object wich was unusable before
        while True:
            rnd = randint(1,54)
            if self.cardBatchDict[rnd].status:
                self.cardBatchDict[rnd].status = False
                return  self.cardBatchDict[rnd]

    def printCard(self,obj):		# second needed method hi`s receive one object of card  and print it
        print (" _______\n|{}\t|\n|       |\n|       |\n|      {}|\n|_______|".format(obj.num,obj.suit))




if __name__ == '__main__':		#simple test
    user = GameBatch()			# we test both classes in this line when we cheate class container
    user.printCard(user.getCard())	# we use short version (when func use other func which get needed object) in this we line get card and print it