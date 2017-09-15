def kwadraten_som(grondgetallen):
    res = 0
    for getal in grondgetallen:
        if getal > 0:
            res += getal**2
    return res

print(kwadraten_som([4, 5, 3, -81]))
