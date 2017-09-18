def stats(filename):
    file = open(filename)
    txt = file.read()
    file.close()
    print('line count: ' + str(txt.count('\n') + 1))
    print('word count: ' + str(txt.count(' ') + 1 + txt.count('\n')))
    print('character count: ' + str(txt.count('')))

stats('example.txt')