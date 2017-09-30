def inValues():
    total = 0
    error = 0
    while True:
        while True:
            userinput = input("Please enter a number: ")
            if userinput == '0':
                return total
            try:
                total += float(userinput)
                error = 0
                break
            except ValueError:
                if error < 1:
                    print('Error.Please re - enter the value.')
                    error += 1
                else:
                    print('Two Errors in row! Quiting...')
                    return total


print(inValues())