import random
from card import Card

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
         "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
          "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10,
          "Queen": 10, "King": 10, "Ace": 11}


class Deck:
    """
    A class to represent a deck

    ...

    Attributes
    ---------
        deck: [card]
            a list of all cards available to deal

    Methods
    -------
        shuffle():
            shuffle the deck
        deal():
            deal (return) a card from the deck
    """

    def __init__(self):
        """
        Constructor of the object

        Parameters
        ----------
            deck: [card]
                a list of all cards available to deal
        """

        self.deck = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit=suit, rank=rank)
                self.deck.append(card)

    def shuffle(self):
        """
        Shuffle the deck
        """

        random.shuffle(self.deck)

    def deal(self):
        """
        Deal a card from the deck
        """

        return self.deck.pop()
