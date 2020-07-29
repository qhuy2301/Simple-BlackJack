from deck import Deck
from player import Player
from dealer import Dealer
import outcomes as outcomes


def blackjack():
    print("Welcome to Black Jack!!!")
    while True:
        deck = Deck()
        deck.shuffle()
        
        num_play = int(input("How many people are playing? "))
        player_list = []

        for i in range(num_play):
            print("\nPlayer {num} information".format(num=i+1))
            name = input("Name: ")
            chips = int(input("Total chips: "))
            player = Player(name, chips)
            player.betting()
            player.hit(deck)
            player.hit(deck)
            player_list.append(player)

        dealer = Dealer("Dealer")
        dealer.hit(deck)
        dealer.hit(deck)

        dealer.show_one_card()
        for player in player_list:
            player.show_all_cards()
            player.show_value()

        for player in player_list:
            dealer.ask(player, deck)

        while dealer.value < 17:
            dealer.hit(deck)
            dealer.show_all_cards()
            dealer.show_value()

        if dealer.value > 21:
            outcomes.dealer_bust(player)
        elif dealer.value == player.value:
            outcomes.push(player)
        elif player.value < dealer.value:
            outcomes.dealer_win(player)
        else:
            outcomes.dealer_win(player)

        new_game = input("Replay?")

        if new_game[0].lower() == 'y':
            game_on = True
            continue
        else:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    blackjack()
