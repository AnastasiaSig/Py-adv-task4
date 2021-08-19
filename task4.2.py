import hashlib
import os
current_dir = os.getcwd()
file_name = 'countries_wikipedia.txt'
path = os.path.join(current_dir, file_name)

def hash_line(path):
    with open(path, encoding='UTF-8') as file:
        for line in file:
            hash_object = hashlib.md5(line.encode())
            yield hash_object.hexdigest()

for i in hash_line(path):
    print(i)

