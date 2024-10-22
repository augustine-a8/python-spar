from cardplayer import CardPlayer

class Player(CardPlayer):
    def __init__(self, name):
        super().__init__(name)
   
    def play_card(self):
        self.show_hand()
        card_index = int(input("Pick card: "))
        if card_index > len(self.hand) or card_index < 1:
            raise IndexError("Card index out of bounds")
        played_card = self.hand.pop(card_index - 1)
        print(f"{self.name} played {played_card[1]} of {played_card[0]}")
        return played_card