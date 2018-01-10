"""
	program rzuca 100 razy monetą i wypisuje
	ile razy wypadł orzeł i ile reszka
"""


import random


print("Rzucę sto razy monetą. Spróbuj zgadnąć, ile razy wypadnie orzeł, a ile reszka")

while True:
        # ustawienie początkowych wystąpień figur
        head_num = 0
        tail_num = 0
        
        input("\nOrzeł: ")
        input("Reszka: ")

        # rzucenie 100 razy monetą
        for i in range(100):
                throw = random.randint(0,1)
                if throw == 0:
                        head_num += 1
                if throw == 1:
                        tail_num += 1

        # podsumowanie rzutów
        print("Orzeł wypadł: " + str(head_num) +  " razy, a reszka: "
              + str(tail_num) + " razy.")
		
	# wyjście z gry
        check = input("\nJeszcze raz? (t/n) ")
        if check != 't':
                print("Koniec")
                break;
        

