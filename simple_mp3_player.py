from tkinter import *
import pygame

root = Tk()
root.title('music player')
root.iconbitmap('music.ico')
root.geometry("500x400")

pygame.mixer.init()


def play():
    pygame.mixer.music.load('mp3.mp3')
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()


play_button = Button(root, text='PLAY', command=play)
play_button.pack(pady=20)

stop_button = Button(root, text='STOP', command=stop)
stop_button.pack(pady=20)

root.mainloop()
