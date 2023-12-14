fname = 'mbox-short.txt'
file = open(fname)

hours = dict()

for line in file:
    words = line.split(' ')
    if len(words) > 0 and words[0] == 'From':
        hour = words[6].split(':')
        hours[hour[0]] = hours.get(hour[0], 0) + 1

lst_hours = list()

for hora, contador in list(hours.items()):
    lst_hours.append((hora, contador))

lst_hours.sort()

for hora, contador in lst_hours:
    print(hora, contador)