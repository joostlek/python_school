file = open('kaartnummers.txt')
txt = file.read()
file.close()
inp = txt.split('\n')[:len(txt.split('\n')) - 1]
for user in inp:
    user = user.split(", ")
    print("{0} heeft kaartnummer: {1}".format(user[1], user[0]))
