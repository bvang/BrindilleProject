from tkinter import *
from tkinter.filedialog import askdirectory

# Affichage
fenetre = Tk()
fenetre.title("Controle automatique des fichiers")
fenetre.minsize(700,600)
fenetre['bg']='white'
# Titre
cadf = Label(fenetre, text="Contrôle automatique de fichiers", font =("arial",20))
cadf.place(x=330,y=25)

# Logo INA
largeur = 50
hauteur = 50
image = PhotoImage(file="logo.png")
canvas = Canvas(fenetre, width=largeur,height=hauteur,bg='blue',bd=0,highlightthickness=0)
canvas.create_image(largeur/2, hauteur/2,image=image)
canvas.place(x=635,y=15)

nom = Label(fenetre, text="Nom")
nom.place(x=100, y=85)

statut = Label(fenetre, text="Statut")
statut.place(x=350, y=85)

date = Label(fenetre, text="Date")
date.place(x=550, y=85)


# Bouton Watchfolder
watchfolder = Label(fenetre, text="Watchfolder")
watchfolder.place(x=48, y=510)
bouton_1=Button(fenetre, text="Choisir ...", command=askdirectory, bg="grey")
bouton_1.place(x=55, y=540)

# Bouton Dossier Fichiers refusés
dossier_fichier_refuses = Label(fenetre, text="Dossier Fichiers refusés")
dossier_fichier_refuses.place(x=150, y=510)
bouton_2=Button(fenetre, text="Choisir ...", command=askdirectory, bg="grey")
bouton_2.place(x=190, y=540)

# Bouton Dossier XDCAM conformes
dossier_XDCAM_conformes = Label(fenetre, text="Dossier XDCAM conformes")
dossier_XDCAM_conformes.place(x=320, y=510)
bouton_3=Button(fenetre, text="Choisir ...", command=askdirectory, bg="grey")
bouton_3.place(x=360, y=540)

# Bouton Dossier PRORES conformes
dossier_PRORES_conformes = Label(fenetre, text="Dossier PRORES conformes")
dossier_PRORES_conformes.place(x=500, y=510)
bouton_4=Button(fenetre, text="Choisir ...", command=askdirectory, bg="grey")
bouton_4.place(x=545, y=540)

# Bouton Générer un rapport ...
bouton_5=Button(fenetre, text="Générer un rapport ...", command=askdirectory, bg="cyan",fg="gray")
bouton_5.place(x=370, y=420)

# Bouton Effacer la liste
bouton_6=Button(fenetre, text="Effacer la liste", command=askdirectory, bg="blue",fg="gray")
bouton_6.place(x=525, y=420)

#Liste des fichiers
liste_fichiers = Frame(fenetre, bg='green')
liste_fichiers.config(width=550,height=300)
liste_fichiers.place(x=70,y=110)

grille



fenetre.mainloop()
