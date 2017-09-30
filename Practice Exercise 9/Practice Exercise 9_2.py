import datetime
import csv

bestand = 'inloggers.csv'

def today():
    return datetime.datetime.today().strftime("%a %d %b %Y")

def save(name, letters, birth, email):
    with open(bestand, 'a') as csvfile:
        fieldnames = ['datum', 'naam', 'voorletters', 'geboortedatum', 'email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'datum': today(), 'naam': name, 'voorletters': letters, 'geboortedatum': birth, 'email': email})


while True:
    naam = input("Wat is je achternaam? ")
    if naam == 'einde':
        break
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")
    save(naam, voorl, gbdatum, email)


