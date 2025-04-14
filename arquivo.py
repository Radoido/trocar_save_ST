import tkinter as tk
import xml.etree.ElementTree as ET

#busca o arquivo de save 
tree = ET.parse('Pitaya_401835050')
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

print(f'Save original \nPlayer principal: {playerName.text}, {playerHouse.text} \nPlayer secundario: {farmerName.text}, {farmerHouse.text}  \n==---------------------==')

#salva os atributos
tree.write("save_editado", encoding="utf-8", xml_declaration="true")
