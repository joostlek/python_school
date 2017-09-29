from random import shuffle

class Card:

    def __init__(self, type, number):
        self.type = type
        self.number = number

    def print(self):
        return '{0} - {1}'.format(self.number, self.type)


def getDecks():
    stack1 = []
    stack2 = []
    for i in range(1, 15):
        for type in range(1, 3):
            stack1.append(Card(type, i))
        for type in range(3, 5):
            stack2.append(Card(type, i))
    shuffle(stack1)
    shuffle(stack2)
    return [stack1, stack2]

def playRound(deck1, deck2):
    card1 = deck1[0]
    card2 = deck2[0]
    if card1.number > card2.number:
        deck2.remove(card2)
        deck1.append(card2)
    elif card2.number > card1.number:
        deck1.remove(card1)
        deck2.append(card1)
    elif card2.number == card1.number:
        war(card1, card2, deck1, deck2, [])

def war(c1, c2, d1, d2, table):
    if not table:
        table = [[], []]
    if len(d1) < 3:
        table[0].extend(d1)
    else:
        table[0].extend(d1[0:3])
    if len(d2) < 3:
        table[1].extend(d2)
    else:
        table[1].extend(d2[0:3])
    e1 = table[0][0]
    e2 = table[1][0]
    if e1.number > e2.number:
        for card in table[1]:
            d1.append(card)
            d2.remove(card)
        print('Won by 1')
    elif e2.number > e1.number:
        for card in table[0]:
            d2.append(card)
            d1.remove(card)
        print('Won by 2')
    elif e2.number == e1.number:
        print('Another war')
        war(c1, c2, d1, d2, table)


a, b = getDecks()
playRound(a, b)