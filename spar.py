from constants import SUITS, RANKS
import random

class Spar:
    def __init__(self):
        self.deck_of_cards = []
        self.players = []

    def shuffle_deck(self):
        self.deck_of_cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck_of_cards.append((suit, rank))
        random.shuffle(self.deck_of_cards)
    
    def __repr__(self):
        if len(self.deck_of_cards) == 0:
            raise Exception("No cards")
        str = ""
        for i in range(0, len(self.deck_of_cards)):
            card = self.deck_of_cards[i]
            str += f"{i+1}. {card[0]} of {card[1]}\n"
        return str
        