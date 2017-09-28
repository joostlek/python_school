invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
inv = invoer.split('-')
lst = []
for i in inv:
    lst.append(eval(i))
print("Gesorteerde list van ints: {0}\nGrootste getal: {1} en Kleinste getal: {2}\nAantal getallen: {3} en Som van de getallen: {4}\nGemiddelde: {5}".format(lst.sort(), max(lst), min(lst), len(lst), sum(lst), sum(lst) / len(lst)))
