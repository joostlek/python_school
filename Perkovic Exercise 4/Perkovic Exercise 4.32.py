def censor(filename):
    file = open(filename)
    txt = file.read()
    file.close()
    lst = txt.split(' ')
    res = ''
    for word in lst:
        if len(word) == 4:
            word = 'xxxx'
        res += word + ' '

    dest = open('censored.txt', 'a')
    dest.write(res)
    dest.close()

censor('example.txt')