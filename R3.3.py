"""
Xavier Cabello, Oriol Canellas
ASIXc 1B
MO3 Programació Paraules Boges
"""

import os

directorio = "./"
archivos_txt = [archivo for archivo in os.listdir(directorio) if archivo.lower().endswith(".txt")]

print("Archivos .txt en el directorio:")
for archivo in archivos_txt:
    print(archivo)