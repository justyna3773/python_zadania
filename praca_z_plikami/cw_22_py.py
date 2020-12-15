import os
set_path = '/dev/'
for path, directories, files in os.walk(set_path):
    for filename in files:
        print(os.path.join(path, filename))
    for dirname in directories:
        print(os.path.join(path, dirname))