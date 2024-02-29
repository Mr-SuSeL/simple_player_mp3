from tkinter import *
import pygame

root = Tk()
root.title('music player')
root.iconbitmap('music.ico')
root.geometry("500x400")

pygame.mixer.init()


def play():
    pass

def stop():
    pass


play_button = Button()
play_button.pack()

stop_button = Button()
stop_button.pack()

root.mainloop()
