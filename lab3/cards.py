from collections import namedtuple
from enum import Enum, IntEnum
import random
import itertools

class SuitEnum(Enum):
    SPADES = '\u2660'   #♠️
    HEARTS = '\u2665'   #♥️
    DIAMONDS = '\u2666' #♦️
    CLUBS = '\u2663'    #♣️

    def __str__(cls):
        return f'{cls.name.lower()} ({cls.value})'

class RankEnum(Enum):
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'
    ACE = 'A'

    def __str__(cls):
        return f'{cls.name.lower()} ({cls.value})'


class Card:
    __slots__ = 'rank', 'suit'  # consume less memory

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f'{self.rank.value}{self.suit.value}'

class Deck:

    def __init__(self):
        self.__cards = list()
        ranks = list(RankEnum)
        suits = list(SuitEnum)
        products = itertools.product(ranks, suits)
        for product in products:
            self.__cards.append(Card(product[0],product[1]))        

    def __len__(self):
        return len(self.__cards)

    def get_top(self):
        return self.__cards.pop(0) if len(self) else None
    
    def get_bottom(self):
        return self.__cards.pop(len(self) - 1) if len(self) else None 

    def shuffle(self):
        random.shuffle(self.__cards)

if __name__ == '__main__':
    ...
