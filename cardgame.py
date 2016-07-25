from random import randint

class Card:				            #class-collection for data about one card
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

    def getCard(self):			# first needed method hi's run get u one card from batch object which was unusable before
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

def welcome():
    print("Welccome to the game '21'\n")

#user and pc

#card values
def cardVal(user):
    cardVal = 0
    cardsTotal = 0
    cardNo = 0
    while cardNo < 2:
        card = user[cardNo][0]
        if card == "T":
            cardVal = 11
        elif card == "K":
            cardVal = 4
        elif card == "D":
            cardVal = 3
        elif card == "V":
            cardVal = 2
        elif card == "2":
            cardVal = 2
        elif card == "3":
            cardVal = 3
        elif card == "4":
            cardVal = 4
        elif card == "5":
            cardVal = 5
        elif card == "6":
            cardVal = 6
        elif card == "7":
            cardVal = 7
        elif card == "8":
            cardVal = 8
        elif card == "9":
            cardVal = 9
        else:
            cardVal = 10

        cardNo += 1
        cardsTotal = cardsTotal + cardVal

    return cardsTotal


welcome()

#deal cards to pc and user

#calculate

#print result

#exit game
print("Game Over!")