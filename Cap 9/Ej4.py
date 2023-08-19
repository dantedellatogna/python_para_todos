import Ej3

email_count = Ej3.email_count
larger = None

# for pair in email_count.keys(), email_count.items():
#    print(i)

for pair in email_count.items():
    if larger == None:
        larger = pair
    else:
        if pair[1] > larger[1]:
            larger = pair

print(f'Larger: {str(larger[0])} {str(larger[1])}')

for line in Ej3.file:
    line = line.split()
