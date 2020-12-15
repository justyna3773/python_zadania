# Napisz skrypt realizujący funkcję zamka szyfrowego. Prosi o po-
# danie kodu i następnie sprawdza czy jest on zgodny z wcześniej
# wprowadzonym kodem

kod = input('Ustaw 6-cyfrowy kod dostępu: ')
for i in range(3):
    otwarcie = input('Podaj 6-cyfrowy kod dostępu: ')
    if(kod == otwarcie):
        print('Kod poprawny')
        break
    else:
        print('Kod niepoprawny')