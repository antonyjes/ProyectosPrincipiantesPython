#singers = ['Michael Jackson', 'Ariana Grande', 'Ozuna']
#diccMichaelJackson = {'name': 'Michael Jackson', 'country': 'USA', 'songs': ['Billie Jean', 'Thriller', 'Smooth Criminal']}
#diccArianaGrande = {'name': 'ArianaGrande', 'country': 'USA', 'songs': ['7 rings', 'Thank you, next', 'Sweetener']}
#diccOzuna = {'name': 'Ozuna', 'country': 'Puerto Rico', 'songs': ['Criminal', 'Farsante', 'Adicto']}

singers = {1:{
    'name': 'Michael Jackson', 'songs': {'Billie Jean':"Lyrics of Billie Jean", 'Thriller': "Lyrics of Thriller", 'Smooth Criminal': "Lyrics of Smooth Criminal"}
},
2:{
    'name': 'Ariana Grande', 'songs': {'7 rings': "Lyrics of 7 rings", 'Thank you, next': "Lyrics of Thank you, next", 'Sweetener': "Lyrics of Sweetener"}
},
3:{
    'name': 'Ozuna', 'songs': {'Criminal': "Lyrics of Criminal", 'Farsante': "Lyrics of Farsante", 'Adicto': "Lyrics of Adicto"}
}}

print("***** Selecciona un artista ******\n")
for singer in singers:
    print(f"{singer}. {singers[singer]['name']}")

choice_singer = int(input("\nIngrese número de cantante: "))

print(f"\nEscogiste {singers[choice_singer]['name']}")


print("***** Selecciona una canción ******\n")
n=0
for song in singers[choice_singer]['songs']:
    n += 1
    print(f"{n}. {song}")

choice_song = input("\nIngrese nombre de la canción: ")

print(f"La letra de la canción es: {singers[choice_singer]['songs'][choice_song]}")
