def player_win(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def player_bust(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def dealer_win(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def dealer_bust(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def push(player, dealer, chips):
    print("It's a tie!")
