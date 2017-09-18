
file = open('kaartnummers.txt')
line = file.readline()
length = 0
numbers = []
while line:
    length += 1
    user = line.split(', ')
    numbers.append(user[0])
    line = file.readline()
file.close()
print("Deze file telt {0} regels\nHet grootste kaartnummer is: {1} en dat staat op regel {2}".format(length, max(numbers), numbers.index(max(numbers)) + 1))