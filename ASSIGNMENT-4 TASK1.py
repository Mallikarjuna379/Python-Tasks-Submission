import os

if os.path.exists('sample.txt'):
    file = open('sample.txt', 'r')
    print('Reading the file content:\n', file.read())
    file.close()
else:
    print("The file 'sample.txt' does not exist.")
