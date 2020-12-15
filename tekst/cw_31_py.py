#.....nie działa 
words_to_remove = ['się', 'i', 'oraz', 'nigdy', 'dlaczego']
# with open('3sat.txt', 'w') as file:
#     lines = file.readlines()
#     for line in lines:
#         for word in words_to_remove:
#             line.replace(word,'')

f_in = open('3sat.txt', 'rt')
data = f_in.read()

for word in words_to_remove:
    data = data.replace(word, '')
f_in.close()

f_in = open('3sat.txt', 'wt')
f_in.write(data)
f_in.close()

