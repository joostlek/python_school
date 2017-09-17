def partition(lst):
    for player in lst:
        first_letter = ord(player[0])
        if first_letter >= 97 and first_letter <= 109 or first_letter >= 65 and first_letter <= 77:
            print(player)

partition(['Eleanor', 'Evelyn', 'Sammy', 'Owen', 'Gavin'])