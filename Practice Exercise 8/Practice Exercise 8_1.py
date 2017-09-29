bruin = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Hout', 'Helmond', 'Brouwhuis', 'Deurne'}
groen = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}
print(bruin & groen)
print(bruin - (bruin & groen))
print(groen - (bruin & groen))
