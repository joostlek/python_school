def week():
    abb = input('Enter day abbreviation: ')
    if abb == 'Mo':
        print('Monday')
    elif abb == 'Tu':
        print('Tuesday')
    elif abb == 'We':
        print('Wednesday')
    elif abb == 'Th':
        print('Thursday')
    elif abb == 'Fr':
        print('Friday')
    elif abb == 'Sa':
        print('Saturday')
    elif abb == 'Su':
        print('Sunday')
    else:
        print('No.')
    week()

week()