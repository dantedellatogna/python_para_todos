fname = 'python_para_todos\Cap 9\mbox-short.txt'

file = open(fname)
email_count = dict()

for line in file:
    words = line.split()
    if len(words) > 0 and words[0] == 'From':
        email_count[words[1]] = email_count.get(words[1], 0) + 1

print(email_count)
