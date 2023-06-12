import random

# Challenge 2 - Deck of cards


class Card:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def show_card(self):
        return f'{self.name}{self.value}'


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

        self.pack = []
        for i in suits:
            for j in range(2, 15):
                self.pack.append(Card(i, j))
        random.shuffle(self.pack)
        self.discarded = []

    def shuffle(self):
        return random.shuffle(self.pack)

    def pick_a_card(self):
        return self.pack.pop(0)
