# Napisz skrypt, który pyta o imię, nazwisko i rok urodzenia
# (powinny być podane w jednej linii)

dane = input('Podaj imię, nazwisko i rok urodzenia oddzielone przecinkami: ')
dane_lista = dane.split(',')
print(f'Twoje imię to: {dane_lista[0]}, nazwisko: {dane_lista[1]}, data urodzenia: {dane_lista[2]}\n')