def inlezen_beginstation(stations):
    while True:
        station = input('Beginstation:')
        if station in stations:
            return station

def inlezen_eindstation(allstations, beginstation):
    index_begin_station = allstations.index(beginstation)
    while True:
        station = input('Eindstation')
        if station in stations:
            index_eind_station = stations.index(station)
            if index_eind_station > index_begin_station:
                return station

def omroepen_reis(allstations, beginstation, eindstation):
    index_begin = allstations.index(beginstation) + 1
    begin = 'Het beginstation is {} en heeft als index {}'.format(beginstation, str(index_begin))
    index_eind = allstations.index(eindstation) + 1
    eind = 'Het eindstation is {} en heeft als index {}'.format(beginstation, str(index_eind))

    print(begin)
    print(eind)
    afstand = index_eind - index_begin
    print('Stand is {}'.format(str(afstand)))
    if afstand > 1:
        for index in range(index_begin + 1, index_eind):
            print(' - ' + stations[index])


stations = stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal'
  , 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

begin_station = inlezen_beginstation(stations)
eind_station = inlezen_eindstation(stations, begin_station)
omroepen_reis(stations, begin_station, eind_station)