from common.tools import read_input

inp = read_input()
test_inp = read_input('task_sample.txt')
lines = inp.split('\n')

cv = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
}


def gv(card):
    return cv.get(card) or int(card)


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    @property
    def counts(self):
        counts = {}
        for i in self.cards:
            counts[i] = counts.get(i, 0) + 1
        return counts

    @property
    def ctype(self):
        # has five of a kind
        if len(set(self.cards)) == 1:
            return 6
        # has four of a kind
        elif list(self.counts.values()).count(4) and list(self.counts.values()).count(1):
            return 5
        # has full_house
        elif list(self.counts.values()).count(3) and list(self.counts.values()).count(2):
            return 4
        # has three of a kind
        elif list(self.counts.values()).count(3):
            return 3
        # has two pairs
        elif list(self.counts.values()).count(2) == 2:
            return 2
        # has one pair
        elif list(self.counts.values()).count(2) == 1:
            return 1
        # has high card
        else:
            return 0


    def compare_cards(self, other):
        """
        returns true if this object is greater than other
        :type other: Hand
        :rtype: bool
        """
        for this_card, other_card in zip(self.cards, other.cards):
            if gv(this_card) == gv(other_card):
                continue
            return gv(this_card) > gv(other_card)
        raise RuntimeError('Hands have exactly equal value!')

    def __eq__(self, other):
        # lets assume Hands cannot be exactly equal for now
        if self.ctype == other.ctype and self.compare_cards(other):
            compared = self.compare_cards(other)
            return False
        return False

    def __lt__(self, other):
        if self.ctype == other.ctype:
            return not self.compare_cards(other)
        return self.ctype < other.ctype

    def __gt__(self, other):
        if self.ctype == other.ctype:
            return self.compare_cards(other)
        return self.ctype > other.ctype


hands = []
for line in lines:
    cards, bid = line.split(' ')
    # print(bid)
    hands.append(Hand([c for c in cards], int(bid)))

shands = sorted(hands)
money = 0
for i, s in enumerate(shands):
    print((i+1, s.cards, s.ctype, s.bid))
    money += (i+1)*s.bid

print(money)
