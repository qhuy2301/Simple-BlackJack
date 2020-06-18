def player_win(player):
    print("Player wins!")
    player.total_chips += player.bet


def player_bust(player):
    print("Player busts!")
    player.total_chips -= player.bet


def dealer_win(player):
    print("Dealer wins!")
    player.total_chips -= player.bet


def dealer_bust(player):
    print("Dealer busts!")
    player.total_chips += player.bet


def push(player):
    print("It's a tie!")


def blackjack(player):
    print("Black Jack!!!")
    player.total_chips += player.bet * 3/2
