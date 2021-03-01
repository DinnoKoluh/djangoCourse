import numpy as np
import random

suite = ["H", "D", "S", "C"]
rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
d = [(s,r) for s in  suite for r in rank]

# for r in rank:
#     for s in suite:
#         deck.append((s,r))


class Deck():
    #deck = np.empty(shape = (2,52))
    deck = []
    deck1 = [[0] * 26 for _ in range(2)]
    deck2 = [[0] * 26 for _ in range(2)]

    def __init__(self):
        self.deck = d

    #def get_other_numbers(self, arr1):
        
    def shuffle_cards(self):
        random.shuffle(self.deck)

    def split_deck(self):
        return (self.deck[0:26], self.deck[26:52])

        



my_deck = Deck()
my_deck.shuffle_cards()
print(my_deck.deck)

#t = np.empty((2,3))
#print(t[1][2])

#print(random.sample(range(0,52), 26))

print(my_deck.split_deck())