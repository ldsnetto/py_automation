# Realiza pesquisa automatizada.

import webbrowser
import pyautogui as pyag
from time import sleep
from random import *

# tela no notebook usar 1200. tela widescreen 2300
cho = int(input("Digite 1 para executar no note e 2 na ultrawide: "))

if cho == 1:
    tela = 1200
elif cho == 2:
    tela = 2300
else:
    tela = print("Numero Inválido\n")
    exit()

# Qual o tema da pesquisa do dia?
st = input("\nDigite sobre qual série histórica deseja pesquisar: ")
print("\n")
stg = st + " 1900"
# nbs = len(stg) + 5

webbrowser.open('https://www.bing.com/search?q=bing')

# click na barra de pesquisa
pyag.click(tela,135,duration=0.5)
sleep(randrange(2,5))

# Apagar texto da pesquisa
for i in range(1,6):
    pyag.press('backspace')
    sleep(0.25)

# Escrever o que texto a ser pesquisado
pyag.write(stg)
sleep(0.5)

# Enter para realizar a pesquisa
pyag.press('enter')
sleep(randrange(2,5))
pyag.press('pgup')
sleep(0.5)
pyag.press('pgup')
sleep(1)

## Pesquisa entre 1991 a 1999

for i in range(1,10):
    # click na barra de pesquisa
    pyag.click(tela,135,duration=0.5)
    sleep(randrange(2,5))

    # Apagar somente 1o digito da pesquisa
    pyag.press('backspace')
    sleep(0.25)

    # Escrever o ultimo digito a ser pesquisado
    pyag.write(str(i))
    sleep(0.5)

    # Enter para realizar a pesquisa
    pyag.press('enter')
    sleep(randrange(2,5))
    pyag.press('pgup')
    sleep(0.5)
    pyag.press('pgup')
    sleep(1)

## Pesquisa entre 2000 a 2023

# click na barra de pesquisa
pyag.click(tela,135,duration=0.5)
sleep(randrange(2,5))

for i in range(1,5):
    pyag.press('backspace')
    sleep(0.25)

# Escrever o ultimo digito a ser pesquisado
pyag.write('2000')
sleep(0.5)

# Enter para realizar a pesquisa
pyag.press('enter')
sleep(randrange(2,5))
pyag.press('pgup')
sleep(0.5)
pyag.press('pgup')
sleep(1)

for i in range(1,24):
    # click na barra de pesquisa
    pyag.click(tela,135,duration=0.5)
    sleep(randrange(2,5))

    # Apagar somente 1 ou 2 digitos da pesquisa
    if i < 10:
        pyag.press('backspace')
        sleep(0.25)
    else:
        pyag.press('backspace')
        sleep(0.25)
        pyag.press('backspace')
        sleep(0.25)

    # Escrever o ultimo digito a ser pesquisado
    pyag.write(str(i))
    sleep(0.5)

    # Enter para realizar a pesquisa
    pyag.press('enter')
    sleep(randrange(2,5))
    pyag.press('pgup')
    sleep(0.5)
    pyag.press('pgup')
    sleep(1)