def ask():
    ins = input("Hoeveel personen?\n")
    try:
        i = int(ins)
        if i < 0:
            print('Negatieve getallen zijn niet toegestaan!')
            return
        print(4356 / i)
        return
    except ZeroDivisionError:
        print('Delen door nul kan niet!')
        return
    except ValueError:
        print('Gebruik cijfers voor het invoeren van het aantal!')
        return
    except Exception:
        print('Onjuiste invoer.')
        return

ask()
