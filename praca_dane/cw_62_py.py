# Napisz program proszący użytkownika o dane zawierające kilka
# pól (może to być np. lista zadań z opisem i terminami wykona-
# nia czy baza recenzji filmów) i zapisujący podane dane do pliku
# w wybranym formacie (CSV/JSON). Przy każdym uruchomie-
# niu program powinien odczytywać i wyświetlać wprowadzone
# wcześniej dane, umożliwiać ich usunięcie (po jednym wpisie)
# oraz dodanie nowych rekordów.

import csv

with open('exemplary.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',',quotechar = '"')
    line_number = 0
    lines = list()
    for row in csv_reader:
        if line_number == 0:
            print(f'{line_number} Column names are {",".join(row)}\n')
            line_number += 1
        else:
            print(f'{line_number} {row[0]} was realeased in {row[1]} and was rated by you as {row[2]}\n')
            line_number +=1

    delete = input('Type the number of row you want to delete, if you want to proceed press "c" ') 
    line_counter = 0
    if delete != 'c':
        if(int(delete)<=line_number):
            for row in csv_reader:
                lines.append(row)
                line_counter +=1
                if(line_number == delete):
                    lines.remove()

            with open('exemplary.csv', 'w') as write_deleted:
                delete_rec = csv.writer(write_deleted)
                delete_rec.writerows(lines)
        else:
            print('line number out of scope\n')
with open('exemplary.csv', 'a+') as csv_file:
    add_record = csv.writer(csv_file,delimiter=',', quotechar = '"')
    inp = input('Add new record, separate values by commas: ')
    new_record = inp.split(',')
    add_record.writerow(new_record)

            

