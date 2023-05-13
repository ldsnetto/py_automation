# Realiza pesquisa automatizada.

import webbrowser
import pyautogui as pyag
from time import sleep

# tela no notebook usar 1200. tela uwscreen 2400
cho = int(input("Digite 1 para executar no note e 2 na ultrawide: "))

if cho == 1:
    tela = 1200
elif cho == 2:
    tela = 2400
else:
    tela = print("Numero Inválido\n")
    exit()

# Qual o tema da pesquisa do dia?
st = input("\nDigite sobre qual série histórica deseja pesquisar: ")
print("\n")
stg = st + " "
nbs = len(stg) + 5

webbrowser.open('https://www.bing.com/search?q=Fla&form=ANNTH1&refig=f99eb03666514d03a76812e49b91d64c')

for i in range(1990,2023):
    # click na barra de pesquisa
    pyag.click(tela,159,duration=1.5)
    sleep(1)

    # Apagar texto da pesquisa
    for j in range(1,nbs):
        pyag.press('backspace')
        sleep(0.1)

    # Escrever o que texto a ser pesquisado
    pyag.write(stg + str(i))
    sleep(0.3)

    # Enter para realizar a pesquisa
    pyag.press('enter')
    sleep(3)