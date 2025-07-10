
def jakiKajak():
    print('\nDostępne kajaki: \n - jednoosobowe \n - dwuosobowe')
    kajak = input('\nJeśli wybierasz kajak jednoosobowy wpisz 1, a jeśli dwuosobowy wpisz 2: ')

    if kajak == "1":
        while True:
            try:
                print('Wybrałeś kajak jednoosobowy! Wpisz odległość i zobacz ile wyniesie Cię wycieczka.')
                odleglosc_input = float(input('Podaj odległość (maksymalna - 37km) (km): '))
                if odleglosc_input <= 37:
                    pierwszy_obiekt = KajakiJednoosobowe(odleglosc=odleglosc_input)
                    pierwszy_obiekt.pokaz()
                    przekieruj = input('Wpisz 2, jeśli chcesz zobaczyć też dwuosobowe kajaki: ')
                    if przekieruj == "2":
                        drugi_obiekt = KajakiDwuosobowe(odleglosc=odleglosc_input)
                        drugi_obiekt.pokaz()
                    break
                else:
                    print("Maksymalna odległość którą możesz przepłynąć to 37km!")
            except ValueError:
                print("Podano nieprawidłową wartość. Wpisz liczbę.")

    elif kajak == "2":
        while True:
            try:
                odleglosc_input = float(input('Podaj odległość (km): '))
                drugi_obiekt = KajakiDwuosobowe(odleglosc=odleglosc_input)
                drugi_obiekt.pokaz()
                break
            except ValueError:
                print("Podano nieprawidłową wartość. Wpisz liczbę.")
    else:
        print('Musisz wybrać 1 albo 2!!')


class KajakiJednoosobowe:
    def __init__(self, odleglosc):
        self.odleglosc = odleglosc
        self.koszt_wycieczki = self.odleglosc * 7

    def pokaz(self):
        print(f'Długość trasy wynosi {self.odleglosc} km')
        print("ZA KAJAKI JEDNOOSOBOWE!")
        print(f'Koszt trasy wyniesie (kajak jednoosobowy): {self.koszt_wycieczki} zł')


class KajakiDwuosobowe:
    def __init__(self, odleglosc):
        self.odleglosc = odleglosc
        self.koszt_wycieczki = self.odleglosc * 10

    def pokaz(self):
        print(f'Długość trasy wynosi {self.odleglosc} km')
        print("ZA KAJAKI DWUOSOBOWE!")
        print(f'Koszt trasy wyniesie (kajak dwuosobowy): {self.koszt_wycieczki} zł')

jakiKajak()
