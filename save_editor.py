# import tkinter as tk
import os 
import xml.etree.ElementTree as ET
from tkinter import filedialog
import tkinter as tk

def get_file(file_text):
    file = filedialog.askopenfilenames(title='Selecionar arquivos')
    title = os.path.basename(file)
    file_text.set((title))
    return file

def show_files(files):
    print('\nArquivos encontrados')
    for id, file in enumerate(files):
        print (f"{id}- {file}")
        
def select_file(files):
        while True:
                choice = int(input('\nDigite a posicao do arquivo que deseja alterar: '))
                if (choice and 0 <= choice <= len(files)):
                    file = files[choice]
                    c = int(input(f"Arquivo {file} selecionado. Deseja continuar?\n 1-SIM\n 2-SELECIONAR OUTRO ARQUIVO\n 3-CANCELAR\n"))
                    if (c == 1):
                        return file
                    if (c == 2):
                        continue
                    else:
                        print('Ate mais :)')
                        exit()
                else:
                    print('Valor selecionado invalido, escolha outro dentro da lista!')
                    continue
    
def change_file(file):
    tree = ET.parse(file)      
    root = tree.getroot()

    #busca o nome e a casa do Player principal
    player = root.find('./player')
    playerName = player.find('./name')
    playerHouse = player.find('.//homeLocation')

    #salva o nome e a casa do Player secundario(Farmer)
    farmer = root.find('.//Farmer')
    x1 = farmer.find('./name')
    x2 = farmer.find('.//homeLocation')

    #seta o Player como Farmer e troca as casas
    farmerName = playerName
    farmerHouse = playerHouse

    #seta o Farmer como player principal
    playerName = x1
    playerHouse = x2
    
    
def save_file(file):
    print('Salvando alterações')
    tree.write("save_editado", encoding="utf-8", xml_declaration="true")
    print(f'Save original\n Player principal: {playerName.text}, {playerHouse.text}\n Player secundario: {farmerName.text}, {farmerHouse.text}  \n==--------------------==')
    exit()





