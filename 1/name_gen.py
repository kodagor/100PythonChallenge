"""
generator imion
program wypluwa losowo imie męskie lub żeńskie,
w zależności od wyboru użytkownika
"""

import random


male_names = ["Jan","Paweł","Adolf","Herman","Alojzy","Geralt","Frodo"]
female_names = ["Ewa","Helga","Brugge","Wojna","Zofia","Renata","Adda"]
last_names = ["Hitler","Goring","Braun","Wojtyła","Grucha","Kutas","Polak"]

print("Program generuje losowa nazwe z listy imion i nazwisk (q aby zakończyć). \nWybierz płeć: ")
while True:
    sex = input("m - męska, f - żeńska: ")
    if sex == 'q':
        print("Koniec")
        break;
    if sex == "m":
        a = random.randrange(len(male_names))
        n = male_names[a]
    elif sex == 'f':
        a = random.randrange(len(female_names))
        n = female_names[a]
    b = random.randrange(len(last_names))
    ln = last_names[b]
    print(n + " " + ln)
    
