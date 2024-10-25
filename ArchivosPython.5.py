print("Fco. Santiago Carrasco C. 3 ° W 0421")
print(" ")
# sobrescribir contenido en un archivo
f = open("demofile.txt", "w")  # abrir el archivo en modo escritura
f.write("woops! i have deleted the content!")  # sobrescribir contenido


# abrir y leer el archivo despues de sobrescribir
f = open("demofile.txt", "r")  # abrir el archivo en modo lectura
print(f.read())  # imprimir contenido del archivo
f.close()  # cerrar el archivo