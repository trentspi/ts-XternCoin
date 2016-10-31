'''
XternCoin Logic + Function Housing

XternCoin numbers can be between 0 and 10

Trenton Spice
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
        uid = str(uid)
        guess = int(guess)
        if uid == self.userID:
            if guess == self.xRand:
                self.userKeys += 1
                self.xRand = self.randNum()
                print("Correct Guess, +1 XternCoin!")
            else:
                print("Incorrect Guess")

    def GetCoins(self, userID):
        userID = str(userID)
        if userID == self.userID:
            return self.userKeys

    def StartGuessing(self):
        for i in range(100):
            randGuess = randint(0,10)
            print("\nGuessing...")
            self.HandleGuess(self.userID, randGuess)
            print("XternCoins : " + str(self.GetCoins(self.userID)))

def main():
    c = xCoin()
    c.StartGuessing()

if __name__ == "__main__":
    main()
