"""Docstring for the deck.py module

This module contains the Deck class which can be used for creating a
normal deck of cards.

Attributes
----------
SUITS : tuple(str)
    A tuple that contains all four suits of a deck of cards
RANKS : tuple(str)
    A tuple that contains all thirteen ranks of a deck of cards
VALUES : dict(str:int)
    A dictionary that maps the ranks to their integer values

"""
import random
from .card import Card


SUITS = ("Hearts", "Diamonds", "Spades", "Clubs")
RANKS = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
         "Nine", "Ten", "Jack", "Queen", "King", "Ace")
VALUES = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
          "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10,
          "Queen": 10, "King": 10, "Ace": 11}


class Deck:
    """
    A class to represent a deck of cards

    Attributes
    ----------
        deck : list(Card)
            A list of all cards available to deal

    Methods
    -------
        shuffle
            Shuffle the deck
        deal
            Get a card from the deck

    """

    def __init__(self):
        """Class constructor"""
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.deck)

    def deal(self):
        """
        Get a card from the deck.

        Remove a random card from the deck and give it to the one who
        draws.

        Returns
        -------
        card : :obj: Card
            A card from the deck.

        """
        card = self.deck.pop()
        return card
