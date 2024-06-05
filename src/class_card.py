# src/cards.py

class Card:
    def __init__(self, id: int, color: str, type: str):
        self.id = id
        self.color = color
        self.type = type

    def __str__(self):
        return f"id={self.id}, color={self.color},type={self.type}"

    