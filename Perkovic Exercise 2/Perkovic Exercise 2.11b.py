#  17 are 9 years old,
# 24 are 10 years old, 21 are 11 years old, and 27 are 12 years o
people = [(9, 17), (10, 24), (11, 21), (12, 27)]
tot = 0
age = 0
for key, value in people:
    tot += value
    age += (key * value)

print(str(age / tot))
