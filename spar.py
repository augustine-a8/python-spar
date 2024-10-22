from constants import SUITS, RANKS, CPU_PLAYER_NAME
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
    
    def deal_hands_to_player(self, player):
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

    def __single_player(self):
        print("SPAR SINGLE PLAYER MODE")
        name = input("Enter player name: ")
        player = Player(name)
        self.players.append(player)
        cpu = Player(CPU_PLAYER_NAME)
        self.players.append(cpu)

        for player in self.players:
            self.deal_hands_to_player(player)
        
        for player in self.players:
            player.show_hand()

    def __multiplayer(self):
        pass

    def play(self):
        print("WELCOME TO PYTHON SPAR")
        print("1. Single Player\n2. Multiplayer")
        mode = input("Choose mode: ")
        while mode != "1" and mode != "2":
            print(f"Invalid choice: {mode}")
            print("Please choose option 1 or 2")
            print("1. Single Player\n2. Multiplayer")
            mode = input("Choose mode: ")

        if int(mode) == 1:
            self.__single_player()
        elif int(mode) == 2:
            self.__multiplayer()
    
    def __repr__(self):
        if len(self.deck_of_cards) == 0:
            raise Exception("No cards")
        str = ""
        for i in range(0, len(self.deck_of_cards)):
            card = self.deck_of_cards[i]
            str += f"{i+1}. {card[1]} of {card[0]}\n"
        return str
        