from pprint import pprint
from pymediainfo import MediaInfo
import glob, os
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import filedialog
import shutil
import time
import tkinter as tk
from datetime import datetime

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~métadonnées PRORES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# General
prores_format_general = "MPEG-4"
prores_type = "QuickTime"

# Other
prores_timecode = "00:00:00:00"

# Video
prores_compression = "ProRes"
prores_profile = "422 HQ"
prores_bitrate = ['184 Mb/s']
prores_width = "1920"
prores_height = "1080"
prores_framerate = ['25.000 FPS']
prores_scan_type = ['Interlaced']
prores_scan_order = ['Top Field First']

# Audio
prores_audio_type = "PCM"
prores_sampling_rate = ['48.0 kHz']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~métadonnées MXF~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# General
mxf_format_general = "MXF"
mxf_format_profile = "OP-1a"

# Video
mxf_compression = "MPEG Video"
mxf_format_version = "Version 2"
mxf_profile = "4:2:2@High"  # à revoir
mxf_bitrate = ['50 Mb/s']
mxf_width = "1920"
mxf_height = "1080"
mxf_framerate = ['25.000 FPS']
mxf_bitdepth = ['10 bits']
mxf_scan_type = ['Interlaced']
mxf_scan_order = ['Top Field First']

# Audio
mxf_audio_type = "PCM"
mxf_sampling_rate = ['48.0 kHz']

# Other
mxf_timecode = "00:00:00:00"

