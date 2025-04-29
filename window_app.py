import tkinter as tk
from tkinter import ttk
from save_editor import *

def init():
    root = tk.Tk()
    window = ttk.Frame(root, padding=10)
    window.grid()
    ttk.Label(window, text='Trocar save stardew valley').grid(column=0,row=0)
    ttk.Button(window, text='Buscar arquivo', command=lambda: get_file()).grid(column=0, row=1)
    
    root.mainloop()