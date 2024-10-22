from constants import MAX_CARDS_PER_PLAYER

class CardPlayer:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def add_card_to_hand(self, card):
        if len(self.hand) > MAX_CARDS_PER_PLAYER:
            raise Exception(f"Max cards reached for {self.name}")
        self.hand.append(card)
    
    def show_hand(self):
        all_cards_str = ""
        for i in range(0, len(self.hand)):
            card = self.hand[i]
            all_cards_str += f"{i+1}. {card[1]} of {card[0]}\t"
        print(f"{self.name}'s Deck")
        print(all_cards_str)

    def hand_is_empty(self):
        return len(self.hand) == 0
    
    def play_card(self):
        pass