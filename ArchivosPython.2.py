print("Fco. Santiago Carrasco C. 3 ° W 0421")
print(" ")
# abrir un archivo en una ubicacion diferente
f = open("C:\\ArchivosPython\\welcome.txt", "r")  # abrir archivo en otra ubicacion
print(f.read())  # imprimir contenido del archivo
f.close()  # cerrar el archivo