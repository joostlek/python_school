studenten = {}
studenten['asd'] = 9.0
studenten['ase'] = 8.0
studenten['asr'] = 10.0
studenten['ast'] = 7.0
studenten['asy'] = 5.0
studenten['asi'] = 4.0
studenten['asu'] = 7.0
studenten['aso'] = 8.0
studenten['asp'] = 9.0

for k, v in studenten.items():
    if v >= 9.0:
        print(k, v)