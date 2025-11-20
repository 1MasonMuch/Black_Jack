import random
import json
cards = open("cards.json", encoding="utf8")
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
        
        print(player)
        print(dealer)
        
        while sum(playertotal) <= 21:
            playerhitstand = input("Do you wish to hit or stand?")
            if playerhitstand == "Yes" or playerhitstand == "yes":
                player.append(deck[0])
                deck.pop(0)
                for i in cards:
                    if i["rank"] in player:
                        playertotal.append(i["value"])
                    if sum(playertotal) > 21 and "Ace" in player:
                        for i in playertotal:
                            if i[playertotal] == 11:
                                i[playertotal]
