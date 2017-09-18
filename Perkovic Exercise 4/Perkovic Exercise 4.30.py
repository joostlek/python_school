def distribution(filename):
    file = open(filename)
    txt = file.read()
    file.close()
    grades = txt.split(' ')
    grades.sort()
    grad = []
    for grade in grades:
        if grade not in grad:
            grad.extend([grade])
            amount = grades.count(grade)
            print(str(amount) + ' students got ' + grade)

distribution('grades.txt')