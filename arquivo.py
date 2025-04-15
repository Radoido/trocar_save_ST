# import tkinter as tk
import os 
import xml.etree.ElementTree as ET

current_directory = os.getcwd()
files = [f for f in os.listdir(current_directory) if os.path.isfile(f) and '.' not in f ]#

if (not files):
    print ('--- Nenhum arquivo de save encontrado --- \nOs aquivos de save nao possuem extensao (".exe",".xml")')
    input("pressione qualquer tecla para sair")
    exit()

print('\nArquivos encontrados')
for id, file in enumerate(files):
    print (f"{id}- {file}")

while True:
    choice = int(input('\nDigite a posicao do arquivo que deseja alterar: '))
    if (choice and 0 <= choice <= len(files)):
        file = files[choice]
        c = int(input(f"Arquivo {file} selecionado. Deseja continuar?\n 1-SIM\n 2-SELECIONAR OUTRO ARQUIVO\n 3-CANCELAR\n"))
        if (c == 1):
            break
        if (c == 2):
            continue
        else:
            print('Ate mais :)')
            exit()
    else:
        print('Valor selecionado invalido, escolha outro dentro da lista!')
        continue
print("==--------------------==")


#busca o arquivo de save 
tree = ET.parse(file)      
root = tree.getroot()

#busca o nome e a casa do Player principal
player = root.find('./player')
playerName = player.find('./name')
playerHouse = player.find('.//homeLocation')

#salva o nome e a casa do Player secundario(Farmer)
x = root.find('.//Farmer')
x1 = x.find('./name')
x2 = x.find('.//homeLocation')

# #seta o Player como Farmer e troca as casa
farmerName = playerName
farmerHouse = playerHouse

#seta o Farmer como player principal
playerName = x1
playerHouse = x2

print(f'Save original\n Player principal: {playerName.text}, {playerHouse.text}\n Player secundario: {farmerName.text}, {farmerHouse.text}  \n==--------------------==')

#salva os atributos
print('Gerando novo save')
tree.write("save_editado", encoding="utf-8", xml_declaration="true")
input('Pressione qualquer tecla para sair')
