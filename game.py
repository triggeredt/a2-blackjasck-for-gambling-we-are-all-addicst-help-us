import random
import discord
from discord.ext  import commands
dic = {10 : '10' ,11 : 'Jack'  ,12  : 'Queen' ,13 : 'King' , 14 : 'A' ,9 : '9' ,8 : '8' ,7 : '7' ,6 : '6' ,5 : '5' ,4 : '4' ,3 : '3' ,2 : '2' }
dic2 = {0: 'Spades',1: 'Hearts',2: 'Diamonds',3: 'Clubs'}
deck = [[x for x in range(2,15)]for y in range (4)]
playerhands = []
playerlist = []
finaltotal = []
winners = []
Blackjacked = []
class Card :
    def __init__(self):
        self.suit = random.randint(0,3)
        self.number = random.choice(deck[self.suit])
        deck[self.suit].remove(self.number)
        #creates a full deck with suits

playernum = 5
player = 0


class game :
    
    def __init__(self):
        self.playernum = 0
        self.player = 0
        self.playerhands = [[]]*10
    


    def getplayernum (self,num):
        self.playernum = num
    #gets the number of players
    def dealcard(self,amount,player):
        x = 0
        for x in range (amount):
            temp = Card()
            self.playerhands[player].append(temp)
            x = x + 1
            return ''
    #deals any amount of cards 

    def printcard(self,player):
        for card in self.playerhands[player]:
            temp = str(dic[card.number]) + ' of ' + str(dic2[card.suit])
            return temp
        #converts the players hand into     
           
    def convertcards(self,player):
        return dic[playerhands[player]]
    #converts all the cards from object form to string
    def total(self,player):
        cards = []
        cards2 = []
        total = 0
        total2 = 0
        for c in self.playerhands[player]:
            cards.append(c.number)
            cards2.append(c.number)
        for c in range (len(self.playerhands[player])):
            if cards[c] < 14 and cards[c] > 10:
                cards[c] = 10
                cards2[c] = 10
            elif cards[c] == 14 :
                cards[c] = 11
                cards2[c] = 1
            total = cards[c] + total
            total2 = cards2[c] + total2
        if total < 22: 
            return total
        else:
            return total2
        if total == total2 :
            return total
        #makes sure that the dealers score is less than 21 even hen an ace is in play

    def gamefin(self):
        finalscore = []
        while self.total(playernum) < 17:
            self.dealcard(1, playernum)
        for c in range(playernum): 
            finalscore.append(self.total(c))
        winners = max(finalscore)
        for c in range(len(winners)):
            if self.total(winners[c]) == 21 and playerhands[winners[c]][0] == 'A':
                Blackjacked.append(winners[c])
            if self.total(winners[c]) == 21 and playerhands[winners[c]][1] == 'A':
                Blackjacked.append(winners[c])
        if not Blackjacked == None:
            return winners
        else: 
            return Blackjacked    



