file = open('gamers.csv')
txt = file.readlines()
file.close()

highest = ['', '00-00-0000', 0]
for line in txt:
    score = line.split(';')
    if int(score[2]) > int(highest[2]):
        highest = score

print('De hoogste score is: {0[2]} op {0[1]} behaald door {0[0]}'.format(highest))
