letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
res = [0, 0, 0]
for letter in letters:
    if letter == "A":
        res[0] += 1
    elif letter == "B":
        res[1] += 1
    elif letter == "C":
        res[2] += 1

print(res)
"[2, 3, 4]"
