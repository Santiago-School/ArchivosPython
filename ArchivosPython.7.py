import os

print("Fco. Santiago Carrasco C. 3 ° W 0421")
print(" ")
# 7 comprobar si el archivo existe
if os.path.exists("demofile.txt"):  # verificar si el archivo existe
    os.remove("demofile.txt")  # eliminar el archivo
else:  # si no existe
    print("the file does not exist")  # imprimir mensaje
