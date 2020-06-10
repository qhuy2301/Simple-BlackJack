class Chips:
    """
    A class to represent player's betting chips

    ...

    Attribute
    ---------
        total: int
            total amount of chips a player has (fixed for now)
        bet: int
            the amount of chips a player bets

    Methods
    -------
        win_bet():
            Add chips to total if player wins
        lose_bet():
            Subtract chips from total if player loses
    """

    def __init__(self):
        """
        Constructor

        Parameters
        ----------
            total: int
                total amount of chips a player has (fixed for now)
            bet: int
                the amount of chips a player bets
        """

        self.total = 100
        self.bet = 0

    def win_bet(self):
        """
        Add chips to total if player wins
        """

        self.total += self.bet

    def lose_bet(self):
        """
        Subtract chips from total if player loses
        """

        self.total -= self.bet
