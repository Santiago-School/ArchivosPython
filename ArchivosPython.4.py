print("Fco. Santiago Carrasco C. 3 ° W 0421")
print(" ")
# escritura en archivos en python
# escribir en un archivo existente
f = open("demofile.txt", "a")  # abrir el archivo en modo anexar
f.write("now the file has more content!")  # agregar contenido al archivo
f.close()  # cerrar el archivo

# abrir y leer el archivo despues de añadir
f = open("demofile.txt", "r")  # abrir el archivo en modo lectura
print(f.read())  # imprimir contenido del archivo
f.close()  # cerrar el archivo
