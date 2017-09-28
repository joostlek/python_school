def seizoen(maand):
    if maand >= 3 and maand <= 5:
        return 'Lente'
    elif maand >= 6 and maand <= 8:
        return 'Zomer'
    elif maand >= 9 and maand <= 11:
        return 'Herfst'
    elif maand >= 12 and maand <= 2:
        return 'Winter'
    else:
        return

