# Author: crelgd

import os
import sys
from time import sleep

# Installing

os.system('apt update && apt upgrade')
os.system('pip install colorama')
os.system('pip install requests')
os.system('clear')

import requests
from colorama import init, Fore

init(autoreset=True)

print(Fore.CYAN + """
   / __      ___     // //  ___    
  //   ) ) //___) ) // // //   ) ) 
 //   / / //       // // //   / /  
//   / / ((____   // // ((___/ /
""")

name = input('Enter text: ')

responce = requests.get(f'https://asciified.thelicato.io/api?text={name}')

print(Fore.CYAN + responce.text)

while True:
    g = input('Confrim? Yes(y), No(n) ')

    if(g == 'y'):
        break
    else:
        sys.exit()

file = open('/data/data/com.termux/files/home/.bashrc', 'w')
txt = f'''
clear
echo "{responce.text}"
'''
file.write(txt)
file.close()

print(Fore.RED + "Restart Termux!")
sleep(9999)
