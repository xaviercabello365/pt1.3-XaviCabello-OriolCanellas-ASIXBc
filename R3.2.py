"""
Xavier Cabello, Oriol Canellas
ASIXc 1B
MO3 Programació Paraules Boges
"""

import os
import datetime

def process_files(input_dir, output_dir, log_dir):
    # Iniciamos el programa
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file = os.path.join(log_dir, "boges.log")
    with open(log_file, 'a') as log:
        log.write(f"El programa se ha iniciado a las {current_time}.\n")

    try:
        # Recorremos los archivos en el directorio de entrada
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".txt"):
                input_file = os.path.join(input_dir, file_name)
                output_file = os.path.join(output_dir, file_name.replace(".txt", "_boges.txt"))

                # Procesamos el archivo
                process_data(input_file, output_file, log_file)

    except Exception as e:
        # Manejamos errores y los registramos en el archivo de log
        with open(log_file, 'a') as log:
            log.write(f"Error durante la ejecución del programa: {str(e)}\n")

    # Finalizamos el programa
    with open(log_file, 'a') as log:
        log.write(f"El programa ha finalizado a las {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.\n")

def process_data(input_file, output_file, log_file):
    try:
        # Abrimos el archivo de entrada para leer
        with open(input_file, 'r') as input_file:
            data = input_file.read()

        # Procesamos los datos convirtiendo el texto a minúsculas y escribimos en el archivo de salida
        with open(output_file, 'w') as output_file:
            output_file.write(data.lower())

        # Registramos en el archivo de log
        with open(log_file, 'a') as log:
            log.write(f"El archivo {input_file} ha sido procesado correctamente.\n")

    except Exception as e:
        # Manejamos errores y los registramos en el archivo de log
        with open(log_file, 'a') as log:
            log.write(f"Error procesando el archivo {input_file}: {str(e)}\n")

# Directorios de trabajo
input_dir = "./entrada"
output_dir = "./sortida"
log_dir = "./log"

# Procesamos los archivos
process_files(input_dir, output_dir, log_dir)
