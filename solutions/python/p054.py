"""
In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

Consider the following hand dealt to two players:

Hand         Player 1         Player 2         Winner
1         5H 5C 6S 7S KD     2C 3S 8S 8D TD    Player 2
          Pair of Fives      Pair of Eights
2         5D 8C 9S JS AC     2C 5C 7D 8S QH
          Highest card Ace   Highest Queen     Player 1

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated
cards), each player's hand is in no specific order, and in each hand there
is a clear winner.

How many hands does Player 1 win?
"""

from utils import read_file, all_equal


def run():
    """
    Practice some OOP with this problem
    """
    games = read_hands()
    count = 0
    for game in games:
        if game.winner() == Game.PLAYER_1:
            count += 1
    return count


def read_hands():
    """
    parse the given file into a hierarchy of objects
    """
    lines = read_file('data/p054 poker.txt', line_delim='\n')
    games = []
    for line in lines:
        if not line:
            continue
        cards = [Card.from_string(card_str) for card_str in line.split(' ')]
        games.append(Game(Hand(cards[:5]), Hand(cards[5:])))
    return games


class Game(object):
    DRAW = 0
    PLAYER_1 = 1
    PLAYER_2 = 2

    def __init__(self, p1_hand, p2_hand):
        self.p1_hand = p1_hand
        self.p2_hand = p2_hand

    def winner(self):
        if self.p1_hand == self.p2_hand:
            return self.DRAW
        elif self.p1_hand > self.p2_hand:
            return self.PLAYER_1
        else:
            return self.PLAYER_2

    def __repr__(self):
        return "(P1: %s, P2: %s)" % (str(self.p1_hand), str(self.p2_hand))


class Hand(object):

    def __init__(self, cards):
        if type(cards) is not list or len(cards) != 5:
            raise Exception('Invalid Hand')

        self.cards = cards
        self.sorted_cards = sorted(cards)
        self.lowest_card = self.sorted_cards[0]
        self.highest_card = self.sorted_cards[4]

        self.RANKERS = [
             self.is_high_card,
             self.is_one_pair,
             self.is_two_pairs,
             self.is_three_of_a_kind,
             self.is_straight,
             self.is_flush,
             self.is_full_house,
             self.is_four_of_a_kind,
             self.is_straight_flush,
             self.is_royal_flush
             ]
        self._compute_rank()

    def is_high_card(self):
        return True

    def is_one_pair(self):
        if all_equal(self.sorted_cards[:2]):
            self.highest_card = self.sorted_cards[0]
            return True
        if all_equal(self.sorted_cards[1:3]):
            self.highest_card = self.sorted_cards[1]
            return True
        if all_equal(self.sorted_cards[2:4]):
            self.highest_card = self.sorted_cards[2]
            return True
        if all_equal(self.sorted_cards[3:5]):
            self.highest_card = self.sorted_cards[3]
            return True
        return False

    def is_two_pairs(self):
        if all_equal(self.sorted_cards[:2]) and \
           all_equal(self.sorted_cards[2:4]):
            self.highest_card = max(self.sorted_cards[0], self.sorted_cards[2])
            return True
        if all_equal(self.sorted_cards[:2]) and \
           all_equal(self.sorted_cards[3:5]):
            self.highest_card = max(self.sorted_cards[0], self.sorted_cards[3])
            return True
        if all_equal(self.sorted_cards[1:3]) and \
           all_equal(self.sorted_cards[3:5]):
            self.highest_card = max(self.sorted_cards[1], self.sorted_cards[3])
            return True
        return False

    def is_three_of_a_kind(self):
        if all_equal(self.sorted_cards[:3]):
            self.highest_card = self.sorted_cards[0]
            return True
        if all_equal(self.sorted_cards[1:4]):
            self.highest_card = self.sorted_cards[1]
            return True
        if all_equal(self.sorted_cards[2:5]):
            self.highest_card = self.sorted_cards[2]
            return True
        return False

    def is_straight(self):
        first = self.lowest_card.value
        for index in xrange(1, len(self.sorted_cards)):
            value = self.sorted_cards[index].value
            if index == 4 and value == 14 and self.lowest_card.value == 2:
                self.highest_card = self.sorted_cards[3]
                return True
            elif value is not first + 1:
                return False
            else:
                first = value
        return True

    def is_flush(self):
        if all_equal([card.suit for card in self.cards]):
            return True
        return False

    def is_full_house(self):
        if all_equal(self.sorted_cards[:3]) and \
           all_equal(self.sorted_cards[3:]):
            self.highest_card = self.sorted_cards[0]
            return True
        if all_equal(self.sorted_cards[:2]) and \
           all_equal(self.sorted_cards[2:]):
            self.highest_card = self.sorted_cards[2]
            return True
        return False

    def is_four_of_a_kind(self):
        if all_equal(self.sorted_cards[:4]):
            self.highest_card = self.sorted_cards[0]
            return True
        if  all_equal(self.sorted_cards[1:]):
            self.highest_card = self.sorted_cards[1]
            return True
        return False

    def is_straight_flush(self):
        return self.is_flush() and self.is_straight()

    def is_royal_flush(self):
        return self.is_straight_flush() and self.lowest_card.value == 9

    def _compute_rank(self):
        for rank in xrange(len(self.RANKERS) - 1, -1, -1):
            if self.RANKERS[rank]():
                self.rank = rank
                return
        self.rank = -1

    def __eq__(self, other):
        if isinstance(other, Hand):
            return self.rank == other.rank and \
                self.highest_card == other.highest_card
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __lt__(self, other):
        if isinstance(other, Hand):
            if self.rank is not other.rank:
                return self.rank < other.rank
            else:
                return self.highest_card < other.highest_card
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Hand):
            if self.rank is not other.rank:
                return self.rank > other.rank
            else:
                return self.highest_card > other.highest_card
        return NotImplemented

    def __repr__(self):
        return ' '.join(map(lambda x: str(x), self.cards))


class Card(object):
    SPECIAL = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def __init__(self, value, suit):
        self.display_value = value
        if value in Card.SPECIAL:
            value = Card.SPECIAL[value]
        else:
            value = int(value)
        self.value = value
        self.suit = suit

    @classmethod
    def from_string(cls, string):
        if type(string) is not str or len(string) != 2:
            raise Exception('Invalid card string')
        return cls(string[0], string[1])

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.value == other.value
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __lt__(self, other):
        if isinstance(other, Card):
            return self.value < other.value
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Card):
            return self.value > other.value
        return NotImplemented

    def __repr__(self):
        return str(self.display_value) + str(self.suit)
