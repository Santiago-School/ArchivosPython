print("Fco. Santiago Carrasco C. 3 ° W 0421")
print(" ")
# leer solo partes del archivo
f = open("demofile.txt", "r")  # abrir el archivo
print(f.read(5))  # devolver los 5 primeros caracteres
f.close()  # cerrar el archivo