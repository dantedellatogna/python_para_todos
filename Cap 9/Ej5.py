fname = 'Cap 9\mbox-short.txt'

file = open(fname)

count_schools = dict()

for line in file:
    words = line.split()
    if len(words) > 0 and words[0] == 'From':
        index = words[1].find('@')
        school_domain = words[1][index+1:]
        count_schools[school_domain
                      ] = count_schools.get(school_domain, 0) + 1

print(count_schools)
