"""Docstring for the player.py module

This module contains the Player class which can be used for creating
multiple Black Jack players.

"""
from deck import VALUES


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
    hit(Deck)
        Add a card from the deck to the player's hand
    adjust
        Adjust the value of aces to keep the total value under 21
    show_all_cards
        Show all cards in the player's hand

    """

    def __init__(self, name, total_chips=0):
        """
        Class constructor

        Parameters
        ----------
        name : str
            Player's name
        total_chips : int, optional
            Total amount of chips the player has

        """
        self.name = name
        self.total_chips = total_chips
        self.bet = 0
        self.hand = []
        self.value = 0
        self.aces = 0

    def betting(self):
        while True:
            try:
                self.bet = int(input("Enter the amount you want to bet: "))
            except ValueError:
                print("Invalid input.")
            else:
                if (self.bet > self.total_chips):
                    print("Sorry. You don't have enough chips.")
                else:
                    break

    def hit(self, deck):
        """
        Add a card from the deck to the player's hand.

        If the player chooses 'hit', a random card from the deck will
        be added to the player's hand, and the card's value will be
        added to the total hand value. If the card is an Ace, it will
        also be kept track of for adjustment if needed.

        Parameters
        ----------
        deck : :obj: Deck
            The deck from which a card will be drawn

        """
        card = deck.deal()
        self.hand.append(card)
        self.value += VALUES[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust(self):
        """
        Adjust the value of Ace cards.

        If the player's total hand value exceeds 21 and there is at
        least one Ace card, its value can be adjust from 11 to 1.

        """
        while (self.value > 21) and (self.aces > 0):
            self.value -= 10
            self.aces -= 1

    def show_all_cards(self):
        """Show all cards in the player's hand."""
        print(f"\n{self.name}'s hand:", *self.hand, sep="\n ")

    def show_value(self):
        """Show the player's hand value."""
        print(f"{self.name}'s hand value: {self.value}")
