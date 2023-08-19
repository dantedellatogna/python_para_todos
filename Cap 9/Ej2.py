fname = 'python_para_todos\Cap 9\mbox-short.txt'

file = open(fname)
counts_days = dict()

for line in file:
    line = line.rstrip()
    words = line.split()

    if len(words) > 0 and words[0] == 'From':
        counts_days[words[2]] = counts_days.get(words[2], 0) + 1

print(counts_days)
