def main():
    musics = [{
        "title": "sample title",
        "artist": "sample artist",
        "link": "sample link"
    }]
    # 1/7 => sauvegarder une musique (nom/artiste/lien) dans un array et lister les musiques
    print("##### My Playlists manager #####")
    while True:
        print("1) Sauvegarder une musique \n2) Lister les musiques \n3) Quitter")
        user_choice : int = int(input("Choisissez une option : "))
        if user_choice == 1:
            music_title: str = str(input("Nom de la musique : "))
            music_artist: str = str(input("Artiste de la musique : "))
            music_link: str = str(input("Lien de la musique : "))
            musics.append({"title": music_title, "artist": music_artist, "link": music_link})
        elif user_choice == 2:    
            for music in musics:
                print(f"\ntitre : {music['title']} \nartiste : {music['artist']} \nlien : {music['link']}\n")
        elif user_choice == 3:
            print("A bientot")
            break
        else:
            print("Choix invalide")    


if __name__ == "__main__":
    main()
