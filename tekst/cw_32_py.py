# Napisz skrypt zmieniający w podanym ciągu wejściowym
# (wybierz kilka plików z repozytorium: Tekstowego) następu-
# jące słowa : i, oraz, nigdy, dlaczego na następujący zestaw słów :
# oraz, i, prawie nigdy, czemu. Zalecaną strukturą jest słownik.

replace_dict = { 'i':'oraz', 'oraz':'i', 'nigdy': 'prawie nigdy', 'dlaczego': 'czemu'}

# with open('3sat.txt', 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         for key in replace_dict:
#             line.replace(key,replace_dict[key])
#     file.close()

# with open('3sat.txt', 'w') as file_1:
#     file_1.writelines(lines)
#     file_1.close()
f_in = open('3sat.txt', 'rt')
data = f_in.read()
new_data = []
for word in data.split(' '):
    new_data.append(replace_dict.get(word,word))
f_in.close()

f_in = open('3sat.txt', 'wt')
f_in.write(' '.join(new_data))
f_in.close()

#prawie dobrze działa
