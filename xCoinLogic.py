'''
XternCoin Logic + Function Housing

XternCoin numbers can be between 0 and 10

- Trenton Spice
https://github.com/trentspi/ts-XternCoin.git
'''

from random import randint

class xCoin(object):
    def __init__(self):
        self.userID = '200169'
        self.userKeys = 0
        self.xRand = randint(0,10)


    def randNum(self):
        return randint(0,10)

    def HandleGuess(self, uid, guess):
        if uid == self.userID:
            if guess == self.xRand:
                self.userKeys += 1
                self.xRand = self.randNum()
                print("Correct guess!")
                print("guess:{a}, xRand:{b}".format(a = guess, b = self.xRand))
            else:
                print("Incorrect guess!")
                print("guess:{a}, xRand:{b}".format(a = guess, b = self.xRand))
        else:
            print("Invalid userID!")

    def GetCoins(self, userID):
        return self.userKeys

    def StartGuessing(self):
        for i in range(100):
            randGuess = randint(0,10)
            print("Guessing {} \n".format(randGuess))
            print(self.HandleGuess(self.userID, randGuess))
            print("Coins : " , self.GetCoins(self.userID))

def main ():
    c = xCoin()
    c.StartGuessing()


if __name__ == "__main__":
    main()
