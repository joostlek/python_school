def menu():
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn\n2: Ik wil een nieuwe kluis\n3: Ik wil even iets uit mijn kluis halen\n4: Ik geef mijn kluis terug')
    choice = eval(input('> '))
    if choice == 1:
        free()
        menu()
    elif choice == 2:
        new()
        menu()
    elif choice == 3:
        take()
        menu()
    elif choice == 4:
        retour()
        menu()
    else:
        print('You did not enter a correct value, please try again.')
        menu()


def free():
    print('{0} kluizen zijn er vrij.'.format(len(getSafes())))


def getSafes():
    file = open('kluizen.txt')
    txt = file.readlines()
    file.close()
    safes = []
    for safe in txt:
        pos = eval(safe.split(';')[0])
        code = safe.split(';')[1]
        safes.append([pos, code])
    return safes


def new():
    if len(getSafes()) < 12:
        unused = list(range(1, 13))
        for safe in getSafes():
            unused.remove(safe[0])
        number = unused[0]
        code = input('Voer uw wachtwoord in: ')
        if len(code) < 4:
            print('Voer een wachtwoord in van minimaal 4 karakters')
            return new()
        addSafe(number, code)
        print('Uw kluisnummer is {0}'.format(number))


def addSafe(number, code):
    file = open('kluizen.txt', 'a')
    file.write('{0};{1}'.format(number, code))
    file.close()

def take():
    number = eval(input('Voer uw kluisnummer in:'))
    if ifint(number):
        for safe in getSafes():
            if number == safe[0]:
                askcode(False, safe)
                return
    print('Dit nummer is niet bij ons bekend')
    return


def retour():
    number = eval(input('Voer uw kluisnummer in:'))
    if ifint(number):
        for safe in getSafes():
            if number == safe[0]:
                askcode(True, safe)
                return
    print('Dit nummer is niet bij ons bekend')
    return


def askcode(retour, safe):
    code = input('Voer uw code in:')
    if code + '\n' == safe[1]:
        print('U heeft toegang tot uw kluis!')
        if retour:
            renew(safe[0])
    else:
        print('Nee.')
        return

def renew(number):
    safes = getSafes()
    file = open('kluizen.txt', 'w').close()
    for safe in safes:
        if safe[0] != number:
            addSafe(safe[0], safe[1])

def ifint(number):
    if type(number) == int:
        return True
    else:
        return False

menu()