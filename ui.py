import tkinter as tk
from tkinter import filedialog, messagebox
import conversione
import os


pathLogo = ""
pathImage = ""
# Seleziona le immagini a cui applicare il logo
def selectFile():
    global pathImage
    filetypes = (("JPEG files", "*.jpg"), ("PNG files", "*.png"))
    pathImage = filedialog.askopenfilenames(filetypes = filetypes)
    print(pathImage)

# Seleziona il logo da applicare alle immagini
def selectLogo():
    global pathLogo
    filetypes = (("JPEG files", "*.jpg"), ("PNG files", "*.png"))
    pathLogo = filedialog.askopenfilename(filetypes = filetypes)    

# Avvia la conversione di ciascuna immagine selezionata
def avvia_conversione():
    global pathImage
    global pathLogo
    if pathImage and pathLogo:
        for i, singolaImmagine in enumerate(pathImage):
            conversione.sovrapponi(singolaImmagine, pathLogo, i); 
        messagebox.showinfo("Avviso", "Le operazioni sono state completate")
    else:
        messagebox.showinfo("Errore", "È necessario selezionare le immagini")            

window = tk.Tk()

window.title("Logo Applier")

font_family = "Helvetica"
font_size = 24
font_size_sottotitolo = 15
font_weight = "bold"

# parte superiore della app
framePrimoBottone = tk.Frame(window)
framePrimoBottone.pack(padx=10, pady=10)

titolo = tk.Label(framePrimoBottone, text="Logo Applier")
sottotitolo = tk.Label(framePrimoBottone, text="Seleziona le foto a cui vuoi applicare il logo")
button = tk.Button(framePrimoBottone, text="Seleziona file", command=selectFile)

# Imposta la formattazione del testo
titolo.config(font=(font_family, font_size, font_weight))
sottotitolo.config(font=(font_family, font_size_sottotitolo, font_weight))
titolo.pack()
sottotitolo.pack()
button.pack()

# parte inferiore dell'app della app
frameSecondoBottone = tk.Frame(window)
frameSecondoBottone.pack(padx=10, pady=10)

buttonLogo = tk.Button(frameSecondoBottone, text="Seleziona file", command=selectLogo)
sottotitolo2 = tk.Label(frameSecondoBottone, text="Seleziona il logo che vuoi applicare alle foto")
sottotitolo2.config(font=(font_family, font_size_sottotitolo, font_weight))
sottotitolo2.pack()
buttonLogo.pack()


# parte terminale dell'app
frameTerzoBottone = tk.Frame(window)
frameTerzoBottone.pack(padx=10, pady=10)

buttonProcedi = tk.Button(frameTerzoBottone, text="Insert Logo", command=avvia_conversione)
buttonProcedi.pack()

# diamo una dimensione fissata iniziale all'app
window.minsize(400, 300)

window.mainloop()