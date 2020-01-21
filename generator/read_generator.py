def file_read(filepath):
    with open(filepath) as io:
        while True:
            line = io.readline()
            if line == '':
                break
            yield line.strip('\n')
        

for line in file_read('./generator/words.txt'):
    print(line)
