commands = input()
line_cnt = 0
symb_cnt = 0
max_len = 0
word_cnt = 0
line = input()
while line != '#':
    line_cnt += 1
    symb_cnt += len(line)
    max_len = max(max_len, len(line))
    line1 = line.split(' ')
    for word in line1:
        if word != '':
            word_cnt += 1
    line = input()


commands = commands.split(' ')
if '-l' in commands:
    print(line_cnt, end=' ')
if '-w' in commands:
    print(word_cnt, end=' ')
if '-m' in commands:
    print(symb_cnt, end=' ')
if '-L' in commands:
    print(max_len, end=' ')
