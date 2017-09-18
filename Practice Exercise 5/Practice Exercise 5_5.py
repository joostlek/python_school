def gemiddelde():
    s = input("Voer uw zin in: ")
    words = s.split(' ')
    amount = 0
    for word in words:
        amount += len(word)
    print('\n' + str(amount / len(words)))

gemiddelde()