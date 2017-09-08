answers = ['Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'N']
numYes = 0
numNo = 0
for answer in answers:
    if answer == 'Y':
        numYes += 1
    if answer == 'N':
        numNo += 1

percentYes = str(numYes / (numYes + numNo) * 100) + '%'
answers.sort()
for answer in answers:
    if answer == 'Y':
        f = answer
        break
