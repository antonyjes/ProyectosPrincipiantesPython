title = input("Ingrese título: ")

title = title.split()
acronimo = []

for word in title:
    #print(letter[0].upper())
    acronimo.append(word[0].upper())

print(''.join(acronimo))