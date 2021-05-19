import random

class SnakesLadders():
    def __init__(self):
        self.won = False
        self.playOrder = 0
        self.playerOnePos = 0
        self.playerTwoPos = 0
        self.playersPos = [self.playerOnePos,self.playerTwoPos]

        self.ladders = {2:38,7:14,8:31,15:26,21:42,28:84,36:44,51:67,71:91,78:98,87:94}
        self.snakes = {16:6,46:25,49:11,62:19,64:60,74:53,89:68,92:88,95:75,99:80}

    def play(self,die1,die2):
        if self.won:
            return "Game over!"
            self.playerOnePos = 0
            self.playerTwoPos = 0
        elif self.playersPos[self.playOrder] + die1 + die2 > 100:
            self.playersPos[self.playOrder] += die1 + die2 - (100 - self.playersPos[self.playOrder])
            out = "Player " + str(self.playOrder+1) + " is on square " + str(self.playersPos[self.playOrder])
            self.reversePlayOrder(die1,die2)
            return out
        elif self.playersPos[self.playOrder] + die1 + die2 == 100:
            self.won = True
            out = "Player " + str(self.playerOrder+1) + " Wins!"
            self.reversePlayOrder(die1,die2)
            return out
        else:
            self.playersPos[self.playOrder] += (die1 + die2)
            if self.playersPos[self.playOrder] in self.ladders:
                self.playersPos[self.playOrder] = self.ladders[self.playersPos[self.playOrder]]
            elif self.playersPos[self.playOrder] in self.snakes:
                self.playersPos[self.playOrder] = self.snakes[self.playersPos[self.playOrder]]
            out = "Player " + str(self.playOrder+1) + " is on square " + str(self.playersPos[self.playOrder])
            self.reversePlayOrder(die1,die2)
            return out

    def reversePlayOrder(self,d1,d2):
        if d1 != d2:
            self.playOrder = (self.playOrder + 1) % 2