import random

# Challenge 2 - Deck of cards


class Card:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def show_card(self):
        return f'{self.name} {self.value}'


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


class Game:

    def __init__(self):

        self.starting_deck = Deck()
        self.score = 0

    def return_score(self):
        return f'Your score is: {self.score}'

    def add_score(self):
        self.score += 1
        return self.score

    def show_card_to_user(self):
        return self.starting_deck.pick_a_card().show_card()


def choice_feedback(first_card, second_card):
    first_card_value = int(first_card.split(' ')[-1])
    second_card_value = int(second_card.split(' ')[-1])
    if users_choice == 'lower':
        if first_card_value <= second_card_value:
            return False
        else:
            return True
    elif users_choice == 'higher':
        if first_card_value >= second_card_value:
            return False
        else:
            return True
    else:
        return 'You misspelled answer. It should be lower or higher'


# game beginning

print('''
Welcome to the game lower or higher
Let's begin!
''')
game_1 = Game()
first_card = game_1.show_card_to_user()
game_on = True

while game_on:
    users_choice = input(f'The card is: {first_card}\nNext gonna be higher or lower? ')
    users_choice = users_choice.lower()

    second_card = game_1.show_card_to_user()
    print(f'Next card is: {second_card}')

    feedback = choice_feedback(first_card, second_card)
    if feedback is False:
        print(f'You are wrong\n{game_1.return_score()}\nGame Over.')
        game_on = False
    elif feedback is True:
        game_1.add_score()
        print(f'You are right.\n{game_1.return_score()}')
    else:
        print(feedback)
        game_on = False

    first_card = second_card

