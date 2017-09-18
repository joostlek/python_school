import datetime


def start():
    name = input()
    s = datetime.datetime.today().strftime("%a %d %b %Y, %H:%M:%S")
    file = open('hardlopers.txt', 'a')
    file.write(s + ', ' + name + '\n')
    file.close()
    start()

start()
