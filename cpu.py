from cardplayer import CardPlayer
from constants import CPU_PLAYER_NAME
import random

class CpuPlayer(CardPlayer):
    def __init__(self):
        super().__init__(CPU_PLAYER_NAME)
    
    def play_card(self):
        card_index = random.randint(0, len(self.hand) - 1)
        played_card = self.hand.pop(card_index - 1)
        print(f"{CPU_PLAYER_NAME} played {played_card[1]} of {played_card[0]}")
        return played_card