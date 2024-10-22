from constants import SUITS, RANKS
from player import Player
import random

class Spar:
    def __init__(self):
        self.deck_of_cards = []
        self.players = []

        self.shuffle_deck()

    def shuffle_deck(self):
        self.deck_of_cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck_of_cards.append((suit, rank))
        random.shuffle(self.deck_of_cards)
    
    def deal_hands(self):
        for player in self.players:
            first_set = 3
            while first_set > 0:
                i = random.randint(0, len(self.deck_of_cards))
                player.add_card_to_hand(self.deck_of_cards.pop(i))
                first_set -= 1
            second_set = 2
            while second_set > 0:
                i = random.randint(0, len(self.deck_of_cards))
                player.add_card_to_hand(self.deck_of_cards.pop(i))
                second_set -= 1

    def play(self):
        print("WELCOME TO PYTHON SPAR")
        player_count = input("Enter number of players: ")
        for i in range(0, int(player_count)):
            name = input(f"Enter player {i+1} name: ")
            player = Player(name)
            self.players.append(player)

        self.deal_hands()

        for player in self.players:
            player.show_hand()
    
    def __repr__(self):
        if len(self.deck_of_cards) == 0:
            raise Exception("No cards")
        str = ""
        for i in range(0, len(self.deck_of_cards)):
            card = self.deck_of_cards[i]
            str += f"{i+1}. {card[1]} of {card[0]}\n"
        return str
        