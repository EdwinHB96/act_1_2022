# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import os

AS_Files = []

main_path = "C:\tareas_aps\act_1"

lista_archivos = os.listdir(main_path)

for archivo in lista_archivos:
    if archivo.endswith(".AS"):
        AS_Files.append(archivo)

        
print("Se encontraron: ",len(AS_Files)," archivos .AS")
print ("Ésta es la lista de archivos: ")
print (AS_Files)


for mediciones in AS_Files:
    os.system("teqc -O.dec 30 +obs " + mediciones.split("_")[0] + ".o "+ mediciones)
    











    
