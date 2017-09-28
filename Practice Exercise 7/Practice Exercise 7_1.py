zero = True
numbers = []


def ifint(number):
    if type(number) == int:
        return True
    else:
        return False


while zero:
    num = eval(input('Geef een getal: '))
    if ifint(num):
        if num == 0:
            print('Er zijn {0} getallen ingevoerd, de som is: {1}'.format(len(numbers), sum(numbers)))
            zero = False
        numbers.append(num)