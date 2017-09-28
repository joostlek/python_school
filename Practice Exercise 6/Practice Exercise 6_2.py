lst = eval(input("Geef lijst met minimaal 10 strings: "))
newLst = []
for item in lst:
    if len(item) == 4:
        newLst.append(item)

print(newLst)
