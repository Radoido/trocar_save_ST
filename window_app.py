import tkinter as tk
from tkinter import ttk
from save_editor import *

class window_app():
        
    def __init__(self, root ):
        self.root = root
        self.root.title('alterar a save - Stardew Valley')
        self.file_text = tk.StringVar()
        self.file = ''
        
        self.create_window()      
        
    #create grid window
    def create_window(self):
        window = ttk.Frame(self.root, padding=10)
        window.grid()
        ttk.Label(window, text='Alterar dono do save \n stardew valley').grid(column=0,row=0)
        
        #select the file and show in window        
        ttk.Button(window, text='Buscar arquivo', command=lambda: self.button_action()).grid(column=0, row=1)
        ttk.Label(window, textvariable=self.file_text).grid(column=1, row=1)
        

    def button_action(self):
        self.file = get_file(self.file_text)
        
    def start(self):
        self.root.mainloop()
            
        
        
    