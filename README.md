# Trocar save - Stardew Valley

**Facilitando a troca de personagens principais em saves do Stardew Valley no modo co-op**

## 🌟 Sobre o Projeto
Este programa altera o arquivo de save do Stardew Valley para trocar os papéis dos jogadores em uma campanha co-op:
- Transforma o jogador principal em "Farmer"
- Promove um "Farmer" para jogador principal (dono da fazenda)

🚧 *Atualmente em fase funcional básica - sem interface gráfica ou tratamento de erros*

## ⚙️ Funcionalidades Atuais
- Modificar o arquivo de save
- Troca básica de IDs dos personagens
- Gera outro save para não sobreescrever o antigo

## 🔮 Implementações a fazer
- [ ] Interface gráfica
- [ ] Executável (.exe)
- [ ] Caminhos automáticos (busca o save)
- [ ] Suporte para múltiplos farmers (2+)
- [ ] Seleção manual de jogadores

## 🛠️ Tecnologias Utilizadas
- Python 3.x (com `xml.etree.ElementTree` para manipulação de saves)
- [Biblioteca X] (se aplicável)

## 📦 Como Usar (Versão Atual)
1. git clone https://github.com/radoido/trocar_save_ST.git
2. Copiar o save que deseja para dentro do diretório clonado (save esta localizado em `%AppData%\StardewValley\Saves`)
3. Execute o script e siga as instruções:
   ```bash
   python arquivo.py
