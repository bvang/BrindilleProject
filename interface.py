from tkinter import *
from tkinter import ttk
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

# Cadre + Scrol
cadre = ttk.Treeview(fenetre,selectmode='browse')
scrol = ttk.Scrollbar(orient="vertical",command=cadre.yview)
cadre.configure(yscrollcommand=scrol.set)

# Configuration du cadre
cadre.place(x = 70, y = 110, width=550,height=293)
cadre["columns"] = ("1", "2","3")
cadre['show'] = 'headings'
cadre.column("1", width=150)
cadre.column("2", width=20, anchor='c')
cadre.column("3", width=50, anchor='c')
cadre.heading("1", text="Fichier")
cadre.heading("2", text="Statut")
cadre.heading("3", text="Date")
c = "Conforme"
nc = "Non conforme"

# Remplissage du cadre
cadre.insert("",'end',text="L1",values=("Loup.mp4",c,"03/03/0303"))
cadre.insert("",'end',text="L2",values=("Fleur.mov",nc,"12/12/1212"))
cadre.insert("",'end',text="L3",values=("Tigre.mxf",nc,"12/12/1212"))
cadre.insert("",'end',text="L4",values=("Tigre.mxf",nc,"12/12/1212"))
cadre.insert("",'end',text="L5",values=("Tigre.mxf",nc,"12/12/1212"))
cadre.insert("",'end',text="L6",values=("Tigre.mxf",nc,"12/12/1212"))
cadre.insert("",'end',text="L7",values=("Tigre.mxf",c,"12/12/1212"))
cadre.insert("",'end',text="L8",values=("Tigre.mxf",c,"12/12/1212"))
cadre.insert("",'end',text="L9",values=("Tigre.mxf",nc,"12/12/1212"))
cadre.insert("",'end',text="L10",values=("Tigre.mxf",nc,"12/12/1212"))
cadre.insert("",'end',text="L11",values=("Tigre.mxf",nc,"12/12/1212"))
cadre.insert("",'end',text="L12",values=("Tigre.mxf",nc,"12/12/1212"))
cadre.insert("",'end',text="L13",values=("Tigre.mxf",c,"12/12/1212"))
cadre.insert("",'end',text="L14",values=("Tigre.mxf",nc,"12/12/1212"))
cadre.insert("",'end',text="L15",values=("Tigre.mxf",nc,"12/12/1212"))
cadre.insert("",'end',text="L16",values=("Tigre.mxf",nc,"12/12/1212"))
cadre.insert("",'end',text="L17",values=("Tigre.mxf",nc,"12/12/1212"))
cadre.insert("",'end',text="L18",values=("Tigre.mxf",nc,"12/12/1212"))
cadre.insert("",'end',text="L19",values=("Tigre.mxf",c,"12/12/1212"))
cadre.insert("",'end',text="L20",values=("Tigre.mxf",nc,"12/12/1212"))
cadre.insert("",'end',text="L21",values=("Tigre.mxf",nc,"12/12/1212"))
cadre.insert("",'end',text="L22",values=("Tigre.mxf",nc,"12/12/1212"))
cadre.insert("",'end',text="L23",values=("Tigre.mxf",nc,"12/12/1212"))

# Fin du programme
fenetre.mainloop()
