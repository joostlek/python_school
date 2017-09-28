name = True
names = {}
while name:
    newname = input('Volgende naam: ')
    if newname:
        if newname in names:
            names[newname] += 1
        else:
            names[newname] = 1
    else:
        name = False

for k, v in names.items():
    if v == 1:
        print('Er is 1 student met de naam {0}'.format(k))
    else:
        print('Er zijn {0} studenten met de naam {1}'.format(v, k))