#Fonction principale qui permettra d'analyser les fichiers selon les dossiers en comparant les métadonnées des fichiers
#aux constantes que nous avons déclarées au-dessus
def video_verif():
    filename = filedialog.askdirectory(title='Select WatchFolder')
    filename_refused = filedialog.askdirectory(title='Select Refused Folder')
    filename_prores = filedialog.askdirectory(title='Select PRORES Folder')
    filename_xdcam = filedialog.askdirectory(title='Select XDCAM Folder')

    folder_path.set(filename)
    os.chdir(filename)
    #while os.listdir(filename):
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~VERIF PRORES HQ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    for file in glob.glob("*.mov"):
        ts = time.time()
        now = datetime.fromtimestamp(ts)
        print("Le nom du fichier est :", file)
        # filepath = (filename + '/' + file)
        media_info = MediaInfo.parse(filename + '/' + file)
        for track in media_info.tracks:
            #########VIDEO################
            if track.track_type == "Video":
                #pprint(track.track_type)
                # print(" Format: {t.format}\n Format profile: {t.format_profile}\n Bit rate: {t.other_bit_rate}\n "
                #      "Width: {t.sampled_width} pixels\n Height: {t.sampled_height} pixels\n Frame rate: {t.other_frame_rate}\n "
                #      "Scan type: {t.other_scan_type}\n Scan order: {t.other_scan_order}\n"
                #      " Bit-(Pixel*Frame): {t.bits__pixel_frame}\n"
                #      .format(t=track))
                if track.format == prores_compression and track.format_profile == prores_profile \
                        and track.sampled_width == prores_width and track.sampled_height == prores_height \
                        and track.other_frame_rate == prores_framerate and track.other_scan_type == prores_scan_type \
                        and track.other_scan_order == prores_scan_order and float(track.bits__pixel_frame) > 1\
                        and track.other_bit_rate == prores_bitrate:
                    # print("partie Video conforme PRORES HQ\n")
                    video_prores = True
                    continue
                else:
                    print("partie Video non conforme PRORES HQ\n")
                    video_prores = False
                    continue

            ################GENERAL##################
            elif track.track_type == "General":
                #pprint(track.track_type)
                # print(" Format : {t.format}\n Format profile : {t.format_profile}\n".format(t=track))
                if track.format_profile == prores_type and track.format == prores_format_general:
                    general_prores = True
                    continue
                else:
                    print("partie General non conforme PRORES HQ\n")
                    general_prores = False
                    continue

            ################AUDIO##################
            elif track.track_type == "Audio":
                #pprint(track.track_type)
                # print(" Format: {t.format}\n Sampling rate: {t.other_sampling_rate}\n"
                #      .format(t=track))
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
                #pprint(track.track_type)
                # print(" TIM: {t.time_code_of_first_frame}\n".format(t=track))
                if track.time_code_of_first_frame == prores_timecode:
                    other_prores = True
                    if video_prores and audio_prores and general_prores and other_prores:
                        print(file, ": VIDEO CONFORME PRORES HQ\n")
                        moveto_prores(filename, file, filename_prores)
                        cadre.insert("", 'end', text="L1", values=(file, "Conforme", now))
                        # videoall_verif = True
                        # return videoall_verif
                        continue
                    else:
                        print(file, ": VIDEO NON CONFORME PRORES HQ\n")
                        # videoall_verif = False
                        # return videoall_verif
                        moveto_refused(filename, file, filename_refused)
                        cadre.insert("", 'end', text="L1", values=(file, "Non conforme", now))
                        continue
                else:
                    print("partie Other non conforme PRORES HQ\n")
                    other_prores = False
                    print(file, ": VIDEO NON CONFORME PRORES HQ\n")
                    moveto_refused(filename, file, filename_refused)
                    cadre.insert("", 'end', text="L1", values=(file, "Non conforme", now))
                    # videoall_verif = False
                    # return videoall_verif
                    continue

            elif not track.track_type == "General" or not track.track_type == "Other" or not track.track_type == "Audio":
                print(file, ": VIDEO NON CONFORME PRORES HQ\n")
                moveto_refused(filename, file, filename_refused)
                cadre.insert("", 'end', text="L1", values=(file, "Non conforme", now))
                continue
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~VERIF XDCAM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    for file in glob.glob("*.mxf"):
        ts = time.time()
        now = datetime.fromtimestamp(ts)
        print("Le nom du fichier est :", file)
        # filepath = (filename + '/' + file)
        media_info = MediaInfo.parse(filename + '/' + file)
        for track in media_info.tracks:
            #########VIDEO################
            if track.track_type == "Video":
                #pprint(track.track_type)
                 print(" Format: {t.format}\n Format profile: {t.format_profile}\n Bit rate: {t.other_bit_rate}\n "
                      "Width: {t.sampled_width} pixels\n Height: {t.sampled_height} pixels\n Frame rate: {t.other_frame_rate}\n "
                      "Scan type: {t.other_scan_type}\n Scan order: {t.other_scan_order}\n"
                      " Bit-(Pixel*Frame): {t.bits__pixel_frame}\n"
                      .format(t=track))
                 if track.format == mxf_compression and track.format_version == mxf_format_version \
                        and track.format_profile == mxf_profile and track.other_bit_rate == mxf_bitrate \
                        and track.sampled_width == mxf_width and track.sampled_height == mxf_height \
                        and track.other_frame_rate == mxf_framerate and track.other_bit_depth == mxf_bitdepth \
                        and track.other_scan_type == mxf_scan_type and track.other_scan_order == mxf_scan_order \
                        and float(track.bits__pixel_frame) > 0.7:
                    video_xdcam = True
                    continue
                 else:
                    print("partie Video non conforme XDCAM\n")
                    video_xdcam = False
                    continue

            ################GENERAL##################
            elif track.track_type == "General":
                #pprint(track.track_type)
                # print(" Format : {t.format}\n Format profile : {t.format_profile}\n".format(t=track))
                if track.format == mxf_format_general and track.format_profile == mxf_format_profile:
                    general_xdcam = True
                    continue
                else:
                    print("partie General non conforme XDCAM\n")
                    general_xdcam = False
                    continue

            ################AUDIO##################
            elif track.track_type == "Audio":
                #pprint(track.track_type)
                # print(" Format: {t.format}\n Sampling rate: {t.other_sampling_rate}\n"
                #      .format(t=track))
                if track.stream_identifier == 0:
                    if track.format == "PCM" and track.other_sampling_rate == ['48.0 kHz']:
                        # print("\npartie Audio conforme PRORES HQ")
                        audio_xdcam = True
                        continue
                    else:
                        print("\npartie Audio non conforme XDCAM\n")
                        audio_xdcam = False
                        continue

            ################OTHER##################
            elif track.track_type == "Other":
                #pprint(track.track_type)
                # print(" TIM: {t.time_code_of_first_frame}\n".format(t=track))
                if track.stream_identifier == 0:
                    if track.time_code_of_first_frame == mxf_timecode:
                        other_xdcam = True
                        if video_xdcam and audio_xdcam and general_xdcam and other_xdcam:
                            print(file, ": VIDEO CONFORME XDCAM\n")
                            moveto_xdcam(filename, file, filename_xdcam)
                            cadre.insert("", 'end', text="L1", values=(file, "Conforme", now))
                            # videoall_verif = True
                            # return videoall_verif
                            continue
                        else:
                            print(file, ": VIDEO NON CONFORME XDCAM\n")
                            # videoall_verif = False
                            # return videoall_verif
                            moveto_refused(filename, file, filename_refused)
                            cadre.insert("", 'end', text="L1", values=(file, "Non conforme", now))
                            continue
                    else:
                        print("partie Other non conforme XDCAM\n")
                        other_xdcam = False
                        print(file, ": VIDEO NON CONFORME XDCAM\n")
                        moveto_refused(filename, file, filename_refused)
                        cadre.insert("", 'end', text="L1", values=(file, "Non conforme", now))
                        # videoall_verif = False
                        # return videoall_verif
                        continue

            elif not track.track_type == "General" or not track.track_type == "Other" or not track.track_type == "Audio":
                print(file, ": VIDEO NON CONFORME XDCAM\n")
                moveto_refused(filename, file, filename_refused)
                cadre.insert("", 'end', text="L1", values=(file, "Non conforme", now))
                continue
    #while not os.listdir(filename):
    #    cadre.insert("", 'end', text="L1", values=("file", "yes", "oui"))
    #    if os.listdir(filename):    #until: os.listdir(filename)
    #        time.sleep(10)
    #        pass
    #    else:
    #        continue


