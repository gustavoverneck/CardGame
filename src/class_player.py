# src/players.py


class Player:
    def __init__(self, id: str):
        self.id = id
        self.hand = []
    
    def showHand(self):
        print(f"\nPlayer {self.id} hand:")
        c = 1
        for card in self.hand:
            print(f"\nCard {c}: {card}")
            c += 1
        print("-----")
    
    def __str__(self) -> str:
        return f"Player {self.id}"