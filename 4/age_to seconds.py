import time
from datetime import date


def age_to_sec(age):
    """pobranie wartości wieku w dniach i zmiana na sekundy"""
    age_in_sec = int(age * 24 * 60 * 60)
    return str(age_in_sec)


# wyświetlenie dzisiejszej daty
date_now = date.today()
print("Dzisiaj jest: " + str(date_now))

# pobranie od usera daty urodzin
year = int(input("\nPodaj rok urodzenia: "))
month = int(input("Podaj miesiąc urodzenia: "))
day = int(input("Podaj dzień urodzin: "))

# wyświetlenie daty urodzin
birthday = date(year, month, day)
print("Twoja data urodzin to: " + str(birthday))

# obliczenie wartości bezwzględnej z różnicy dat
time_days = abs(date_now - birthday)

# wyświetlenie wieku w latach
your_age = int(time_days.days / 365.25)
print("Twój wiek to: " + str(your_age))

# wyświetlenie wieku w sekundach
age_in_sec = age_to_sec(time_days.days)
print("Twój wiek w sekundach to: " + str(age_in_sec))

