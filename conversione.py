from PIL import Image

def sovrapponi(pathImage, pathLogo, numeroImmagine):
    #print(pathImage + "  " + pathLogo)
    img1 = Image.open(pathImage)
    img2 = Image.open(pathLogo)

    # Ridimensiono per il logo
    new_width = 200
    new_height = int(new_width * img2.size[1] / img2.size[0])
    img2 = img2.resize((new_width, new_height))

    width1, height1 = img1.size
    width2, height2 = img2.size

    # Posizionamento del logo
    x = width1 - width2 - 30
    y = height1 - height2 - 30

    # Per mantenere la trasparenza del logo
    alpha = img2.getchannel('A')
    img2.putalpha(alpha)

    # Unione delle immagini
    img1.paste(img2, (x, y), img2)

    #Salvataggio delle immagini
    img1.save("immagine_sovrapposta" + str(numeroImmagine) + ".png")
