four = True
while four:
    fou = input('Geef een string van vier letters: ')
    if len(fou) == 4:
        print('Inlezen van correcte string: {0} is geslaagd'.format(fou))
        break
    print('{0} heeft {1} letters'.format(fou, len(fou)))
