def rps(player1, player2):
    if player1 == 'R':
        if player2 == 'S':
            return -1
        elif player2 == 'P':
            return 1
        return 0
    elif player1 == 'S':
        if player2 == 'P':
            return -1
        elif player2 == 'R':
            return 1
        return 0
    elif player1 == 'P':
        if player2 == 'R':
            return -1
        elif player2 == 'S':
            return 1
        return 0
    else:
        return 0

print(rps('R', 'P'))
print(rps('R', 'S'))
print(rps('S', 'S'))
