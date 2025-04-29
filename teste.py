import os
import pytest
import xml.etree.ElementTree as ET
from io import StringIO
import sys

def test_arquivo_selecao(tmp_path, monkeypatch):
    """Testa a seleção de arquivo"""
    # Cria arquivo de teste
    test_file = tmp_path / "test_save"
    test_file.write_text("<root><player><name>Test</name></player></root>")
    
    # Muda para o diretório temporário
    monkeypatch.chdir(tmp_path)
    
    # Simula entrada do usuário (0 para primeiro arquivo, 1 para confirmar)
    monkeypatch.setattr('sys.stdin', StringIO('0\n1\n'))
    
    # Captura a saída
    from save_editor import main  # assumindo que seu código está em arquivo.py
    
    # Verifica se o arquivo foi processado
    assert os.path.exists(tmp_path / "save_editado")

def test_swap_values(tmp_path, monkeypatch):
    """Testa se os valores são trocados corretamente"""
    # Cria XML de teste
    xml_content = """
    <root>
      <jogador>
        <name>Player</name>
        <homeLocation>CasaPlayer</homeLocation>
      </jogador>
      <Lander>
        <name>Farmer</name>
        <homeLocation>CasaFarmer</homeLocation>
      </Lander>
    </root>
    """
    test_file = tmp_path / "test_save"
    test_file.write_text(xml_content)
    
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr('sys.stdin', StringIO('0\n1\n'))
    
    from save_editor import main
    main()
    
    # Verifica o arquivo gerado
    tree = ET.parse(tmp_path / "save_editado")
    root = tree.getroot()
    
    assert root.find('./player/name').text == "Farmer"
    assert root.find('./Farmer/name').text == "Player"