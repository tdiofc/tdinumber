from colorama import init, Fore, Back, Style
import os
import sys
import requests

#colores 

rojo = Fore.RED
violeta = Fore.MAGENTA
amarillo = Fore.YELLOW
blanco = Fore.WHITE
azul = Fore.BLUE
celeste = Fore.CYAN

print(f"""{celeste}

████████╗░░░██████╗░░░░██╗
╚══██╔══╝░░░██╔══██╗░░░██║
░░░██║░░░░░░██║░░██║░░░██║
░░░██║░░░░░░██║░░██║░░░██║
░░░██║░░░██╗██████╔╝██╗██║
░░░╚═╝░░░╚═╝╚═════╝░╚═╝╚═╝{blanco}
""")

api_key = 'a34d97f03e51e991d6699b9de0b8694c'
number = input('Número: ')
print("")

   # Petición

data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, number))

for key, value in data.json().items():
    
  print("%s: %s" % (key, value))

print("")

