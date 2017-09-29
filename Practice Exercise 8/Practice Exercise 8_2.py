from random import randrange
def monopolyworp(time):
    dob1 = randrange(1, 7)
    dob2 = randrange(1, 7)
    ext = ''
    if dob1 == dob2:
        time += 1
        ext = '(dubbel)'
    if time == 3:
        ext = '(direct naar de gevangenis)'
    print('{0} + {1} = {2} {3}'.format(dob1, dob2, dob1 + dob2, ext))
    if ext == '(dubbel)':
        monopolyworp(time)
monopolyworp(0)