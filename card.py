class Card:
    """
    A class to represent a card

    ...


    Attribute
    ---------
    suit: str
        the suit of the card
    rank: str
        the rank of the card
    """

    def __init__(self,suit,rank):
        """
        Constructor of the object

        Parameters
        ----------
        suit: str
            the suit of the card
        rank: str
            the rank of the card
        """

        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
        Print out the suit and rank of the card
        """

        return "{} of {}".format(suit.capitalize(), rank.capitalize())
