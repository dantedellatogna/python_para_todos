import string

fname = 'mbox-short.txt'
file = open(fname)

dict_letras = dict()
lst_lower = list(string.ascii_lowercase)
lst_letras = list()

for line in file:
    line = line.lower()
    for letter in line:
        if letter in lst_lower:
            dict_letras[letter] = dict_letras.get(letter, 0) + 1

for letra, contador in list(dict_letras.items()):
    lst_letras.append((contador, letra))

lst_letras.sort(reverse=True)

for contador, letra in lst_letras:
    print(letra, contador)