from deck import Deck
from hand import Hand
from chips import Chips


def blackjack():
    while True:
        print("Welcome to Black Jack")

        deck = Deck()
        deck.shuffle()

        player = Hand()
        player.add_card(deck.deal())
        player.add_card(deck.deal())
        player_chips = Chips()

        dealer = Hand()
        dealer.add_card(deck.deal())
        dealer.add_card(deck.deal())





if __name__ == "__main__":
    blackjack()
