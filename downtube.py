from cgitb import text
from queue import Empty
from re import T
import rlcompleter
from pytube import *
from tkinter import *
import time
import os
from tkinter import filedialog

test = "test"

def vid():
    VideoType.config(text="Type de fichier: Vidéo")
    StatusLabel.config(text="Hors Ligne.")
    StatusLabel.config(text="Obtention du lien...")
    time.sleep(4)
    global yt
    yt = YouTube(lien.get())
    global path
    path = emplacement.get()
    global yd
    yd = yt.streams.get_highest_resolution()
    print('Type: Vidéo.')
    StatusLabel.config(text="Trouvé!")
    time.sleep(4)
    StatusLabel.config(text="Pret.")

def aud():
    VideoType.config(text="Type de fichier: Audio")
    StatusLabel.config(text="Hors Ligne.")
    StatusLabel.config(text="Obtention du lien...")
    time.sleep(4)
    yt = YouTube(lien.get())
    global path
    path = emplacement.get()
    global yd
    yd = yt.streams.get_audio_only()
    print('Type: Audio')
    StatusLabel.config(text="Trouvé!")
    time.sleep(4)
    StatusLabel.config(text="Pret.")

videos = os.path.join(os.environ['USERPROFILE'], "Videos")

def choose():
    emplacement.delete(0, END)
    emplacement.insert(0, filedialog.askdirectory(initialdir = videos))

def downtube():
    StatusLabel.config(text="Téléchargement...")
    time.sleep(6)
    yd.download(emplacement.get())
    time.sleep(3)
    StatusLabel.config(text="Téléchargé!")

path = ""
link = ""

root = Tk()
root.title("DownTube")
root.geometry('410x370')
root.configure(background='#FFFFFF')
root.title('DownTube')
Label(root, text='Emplacement de la vidéo:', bg='#FFFFFF', font=('arial', 24, 'normal')).place(x=5, y=7)
emplacement=Entry(root)
emplacement.insert(0, "Entrez l'emplacement ou cliquez sur choisir...")
emplacement.place(x=5, y=48, width=275)
Label(root, text='Lien de la vidéo:', bg='#FFFFFF', font=('arial', 24, 'normal')).place(x=5, y=77)
lien=Entry(root)
lien.insert(0, link)
lien.place(x=5, y=117, width=400)
choisir = Button(root, text="Choisir Dossier", bg='#FFFFFF', font=('arial', 12, 'normal'), padx=1, pady=1, command=choose).place(x=285, y=45)
Button(root, text='Audio', bg='#FFFFFF', font=('arial', 24, 'normal'), command=aud, width=10).place(x=5, y=177)
Button(root, text='Video', bg='#FFFFFF', font=('arial', 24, 'normal'), command=vid, width=10).place(x=210, y=177)
Button(root, text='DownTube!', bg='#FFFFFF', font=('arial', 24, 'normal'), command=downtube).place(x=110, y=247)
Label(root, text='Status:', bg='#FFFFFF', font=('arial', 24, 'normal')).place(x=15, y=327)
StatusLabel = Label(root, text="Hors Ligne.", bg='#FFFFFF', font=('arial', 24, 'normal'))
StatusLabel.place(x=125, y=327)
VideoType = Label(root, text='Type de fichier:', bg='#FFFFFF', font=('arial', 24, 'normal'))
VideoType.place(x=5, y=137)

root.mainloop()
