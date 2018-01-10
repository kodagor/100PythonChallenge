"""
program przeprowadza konwersję temperatur
"""


def if_temp_c(temp):
    """konwersja celsjuszy na farenheity i kelviny"""
    temp_F = (temp * 1.8) + 32
    temp_K = temp + 273.15
    print("Podana wartość: " + str(temp) + " stopnie w Celsjuszach to:")
    print("- temperatura w Farenheitach:\t" + str(temp_F))
    print("- temperatura w Kelvinach:\t" + str(temp_K))


def if_temp_f(temp):
    """konwersja farenheitów na celsjuszy i kelviny"""
    temp_C = (temp - 32) / 1.8
    temp_K = temp_C + 273.15
    print("Podana wartość: " + str(temp) + " stopnie w Farenheitach to:")
    print("- temperatura w Celsjuszach:\t" + str(temp_C))
    print("- temperatura w Kelvinach:\t" + str(temp_K))


def if_temp_k(temp):
    """konwersja kelvinów na celsjuszy i farenheity"""
    temp_C = temp - 273.15
    temp_F = (temp_C * 1.8) + 32
    print("Podana wartość: " + str(temp) + " stopnie w Celsjuszach to:")
    print("- temperatura w Celsjuszachh:\t" + str(temp_C))
    print("- temperatura w Farenheitach:\t" + str(temp_F))
    

"""część główna progarmu"""
# zapytanie o temperature
print("Konwerter temperatury.\n")
while True:
    temp_kind = input("****\nPodaj format temperatury (C, K, F)\n('q' aby zakończyć): ")
    temp_kind = temp_kind.lower()

    # wyjście z programu
    if temp_kind == 'q':
        print("Koniec")
        break;
    
    # wartość temperatury
    temp = float(input("Podaj wartość temperatury: "))

    # wybranie odpowiedniej funkcji konwersji
    if temp_kind == 'c':
        if_temp_c(temp)
    elif temp_kind == 'f':
        if_temp_f(temp)
    elif temp_kind == 'k':
        if_temp_k(temp)
    
