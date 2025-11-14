import random
import json
cards = open("./movies.json", encoding="utf8")
data = json.load(cards)

class owner():
    def __init__(self, name, money, inventory, xp, lvl):
        self.name = name
        self.money = money 
        self.inventory = inventory
        self.xp = xp
        self.lvl = lvl
    
    def blackjack(self):
        player = [] 
        dealer = []
        playertotal = []
        dealertotal = []
        playerhitstand = ""
        dealerhitstand = ""

        deck = []
        for i in cards:
            deck.append(i["rank"])
        random.shuffle(deck)
        player.append(deck[0])
        deck.pop(0)
        player.append(deck[0])
        deck.pop(0)
        dealer.append(deck[0])
        deck.pop(0)
        dealer.append(deck[0])
        deck.pop(0)

        playerhitstand = input("Do you wish to hit or stand?")

        if playerhitstand == "Hit" or playerhitstand == "hit":
            