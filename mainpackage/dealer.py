"""Docstring for the dealer.py module


"""
from player import Player
import outcomes


class Dealer(Player):
    """
    A class to represent the dealer

    """

    def __init__(self, name):
        Player.__init__(self, name)

    def show_one_card(self):
        """Show one card in the dealer's hand."""
        print("\nDealer's hand:")
        print("", self.hand[0])
        print(" <Hidden card>")

    def ask(self, player, deck):
        """
        TODO: Docstring

        """
        print(f"\n{player.name}'s turn:")
        while True:
            print("\nWhat would you like to do?")
            print("[1] Hit")
            print("[2] Stand")
            if len(player.hand) == 2:
                print("[3] Double Down")
            decision = input("Please choose an option: ")

            if decision == '1':
                player.hit(deck)
                player.adjust()
                player.show_all_cards()
                player.show_value()

                if player.value >= 21:
                    if player.value == 21:
                        print("Your hand value is 21. Stand.")
                    else:
                        outcomes.player_bust(player)
                    break
            elif decision == '2':
                print("Player stands. Dealer is playing.")
                break
            elif decision == '3':
                player.bet *= 2
                player.hit(deck)
                player.adjust()
                player.show_all_cards()
                player.show_value()
                break
            else:
                print("Invalid input. Please try again.")
