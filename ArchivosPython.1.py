print("Fco. Santiago Carrasco C. 3 ° W 0421")
print(" ")
# abrir un archivo en el servidor
f = open("demofile.txt", "r")  # abrir el archivo en modo lectura
print(f.read())  # imprimir el contenido del archivo
f.close()  # cerrar el archivo