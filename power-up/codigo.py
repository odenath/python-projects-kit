# Para começar anote o passo a passo
# 1. Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# 2. Fazer login
# 3. Importar a base de produtos pra cadastrar
# 4. Cadastrar os produtos
# 5. Repetir o processo até acabar a base
# 6. Verificar se os produtos foram cadastrados


# 1. Entrar no sistema da empresa
import pyautogui 
import time
import pandas as pd
# pyautogui.write() escreve onde o mouse está
# pyautogui.press() pressiona uma tecla
# pyautogui.click() clica onde o mouse está
# (button="right") clica com o botão direito (button="left") clica com o botão esquerdo (clicks=2) clica duas vezes
# pyautogui.position() mostra a posição do mouse
# pyautogui.alert() mostra um alerta na tela
# pyautogui.hotkey() combina teclas

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(4.5)   # espera 3 segundos
pyautogui.press("tab")
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.write("admi64")
pyautogui.press("tab")
pyautogui.press("enter")



# Olá, tudo bem?
#Fiz este comentário para falar sobre um erro que aconteceu comigo e me levou quase 1.30h para resolver.
#O erro aconteceu na hora de importar a base de dados, pois o caminho do arquivo estava errado.
#O caminho foi relativo, mas não funcionou. Então, coloquei o caminho absoluto e funcionou.
# Ainda vou descobrir pq não funcionou o caminho relativo, pois no \data-analysis\initial.ipynb funcionou.
tabela = pd.read_csv("C:\\Users\Gustavo\Documents\Python-Hashtag\projects\power-up\produtos.csv")
print(tabela)

time.sleep(4.5)   # espera 4.5 segundos

for linha in tabela.index:
    pyautogui.click(x=880, y=341)
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.press("pgup")






