from pprint import pprint
from pymediainfo import MediaInfo
import glob, os
from os import listdir
from os.path import isfile, join
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import filedialog
import shutil
from pathlib import Path

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PRORES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# General
prores_format_general = "MPEG-4"  # à ajouter
prores_type = "QuickTime"

# Other
prores_timecode = "00:00:00:00"

# Video
prores_compression = "ProRes"
prores_profile = "422 HQ"
prores_bitrate = ['184 Mb/s']  # à ajouter
prores_width = "1920"
prores_height = "1080"
prores_framerate = ['25.000 FPS']
prores_scan_type = ['Interlaced']
prores_scan_order = ['Top Field First']

# Audio
prores_audio_type = "PCM"
prores_sampling_rate = ['48.0 kHz']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MXF~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# General
mxf_format_general = "MXF"
mxf_format_profile = "OP-1a"

# Video
mxf_compression = "MPEG Video"
mxf_format_version = "Version 2"
mxf_profile = "422 HQ"  # à revoir
mxf_bitrate = ['50 Mb/s']
mxf_width = "1920"
mxf_height = "1080"
mxf_framerate = ['25.000 FPS']
mxf_bitdepth = "10 bits"
mxf_scan_type = ['Interlaced']
mxf_scan_order = ['Top Field First']

# Audio
mxf_audio_type = "PCM"
mxf_sampling_rate = ['48.0 kHz']

# Other
mxf_timecode = "00:00:00:00"


def prores_verif(filename):
    os.chdir(filename)
    for file in glob.glob("*.mov"):
        print("Le nom du fichier est :", file)
        media_info = MediaInfo.parse(file)
        for track in media_info.tracks:
            #########VIDEO################
            if track.track_type == "Video":
                pprint(track.track_type)
                print(" Format: {t.format}\n Format profile: {t.format_profile}\n Bit rate: {t.other_bit_rate}\n "
                      "Width: {t.sampled_width} pixels\n Height: {t.sampled_height} pixels\n Frame rate: {t.other_frame_rate}\n "
                      "Scan type: {t.other_scan_type}\n Scan order: {t.other_scan_order}\n"
                      " Bit-(Pixel*Frame): {t.bits__pixel_frame}\n"
                      .format(t=track))
                if track.format == prores_compression and track.format_profile == prores_profile \
                        and track.sampled_width == prores_width and track.sampled_height == prores_height \
                        and track.other_frame_rate == prores_framerate and track.other_scan_type == prores_scan_type \
                        and track.other_scan_order == prores_scan_order and float(track.bits__pixel_frame) > 1:
                    # print("partie Video conforme PRORES HQ\n")
                    video_prores = True
                    continue
                else:
                    print("partie Video non conforme PRORES HQ\n")
                    video_prores = False
                    continue

            ################GENERAL##################
            elif track.track_type == "General":
                pprint(track.track_type)
                print(" Format : {t.format}\n Format profile : {t.format_profile}\n".format(t=track))
                if track.format_profile == prores_type and track.format == prores_format_general:
                    general_prores = True
                    continue
                else:
                    print("partie General non conforme PRORES HQ\n")
                    general_prores = False
                    continue

            ################AUDIO##################
            elif track.track_type == "Audio":
                pprint(track.track_type)
                print(" Format: {t.format}\n Sampling rate: {t.other_sampling_rate}\n"
                      .format(t=track))
                if track.format == "PCM" and track.other_sampling_rate == ['48.0 kHz']:
                    # print("\npartie Audio conforme PRORES HQ")
                    audio_prores = True
                    continue
                else:
                    print("\npartie Audio non conforme PRORES HQ\n")
                    audio_prores = False
                    continue

            ################OTHER##################
            elif track.track_type == "Other":
                pprint(track.track_type)
                print(" TIM: {t.time_code_of_first_frame}\n".format(t=track))
                if track.time_code_of_first_frame == prores_timecode:
                    other_prores = True
                    if video_prores and audio_prores and general_prores and other_prores:
                        print(file, ": VIDEO CONFORME PRORES HQ\n")
                        # videoall_verif = True
                        # return videoall_verif
                        continue
                    else:
                        print(file, ": VIDEO NON CONFORME PRORES HQ\n")
                        # videoall_verif = False
                        # return videoall_verif
                        continue
                else:
                    print("partie Other non conforme PRORES HQ\n")
                    other_prores = False
                    print(file, ": VIDEO NON CONFORME PRORES HQ\n")
                    # videoall_verif = False
                    # return videoall_verif
                    continue

            elif not track.track_type == "General" or not track.track_type == "Other" or not track.track_type == "Audio":
                print(file, ": VIDEO NON CONFORME PRORES HQ\n")
                continue


