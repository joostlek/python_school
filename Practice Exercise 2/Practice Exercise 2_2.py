cijferICOR = 10
cijferPROG = 7
cijferCSN = 5

gemiddelde = (cijferCSN + cijferICOR + cijferPROG) / 3
beloning = gemiddelde * 90
overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van €' + str(beloning) + ' op!'

print(overzicht)
"Mijn cijfers (gemiddeld een 7.333333333333333) leveren een beloning van €660.0 op!"
