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

lbx_1 = Listbox(liste_fichiers,width=16,height=18)
lbx_1.place(x=0,y=0)
lbx_1.insert(0,"Video.mp4")
lbx_1.insert(1,"PAD.mxf")
lbx_1.insert(2,"Livraison PAD.mov")

lbx_2 = Listbox(liste_fichiers,width=33,height=18)
lbx_2.place(x=145,y=0)
lbx_2.insert(0,"Conforme XDCAM 4:2:2")
lbx_2.insert(1,"Non conforme")
lbx_2.insert(2,"Conforme XDCAM 4:2:2")

lbx_3 = Listbox(liste_fichiers,width=12,height=18)
lbx_3.place(x=443,y=0)
lbx_3.insert(0,"07/10/21")
lbx_3.insert(1,"04/12/93")
lbx_3.insert(2,"11/08/24")



"""Tableau liste des fichiers et informations"""
"""class ComboBox(Frame):
    def __init__(self, boss, item='', items=[], command='', width=10,
                 listSize=5):
        self.items = items
        self.command = command
        self.item = item
        self.entree = Entry(self, width=width)
        self.entree.insert(END, item)
        self.entree.bind("<Return>", self.sortieE)
        self.entree.pack(side=TOP)
        cadreLB = Frame(self)
        self.bListe = Listbox(cadreLB, height=listSize, width=width - 1)
        scrol = Scrollbar(cadreLB, command=self.bListe.yview)
        self.bListe.config(yscrollcommand=scrol.set)
        self.bListe.bind("<ButtonRelease-1>", self.sortieL)
        self.bListe.pack(side=LEFT)
        scrol.pack(expand=YES, fill=Y)
        cadreLB.pack()

        for it in items:
            self.bListe.insert(END, it)

            if __name__ == "__main__":  # --- Programme de test ---
                def changeCoul(col):
                    fenetre.configure(background=col)


                couleurs = ('navy', 'royal blue', 'steelblue1', 'cadet blue',
                            'lawn green', 'forest green', 'yellow', 'dark red',
                            'grey80', 'grey60', 'grey40', 'grey20', 'pink', 'red')

                Liste_fichiers = ComboBox(fenetre, item="néant", items=couleurs, command=changeCoul,
                                          width=30, listSize=6)
                Liste_fichiers.grid(row=1, columnspan=2, padx=10, pady=10)

"""

fenetre.mainloop()