def mxf_verif():
    for file in glob.glob("*.mxf"):
        print("Le nom du fichier est :", file)
        media_info = MediaInfo.parse(file)
    for track in media_info.tracks:

        ############VIDEO################
        if track.track_type == "Video":
            pprint(track.track_type)
            print(" Format: {t.format}\n Format version: {t.format_version}\n Format profile: {t.format_profile}\n"
                  " Bit rate: {t.other_bit_rate}\n Width: {t.sampled_width} pixels\n Height: {t.sampled_height} pixels\n"
                  " Frame rate: {t.other_frame_rate}\n Bit depth: {t.other_bit_depth}\n Scan type: {t.other_scan_type}\n"
                  " Scan order: {t.other_scan_order}\n Bit-(Pixel*Frame): {t.bits__pixel_frame}\n"
                  .format(t=track))
            if track.format == mxf_compression and track.format_version == mxf_format_version \
                    and track.format_profile == mxf_profile and track.other_bit_rate == mxf_bitrate \
                    and track.sampled_width == mxf_width and track.sampled_height == mxf_height \
                    and track.other_frame_rate == mxf_framerate and track.other_bit_depth == mxf_bitdepth \
                    and track.other_scan_type == mxf_scan_type and track.other_scan_order == mxf_scan_order \
                    and float(track.bits__pixel_frame) > 0.7:
                # print("partie Video conforme PRORES HQ\n")
                video_prores = True
            else:
                print("partie Video non conforme PRORES HQ\n")
                video_prores = False

        ################GENERAL##################
        elif track.track_type == "General":
            pprint(track.track_type)
            print(" Format : {t.format}\n Format profile : {t.format_profile}\n".format(t=track))
            if track.format_profile == prores_type and track.format == prores_format_general:
                general_prores = True
            else:
                print("partie General non conforme PRORES HQ\n")
                general_prores = False

        ################AUDIO##################
        elif track.track_type == "Audio":
            pprint(track.track_type)
            print(" Format: {t.format}\n Sampling rate: {t.other_sampling_rate}"
                  .format(t=track))
            if track.format == "PCM" and track.other_sampling_rate == ['48.0 kHz']:
                # print("\npartie Audio conforme PRORES HQ")
                audio_prores = True
                if video_prores and audio_prores and general_prores:
                    print("\nVIDEO CONFORME PRORES HQ")
                    videoall_verif = True
                    return videoall_verif
                else:
                    print("\nVIDEO NON CONFORME PRORES HQ")
                    videoall_verif = False
                    return videoall_verif
            else:
                print("\npartie Audio non conforme PRORES HQ\n")
                audio_prores = False



        ################OTHER##################
        elif track.track_type == "Other":
            pprint(track.track_type)
            print(" TIM: {t.time_code_of_first_frame}\n".format(t=track))
            if track.time_code_of_first_frame == prores_timecode:
                other_prores = True
                if video_prores and audio_prores and general_prores and other_prores:
                    print("\nVIDEO CONFORME PRORES HQ")
                    videoall_verif = True
                    return videoall_verif
                else:
                    print("\nVIDEO NON CONFORME PRORES HQ")
                    videoall_verif = False
                    return videoall_verif
            else:
                print("partie Other non conforme PRORES HQ\n")
                other_prores = False
                if video_prores and audio_prores and general_prores and other_prores:
                    print("\nVIDEO CONFORME PRORES HQ")
                    videoall_verif = True
                    return videoall_verif
                else:
                    print("\nVIDEO NON CONFORME PRORES HQ")
                    videoall_verif = False
                    return videoall_verif


# Affichage
fenetre = Tk()
fenetre.title("Controle automatique des fichiers")
fenetre.minsize(700, 600)
fenetre['bg'] = 'white'
# Titre
cadf = Label(fenetre, text="Contrôle automatique de fichiers", font=("arial", 20))
cadf.place(x=330, y=25)

# Logo INA
largeur = 50
hauteur = 50
image = PhotoImage(file="G:\Documents\GitHub\BrindilleProject\logo.png")
canvas = Canvas(fenetre, width=largeur, height=hauteur, bg='blue', bd=0, highlightthickness=0)
canvas.create_image(largeur / 2, hauteur / 2, image=image)
canvas.place(x=635, y=15)

