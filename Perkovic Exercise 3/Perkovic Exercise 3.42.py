def avg(lst):
    for student in lst:
        amount = 0
        res = 0
        for score in student:
            amount += 1
            res += score
        print(res/amount)

avg([[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]])
