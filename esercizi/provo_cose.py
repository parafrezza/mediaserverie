# provo_cose.py
from ast import Try
import os

# -------------------------------------------  variabili
variabile_per_tutti = 5  #variabile "globale"

# -------------------------------------------


# -------------------------------------------  funzioni

def moltiplicaPerLaVariabileGlobale( valore_da_moltiplicare):
    una_roba_stupida_da_dire = "Ciao"    #  variabile "locale"
    return valore_da_moltiplicare * variabile_per_tutti
# -------------------------------------------  


# -------------------------------------------  codice
os.system('clear')

framerate = ['24', '25', '30']

try:
    x = framerate.index('60')
    print (x)
except:
    print('seeeee...')

print ('ciao ciao')