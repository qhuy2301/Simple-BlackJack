from chip import Chips
from deck import Deck
from hand import Hand


def bet(chips):
    while True:
        try:
            chips.bet = int(input("Enter the amount you want to bet:"))
        except ValueError:
            print("Invalid input.")
        else:
            if (chips.bet > chips.total):
                print("Insufficient.")
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()


def hit_or_stand(deck, hand):
    global playing
    while True:
        decision = input("Would you like to hit or stand? Enter 'h' for hit or 's' for stand.")
        if (decision == 'h'):
            hit(deck, hand)
            break
        elif (decision == 's'):
            print("Player stands. Dealer is playing.")
            break
        else:
            print("Invalid input. Please try again.")


def show_some_cards(player, dealer):
    print("\nDealer's hand:")
    print(" <hidden card>")
    print(" ", dealer.cards[1])
    print("\nPlayer's hand:", *player.cards, sep='\n')


def show_all_cards(player, dealer):
    print("\nDealer's hand:", *dealer.cards, sep='\n')
    print("Dealer's hand = ", dealer.value)
    print("\nPlayer's hand:", *player.cards, sep='\n')
    print("Player's hand = ", player.value)
