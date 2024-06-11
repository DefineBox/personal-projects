#Importing important libraries for this project
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

def addSongs():
    new_var = "*MP3"
    tempSong = filedialog.askopenfilenames(initialdir = "Music/", title = "Choose a song", filetypes = (("MP3 Files", "*.mp3"),))
    
    for song in tempSong:
        song = song.replace("C:\Users\reblp\Documents\Music.txt", "")
        songList.insert(END, song)

