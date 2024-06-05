# src/deck.py

from src.class_card import Card
from sklearn.utils import shuffle

class Deck:
    def __init__(self) -> None:
        self.deck = []
        self.colors = ["blue", 
                       "red", 
                       "dark green", 
                       "yellow",
                       "orange",
                       "pink",
                       "purple",
                       "light green"
                       ]
        self.types = ["square",
                      "triangle",
                      "circle",
                      "pentagon"
                      ]
        self.table = []
    
    def addCards(self):
        ids = 0
        for color in self.colors:
            for type in self.types:
                ids += 1
                self.deck.append(Card(ids, color, type))
    
    def removeCard(self, card: Card) -> None:
        self.deck.index(card).pop()
    
    def shuffleCards(self) -> None:
        self.deck = shuffle(self.deck, random_state=1)
    
    def putOnTable(self, card: Card) -> None:
        self.table.append(card)
    
    def showTable(self):
        print("Table:")
        for card in self.table:
            print(f"\t{card}")
    
    def __str__(self) -> None:
        txt_to_print = ""
        for card in self.deck:
            txt_to_print = txt_to_print + f"{card}\n"
        return txt_to_print
    