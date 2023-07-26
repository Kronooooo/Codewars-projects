def rps(p1, p2):
    win = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    if p1 == p2:
        return 'Draw!'
    elif p2 == win[p1]:
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'