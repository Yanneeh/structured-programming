
f = open('file.txt')

text = f.readlines()

lst = []

for line in text:
    line = line.rstrip().strip('\\n ')

    if line != '':
        lst.append(line)

f = open('new_file.txt', 'w')

for item in lst:
    f.write(item)
