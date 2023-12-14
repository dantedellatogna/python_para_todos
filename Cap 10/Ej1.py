fname = 'Cap 10\mbox-short.txt'

file = open(fname)

emails = dict()

for line in file:
    words = line.split()
    if len(words) > 0 and words[0] == 'From':
        emails[words[1]] = emails.get(words[1], 0) + 1

lst_emails = list()
#lst_emails = list(emails.items())
for email, contador in list(emails.items()):
    lst_emails.append((contador, email))

lst_emails.sort(reverse=True)

for contador, email in lst_emails[:1]:
    print(contador, email)