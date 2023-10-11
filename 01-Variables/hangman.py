name = input("Name: ")
print(f"Hello {name} time to play hangman!")

toplam_hak = 10
kelime = "Can"
tahmin_edilecek_kelime = list()
for x in kelime:
    tahmin_edilecek_kelime.append("-")


while toplam_hak > 0:
    for index,_ in enumerate(range(len(kelime))):
        print(tahmin_edilecek_kelime[index])
    
    guess = input("Tahmin: ")
    if guess in kelime:
        index = kelime.index(guess)
        tahmin_edilecek_kelime[index] = guess
        
        print(tahmin_edilecek_kelime)

        if "".join(tahmin_edilecek_kelime) == kelime:
            print("Tebrikler başarılı oldunuz.")
            break
    elif guess not in kelime and toplam_hak > 0:
        toplam_hak -= 1
        print("Wrong")
        print(f"You have {toplam_hak} lives left")
    else:
        print("Öldünüz")