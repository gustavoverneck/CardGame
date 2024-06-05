# src/setup.py

from src.class_deck import Deck
from src.class_player import Player

class Game:
    def __init__(self, n_players):
        if n_players < 2:
            raise ValueError("The number of players must be at least 2")
        elif n_players > 4:
            raise ValueError("The number of players must be at most 4")
        else:
            self.n_players = n_players
            self.players = []
            self.current_player = 0
            self.cards_per_player = 8
            self.addPlayers()
        
    def addPlayers(self):
        for i in range(self.n_players):
            self.players.append(Player(i+1))
    
    def dealCards(self):
        for i in range(self.cards_per_player):
            for player in self.players:
                player.hand.append(self.deck.deck.pop())

    def startGame(self):
        print("Starting game...")
        self.deck = Deck()
        print("Setting deck up...")
        self.deck.addCards()
        self.deck.addCards()
        self.deck.shuffleCards()
        print("Dealing cards...")
        self.dealCards()
        self.winner = None
        print("Starting game!\n")
        while self.winner == None:
            self.current_player = 0
            for p in range(self.n_players):
                self.current_player = p
                print(f"\n It's player {self.current_player+1}'s turn.\n")
                self.players[self.current_player].showHand()
                self.playTurn(self.current_player)
    
    def playTurn(self, player_id):
        played = False
        self.deck.showTable()
        while not played:
            validPlay=False
            while not validPlay:
                print("What do you want to do?")
                play = int(input("Options:\n1: Buy from deck. 2: Pick from table.\n"))
                if (play == 1 and len(self.deck.deck) < 1):
                    print("There are no cards on the deck. Please take from the table.")
                    play = 2
                if (play == 2 and len(self.deck.table) < 1):
                    print("There are no cards on the table. Please take from the deck.")
                    play = 1
                if play == 1 or play == 2:
                    validPlay = True

            if play == 1:      
                self.players[player_id].hand.append(self.deck.deck.pop())
            elif play == 2:
                #self.deck.showTable()
                while True:
                    cardid_to_pick = int(input("Choose a card:"))
                    if cardid_to_pick < 1 or cardid_to_pick > len(self.deck.table):
                        print("Invalid option. Please try again.")
                    else:
                        break
                self.players[player_id].hand.append(self.deck.table.pop(cardid_to_pick-1))
            else:
                print("Invalid option. Please try again.")
            played = True
        self.verifyWinner(player_id)
        if self.winner != None:
            exit()
        self.players[self.current_player].showHand()    # Show Hand
        discard = int(input("Which card do you want to discard? (1~9)\n"))-1
        while discard < 0 or discard > 8:
            discard = int(input("Invalid option. Please try again. (1~9)\n"))-1
        self.deck.table.append(self.players[player_id].hand.pop(discard))

    def verifyWinner(self, player_id):
        count = {color:0 for color in self.deck.colors}
        for card in self.players[player_id].hand:
            count.update({card.color: count[card.color]+1})
        total_with_three = 0
        for color in count:
            if count[color] == 3:
                total_with_three += 1
        if total_with_three == 3:
            self.winner = player_id
            print(f"Player {player_id+1} wins!")
            return