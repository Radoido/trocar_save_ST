# Trocar save - Stardew Valley

**Facilitando a troca de personagens principais em saves do Stardew Valley no modo co-op**

## 🌟 Sobre o Projeto

Este programa altera o arquivo de save do Stardew Valley para trocar os papéis dos jogadores em uma campanha co-op:
- Transforma o jogador principal em "Farmer"
- Promove um "Farmer" para jogador principal (dono da fazenda)

Eu jogava com minha namorada e o save ficava sempre no meu computador. Com o tempo fui parando de jogar e ela queria continuar então pensei em apenas enviar o save para ela, porém(obviamente), o jogo iniciava com o meu personagem e etc. Procurei em alguns lugares se havia alguma forma ou site com script para fazer a troca e só encontrei uma instrução no reddit do que poderia alterar. Comecei a ler o arquivo de save para identificar onde estavam o parametros que eu gostaria de trocar (Persongens e local da casa), algo bem chato embora simples. Assim tive a ideia de fazer um script para facilitar este processo quando precisasse realizar novamente. 

🚧 *Atualmente em fase funcional básica - sem interface gráfica ou tratamento de erros*

## ⚙️ Funcionalidades Atuais
- Modificar o arquivo de save
- Troca básica de IDs dos personagens
- Gera outro save para não sobreescrever o antigo

## 🔮 Funcionalidades futuras
- [ ] Interface gráfica
- [ ] Executável (.exe)
- [ ] Caminhos automáticos (busca o save)
- [ ] Suporte para múltiplos farmers (2+)
- [ ] Seleção manual de jogadores

## 📦 Como Usar (Necesário ter python instalado)
1. git clone https://github.com/radoido/trocar_save_ST.git
2. Copie o save que deseja para dentro do diretório clonado (save esta localizado em `%AppData%\StardewValley\Saves`)
3. Execute o script no terminal e siga as instruções:
   ```bash
   python arquivo.py
