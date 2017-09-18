def convert(celcius):
    return celcius * 1.8 + 32


def table():
    print('  F      C')
    for i in range(-30, 41, 10):
        print("{0:5} {1:6}".format(convert(i), float(i)))

table()
