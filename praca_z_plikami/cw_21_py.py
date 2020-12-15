# Napisz skrypt zliczający ilość plików w katalogu /dev, skorzystaj
# ze standardowej biblioteki - os


import os

path, directories, files = next(os.walk("/dev/"))
num_of_files= len(files)
print(num_of_files)