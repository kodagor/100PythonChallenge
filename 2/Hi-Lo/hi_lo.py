import random


def setCompNum():
    """Losowanie liczby"""
    comp_num = random.randrange(0, 100) + 1
    return comp_num

def gameLoop(tries):
    """sprawdzanie, czy liczba się zgadza"""
    comp_num = setCompNum()
    
    while True:
        guess = int(input("Do dzieła. Podaj liczbę: "))
        tries -= 1
        if guess < 1 or guess > 100:
            print("Tylko liczby pomiędzy 1 a 100!")
        elif guess > comp_num:
            print("Moja liczba jest mniejsza")
        elif guess < comp_num:
            print("Moja liczba jest większa")
        if tries <= 0:
            print("Koniec gry. Moja liczba to: " + str(comp_num) + ".")
            again = input("Jeszcze raz (t/n)? ")
            if again == 't':
                tries = 7
                gameLoop(tries)
            elif again == 'n':
                print("Koniec")
                break;
        if guess == comp_num:
            print("Zwycięstwo! Moja liczba to " + str(comp_num) + ".")
            again = input("Jeszcze raz (t/n)? ")
            if again == 't':
                tries = 7
                gameLoop(tries)
            elif again == 'n':
                print("Koniec")
                break;
        print("Pozostało " + str(tries) + " prób")


tries = 7
print("Wylosuję liczbę od 1 do 100. Masz 7 prób, aby ją zgadnąć")
gameLoop(tries)




