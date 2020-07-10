"""Docstring for the card.py module

This module contains the Card class which can be used for creating
multiple cards in a deck.

"""


class Card:
    """
    A class to represent cards.

    Parameters
    ----------
    suit : str
        The suit of the card
    rank : str
        The rank of the card

    Attributes
    ----------
    suit : str
        The suit of the card
    rank : str
        The rank of the card

    """

    def __init__(self, suit, rank):
        """
        Class constructor

        Parameters
        ----------
        suit : str
            The suit of the card
        rank : str
            The rank of the card

        """
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Print out the suit and rank of the card."""
        return self.rank + " of " + self.suit
