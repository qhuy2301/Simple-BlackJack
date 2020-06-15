from deck import Deck
from hand import Hand
from chips import Chips
import action as action
import outcomes as outcomes


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

        action.bet(player_chips)

        action.show_some_cards(player, dealer)

        global game_on
        while game_on:
            action.hit_or_stand(deck, player)

            action.show_some_cards(player, dealer)

            if player.value > 21:
                outcomes.player_bust(player, dealer, player_chips)
                break

        while dealer.value < 17:
            action.hit(deck, dealer)
            action.show_all_cards(player, dealer)

        if dealer.value > 21:
            outcomes.dealer_bust(player, dealer, player_chips)
        elif dealer.value == player.value:
            outcomes.push(player, dealer, player_chips)
        elif player.value < dealer.value:
            outcomes.dealer_win(player, dealer, player_chips)
        else:
            outcomes.dealer_win(player, dealer, player_chips)

        new_game = input("Replay?")

        if new_game[0].lower() == 'y':
            game_on = True
            continue
        else:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    blackjack()