# Affichage
fenetre = Tk()
fenetre.title("Contrôle automatique des fichiers")
fenetre.minsize(700, 600)
fenetre['bg'] = 'white'
# Titre
cadf = Label(fenetre, text="Contrôle automatique de fichiers", font=("arial", 20))
cadf.place(x=280, y=25)

# Logo INA
"""largeur = 50
hauteur = 50
image = PhotoImage(file="logo.png")
canvas = Canvas(fenetre, width=largeur, height=hauteur, bg='blue', bd=0, highlightthickness=0)
canvas.create_image(largeur / 2, hauteur / 2, image=image)
canvas.place(x=635, y=15)"""


def choose_folder_refused():
    global folder_path
    filename_refused = filedialog.askdirectory(title='Select Refused Folder')
    folder_path.set(filename_refused)
    print("Dossier refuse", filename_refused)
    os.chdir(filename_refused)
    dossier_fichier_refuses_confirm = Label(fenetre, text=filename_refused)
    dossier_fichier_refuses_confirm.place(x=150, y=570)
    return filename_refused

def choose_folder_xdcam():
    global folder_path
    filename = filedialog.askdirectory(title='Select XDCAM Folder')
    folder_path.set(filename)
    print(filename)
    os.chdir(filename)
    dossier_fichier_refuses_confirm = Label(fenetre, text=filename)
    dossier_fichier_refuses_confirm.place(x=300, y=570)
    return filename

def choose_folder_prores():
    global folder_path
    filename = filedialog.askdirectory(title='Select Prores Folder')
    folder_path.set(filename)
    print(filename)
    os.chdir(filename)
    dossier_fichier_refuses_confirm = Label(fenetre, text=filename)
    dossier_fichier_refuses_confirm.place(x=500, y=570)
    return filename


def moveto_refused(filename, file, filename_refused):
    source = (filename + '/' + file)
    destination = (filename_refused + '/' + file)
    shutil.move(source, destination)
    print(file, "déplacé dans le dossier REFUSE")

def moveto_prores (filename, file, filename_prores):
    source = (filename + '/' + file)
    destination = (filename_prores + '/' + file)
    shutil.move(source, destination)
    print(file, "déplacé dans le dossier PRORES CONFORME")

