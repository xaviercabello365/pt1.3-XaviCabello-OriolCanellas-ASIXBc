"""
Xavier Cabello, Oriol Canellas
ASIXc 1B
MO3 Programació Paraules Boges
"""

import datetime

def process_data(input_file, output_file, log_file):
    # Iniciamos el programa
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a') as log:
        log.write(f"El programa se ha iniciado a las {current_time}.\n")

    try:
        # Abrimos el archivo de entrada para leer
        with open(input_file, 'r') as input_file:
            data = input_file.read()

        # Procesamos los datos convirtiendo el texto a minúsculas y escribimos en el archivo de salida
        with open(output_file, 'w') as output_file:
            output_file.write(data)

    except Exception as e:
        # Manejamos errores y los registramos en el archivo de log
        with open(log_file, 'a') as log:
            log.write(f"Error durante la ejecución del programa: {str(e)}\n")

    # Finalizamos el programa
    with open(log_file, 'a') as log:
        log.write(f"El programa ha finalizado a las {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.\n")

# Archivos de entrada, salida y log
input_file = "paraules.txt"
output_file = "paraules_boges.txt"
log_file = "boges.log"

# Ejecutamos el programa
process_data(input_file, output_file, log_file)