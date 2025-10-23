import random


cards = []
suits = ["spades", "clubs", "Hearts", "Diamond"]
ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])


def shuffle():
    random.shuffle(cards)

def deal(number):
    card_dealt = []
    for x in range(number):
        card = cards.pop()
        card_dealt.append(card)
        return card_dealt


shuffle()
card_dealt = deal(2)
card = card_dealt[0]
rank = card[1]
if rank == "A":
    value = 11
elif rank == "J" or rank == "Q" or rank == "K":
    value = 10
else:
    value = rank


print(rank, value)
