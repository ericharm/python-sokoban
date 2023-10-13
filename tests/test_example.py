from dataclasses import dataclass
from enum import Enum
from typing import Union
from random import shuffle


class Suit(Enum):
    clubs = "clubs"
    hearts = "hearts"
    diamonds = "diamonds"
    spades = "spades"


class Face(Enum):
    king = "king"
    queen = "queen"
    jack = "jack"
    ace = "ace"


@dataclass
class Card:
    suit: Suit
    rank: Union[int, Face]


@dataclass
class Deck:
    cards: list[Card]


def create_deck() -> Deck:
    deck = Deck([])
    for suit in Suit:
        for rank in range(2, 11):
            deck.cards.append(Card(suit, rank))
        for rank in Face:
            deck.cards.append(Card(suit, rank))
    return deck


def shuffle_deck(deck: Deck) -> None:
    # make a copy of the deck
    # new_deck = deck.cards[:]
    shuffle(deck.cards)


def test_create_deck():
    deck = create_deck()
    assert len(deck.cards) == 52


def test_shuffle_deck():
    deck = create_deck()
    first_card = deck.cards[0]
    shuffle_deck(deck)
    new_first_card = deck.cards[0]

    assert new_first_card != first_card