def moveto_xdcam (filename, file, filename_xdcam):
    source = (filename + '/' + file)
    destination = (filename_xdcam + '/' + file)
    shutil.move(source, destination)
    print(file, "déplacé dans le dossier XDCAM CONFORME")


def erase_list():
    x = cadre.get_children()
    for item in x:
        cadre.delete(item)
        """fenetre.update()"""

def rapport():
    fenetre_rapport = Tk()
    fenetre_rapport.title("Entrer le nom de votre rapport")
    fenetre_rapport.minsize(300, 200)
    fenetre_rapport.maxsize(300,200)
    fenetre_rapport['bg'] = 'white'

    cadf2 = Label(fenetre_rapport, text="Entrer le nom de votre rapport", font=("arial", 15))
    cadf2.place(x=100,y=25,anchor='c')

    DossierRapport = Label(fenetre_rapport, text="Dossier du rapport")
    DossierRapport.place(x=20, y=50)
    bouton_dossier = Button(fenetre_rapport, text="Choisir ...", command=askdirectory, bg="grey")
    bouton_dossier.place(x=200, y=55)


    def getEntry():
        nomdufichier = myEntry.get()
        print(nomdufichier)

    myEntry = tk.Entry(fenetre_rapport,width=15)
    myEntry.place(x=20,y=100)

    bouton_entree = Button(fenetre_rapport, text="Entrée", command=getEntry, bg="grey")
    bouton_entree.place(x=200,y=105)

    fenetre_rapport.mainloop()

"""def Filerapport(nomdufichier):
    myFile = open("(nomdufichier).txt", "w+")
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

                ################GENERAL##################
            elif track.track_type == "General":
                pprint(track.track_type)
                print(" Format : {t.format}\n Format profile : {t.format_profile}\n".format(t=track))


                ################AUDIO##################
            elif track.track_type == "Audio":
                pprint(track.track_type)
                print(" Format: {t.format}\n Sampling rate: {t.other_sampling_rate}\n"
                          .format(t=track))


                ################OTHER##################
            elif track.track_type == "Other":
                pprint(track.track_type)
                print(" TIM: {t.time_code_of_first_frame}\n".format(t=track))


myFile = open("cuppa2py.txt", "w+")

myFile.write("Le nom du fichier est :")

myFile.write(" Format: {t.format}\n Format profile: {t.format_profile}\n Bit rate: {t.other_bit_rate}\n "
                      "Width: {t.sampled_width} pixels\n Height: {t.sampled_height} pixels\n Frame rate: {t.other_frame_rate}\n "
                      "Scan type: {t.other_scan_type}\n Scan order: {t.other_scan_order}\n"
                      " Bit-(Pixel*Frame): {t.bits__pixel_frame}\n".format(t= track))

myFile.write(" Format : {t.format}\n Format profile : {t.format_profile}\n".format(t=track))

myFile.write(" Format: {t.format}\n Sampling rate: {t.other_sampling_rate}\n"
                      .format(t=track))

myFile.write(" TIM: {t.time_code_of_first_frame}\n".format(t=track))

myFile.close()"""

# Bouton Watchfolder
folder_path = StringVar()
watchfolder = Label(fenetre, text="Watchfolder")
watchfolder.place(x=48, y=510)
bouton_1 = Button(fenetre, text="Vérification", command=video_verif, bg="grey")
bouton_1.place(x=48, y=540)

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
bouton_5 = Button(fenetre, text="Générer un rapport ...", command=rapport, bg="cyan", fg="gray")
bouton_5.place(x=370, y=420)

# Bouton Effacer la liste
bouton_6 = Button(fenetre, text="Effacer la liste", command=erase_list, bg="blue", fg="gray")
bouton_6.place(x=525, y=420)

##################HORODATAGE##################


#onlyfiles = [f for f in listdir("G:/Documents/testFichier") if isfile(join("G:/Documents/testFichier", f))]
# utiliser os.listdir(path)

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




# Fin du programme

fenetre.mainloop()