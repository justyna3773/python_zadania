import os
full_path = '/home/ultramarine/Desktop/python_rozwiazania/praca_z_plikami/pictures'
for file in os.scandir('./pictures/'):
    if file.path.endswith('.jpg'):
        os.rename(file.path, file.path.rstrip('.jpg') + '.png')

