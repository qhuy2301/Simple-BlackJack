"""Docstring for the player.py module

This module contains the Player class which can be used for creating
multiple Black Jack players.

"""
from .deck import VALUES


class Player:
    """
    A class to represent players.

    Parameters
    ----------
    name : str
        Player's name
    total_chips : int
        Total amount of chips the player has

    Attributes
    ----------
    name : str
        Player's name
    total_chips: int
        Total amount of chips the player has
    bet : int
        The amount of chips the player bets
    hand : list(Card)
        Player's cards
    value : int
        Total value of player's hand
    aces : int
        Number of aces in player's hand

    Methods
    -------
    add_card(Card)
        Add a card from the deck to the player's hand
    adjust
        Adjust the value of aces to keep the total value under 21

    """

    def __init__(self, name, total_chips):
        """
        Class constructor

        Parameters
        ----------
        name : str
            Player's name
        total_chips : int
            Total amount of chips the player has

        """
        self.name = name
        self.total_chips = total_chips
        self.bet = 0
        self.hand = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        """
        Add a card from the deck to the player's hand.

        If the player chooses 'hit', a random card from the deck will
        be added to the player's hand, and the card's value will be
        added to the total hand value. If the card is an Ace, it will
        also be kept track of for adjustment if needed.

        Parameters
        ----------
        card : :obj: Card
            The card to be added to the player's hand

        """
        self.hand.append(card)
        self.value += VALUES[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust(self):
        """
        Adjust the value of Ace cards

        If the player's total hand value exceeds 21 and there is at
        least one Ace card, its value can be adjust from 11 to 1.

        """
        while (self.value > 21) and (self.aces > 0):
            self.value -= 10
            self.aces -= 1
