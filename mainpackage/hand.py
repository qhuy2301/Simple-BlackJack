from deck import values


class Hand:
    """
    A class to represent a player's hand

    ...

    Attributes
    ----------
    cards: [card]
        A list of card the player has
    values: int
        Total value of all cards in player's hand
    aces: int
        The number of aces in player's hand

    Methods
    -------
    add_card(card):
        Add a card from deck to player's hand
    adjust_for_aces:
        Adjust the value of aces to keep the total value under 21
    """

    def __init__(self):
        """
        Class constructor
        """

        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        """
        Add the card to the player's hand, increase the hand's value and keep
        track of the total number of aces.

        Parameters
        ----------
        card: Card
           The card to be added to player's hand
        """

        self.cards.append(card)
        self.value += values(card.rank)
        if card.rank == "Ace":
            self.aces += 1


    def adjust_for_ace(self):
        """
        Adjust the values of aces in the player's hand (if exists) to keep the hand's value
        below 21.
        """

        while (self.value > 21) and (self.aces > 0):
            self.value -= 10
            self.aces -= 1