nom = Label(fenetre, text="Nom")
nom.place(x=100, y=85)

statut = Label(fenetre, text="Statut")
statut.place(x=350, y=85)

date = Label(fenetre, text="Date")
date.place(x=550, y=85)


def browsefolder():
    os.chdir("G:/Documents/testFichier")
    for file in glob.glob("*.mov"):
        print("Le nom du fichier est :", file)
        filedialog.askopenfilename(initialdir="/", title="Select a File",
                                   filetype=(("jpeg files", "*.jpg"), ("all files", "*.*")))


def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)
    os.chdir(filename)
    prores_verif(filename)
    dossier_watchfolder = Label(fenetre, text=filename)
    dossier_watchfolder.place(x=10, y=570)
    for file in glob.glob("*.mov"):
        print("Le nom du fichier est :", file)
        return file


def choose_folder_refused():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)
    os.chdir(filename)
    dossier_fichier_refuses_confirm = Label(fenetre, text=filename)
    dossier_fichier_refuses_confirm.place(x=150, y=570)


def choose_folder_xdcam():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)
    os.chdir(filename)
    dossier_fichier_refuses_confirm = Label(fenetre, text=filename)
    dossier_fichier_refuses_confirm.place(x=300, y=570)


def choose_folder_prores():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)
    os.chdir(filename)
    dossier_fichier_refuses_confirm = Label(fenetre, text=filename)
    dossier_fichier_refuses_confirm.place(x=500, y=570)


# Bouton Watchfolder
folder_path = StringVar()
watchfolder = Label(fenetre, text="Watchfolder")
watchfolder.place(x=48, y=510)
bouton_1 = Button(fenetre, text="Choisir ...", command=browse_button, bg="grey")
bouton_1.place(x=55, y=540)

# Bouton Dossier Fichiers refusés
dossier_fichier_refuses = Label(fenetre, text="Dossier Fichiers refusés")
dossier_fichier_refuses.place(x=150, y=510)
bouton_2 = Button(fenetre, text="Choisir ...", command=choose_folder_refused, bg="grey")
bouton_2.place(x=190, y=540)

# Bouton Dossier XDCAM conformes
dossier_XDCAM_conformes = Label(fenetre, text="Dossier XDCAM conformes")
dossier_XDCAM_conformes.place(x=320, y=510)
bouton_3 = Button(fenetre, text="Choisir ...", command=choose_folder_xdcam, bg="grey")
bouton_3.place(x=360, y=540)

# Bouton Dossier PRORES conformes
dossier_PRORES_conformes = Label(fenetre, text="Dossier PRORES conformes")
dossier_PRORES_conformes.place(x=500, y=510)
bouton_4 = Button(fenetre, text="Choisir ...", command=choose_folder_prores, bg="grey")
bouton_4.place(x=545, y=540)

# Bouton Générer un rapport ...
bouton_5 = Button(fenetre, text="Générer un rapport ...", command=askdirectory, bg="cyan", fg="gray")
bouton_5.place(x=370, y=420)

# Bouton Effacer la liste
bouton_6 = Button(fenetre, text="Effacer la liste", command=askdirectory, bg="blue", fg="gray")
bouton_6.place(x=525, y=420)

# Liste des fichiers
liste_fichiers = Frame(fenetre, bg='green')
liste_fichiers.config(width=550, height=300)
liste_fichiers.place(x=70, y=110)

lbx_1 = Listbox(liste_fichiers, width=16, height=18)
lbx_1.place(x=0, y=0)
onlyfiles = [f for f in listdir("G:/Documents/testFichier") if isfile(join("G:/Documents/testFichier", f))]
lbx_1.insert(0, browse_button)
lbx_1.insert(1, onlyfiles)
lbx_1.insert(2, "Livraison PAD.mov")

lbx_2 = Listbox(liste_fichiers, width=33, height=18)
lbx_2.place(x=145, y=0)
lbx_2.insert(0, "Conforme XDCAM 4:2:2")
lbx_2.insert(1, "Non conforme")
lbx_2.insert(2, "Conforme XDCAM 4:2:2")

lbx_3 = Listbox(liste_fichiers, width=12, height=18)
lbx_3.place(x=443, y=0)
lbx_3.insert(0, "07/10/21")
lbx_3.insert(1, "04/12/93")
lbx_3.insert(2, "11/08/24")

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
