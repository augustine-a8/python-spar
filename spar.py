from constants import SUITS, RANKS, CPU_PLAYER_NAME
from player import Player
import random

class Spar:
    def __init__(self):
        self.deck_of_cards = []
        self.players = []
        self.trick_winning_card = ()

        self.shuffle_deck()

    def shuffle_deck(self):
        self.deck_of_cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck_of_cards.append((suit, rank))
        random.shuffle(self.deck_of_cards)

    def __get_random_card_from_deck(self):
        i = random.randint(0, len(self.deck_of_cards) - 1)
        return self.deck_of_cards.pop(i) 
    
    def deal_hands_to_player(self, player):
        first_set = 3
        while first_set > 0:
            player.add_card_to_hand(self.__get_random_card_from_deck())
            first_set -= 1
        second_set = 2
        while second_set > 0:
            player.add_card_to_hand(self.__get_random_card_from_deck())
            second_set -= 1

    def __single_player(self):
        self.players = []
        print("SPAR SINGLE PLAYER MODE")
        name = input("Enter player name: ")
        player = Player(name)
        self.players.append(player)
        cpu = Player(CPU_PLAYER_NAME)
        self.players.append(cpu)

        for player in self.players:
            self.deal_hands_to_player(player)
        
        random.shuffle(self.players)
        starting_player = self.players[0]
        next_player = self.players[1]

        while not starting_player.hand_is_empty() and not next_player.hand_is_empty():
            print(f"{starting_player.name}'s turn")
            p1_card = starting_player.play_card()
            print(f"{next_player.name}'s turn")
            p2_card = next_player.play_card()
            trick_winner = self.__compare_cards(p1_card, p2_card)
            if trick_winner == 1:
                print(f"{starting_player.name} won turn with {p1_card[1]} of {p1_card[0]}")
            else:
                print(f"{next_player.name} won turn with {p2_card[1]} of {p2_card[0]}")
                temp = starting_player
                starting_player = next_player
                next_player = temp
        
        print(f"{starting_player.name} WON SET")
        print(f"GAME OVER!!")

    def __compare_cards(self, card_one, card_two):
        if card_one[0] == card_two[0]:
            if RANKS.index(card_one[1]) >= RANKS.index(card_two[1]):
                return 1
            else:
                return 2
        return 1

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
        