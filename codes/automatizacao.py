#Bibiliotecas importadas
import pyautogui
import time
import pandas as pd
#Importar a base dos produtos
tabela = pd.read_csv ('produtos.csv')
print (tabela)
#tempo
pyautogui.PAUSE = 1
#Abrindo o navegador / Site de cadastro
pyautogui.press('win')
pyautogui.write('Google Chrome')
pyautogui.press('enter')
pyautogui.press('F11')
pyautogui.click(x=455, y=316)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep (2)
#Fazendo login no site
pyautogui.click(x=397, y=286)
pyautogui.write('emailficticio@outlook.com.br')
pyautogui.press('tab')
pyautogui.write('senha123')
pyautogui.click(x=662, y=450)
#Fazendo o cadrasto dos itens da tabela
for linha in tabela.index:
    pyautogui.click(x=394, y=171)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,  'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    if not pd.isna(tabela.loc[linha, 'obs']):   
        pyautogui.write(str(tabela.loc[linha, 'obs']))
#envio do produto e reiniciamento do ciclo
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000) #subir para o inicio da pagina novamente
    pyautogui.click(x=389, y=172)