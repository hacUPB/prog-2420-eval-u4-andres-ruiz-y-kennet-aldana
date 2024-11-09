import os
import csv
import matplotlib.pyplot as plt
def count_words(file):
    with open(file,"r") as myFile:
        count = 0
        for line in myFile.readlines():
            words_per_line = line.split(' ')
            # borramos el salto de línea
            if '\n' in words_per_line:
                words_per_line.remove('\n')
            count += (len(words_per_line))
        print(f"El texto tiene {count} palabras.")

def replace_word(find,replace,file):
    # variable bandera
    found = False
    # leemos todas las líneas
    with open(file,"r") as myFile:
        lines = myFile.readlines()

    new_lines = []
    for line in lines:
        if find in line:
            line = line.replace(find,replace)
            found = True
        new_lines.append(line)
    # si encontramos la palabra, escribimos para reemplazar
    if found:
        with open(file,"w") as myFile:
            myFile.writelines(new_lines)
def total_chars(file):
    chars = 0
    filtered_chars = 0
    with open(file,"r") as myFile:
        lines = myFile.readlines()
    for line in lines:
        for char in line:
            chars += 1
    
    
    for line in lines:
        for word in line.split(" "):
            for char in word:
                filtered_chars += 1
                print(char if char != " " else 0)
    print(filtered_chars)
    
    print(f"Total caracteres incluyendo espacios en blanco: {chars}")

def list_files(path):
    if path != '':
        archivos = os.listdir(path)
    else:
        archivos = os.listdir(os.getcwd())

    for archivo in archivos:
        print(archivo)
            
def first_rows(file):
    with open(file,"r") as csvfile:
        lector = csv.reader(csvfile)
        index = 0
        for fila in lector:
            print(fila)
            if index >14:
                break
            index += 1

def compute_stats(column,file):
    header = None
    values = []
    with open(file,"r") as csvfile:
        lector = csv.reader(csvfile)
        header = next(lector)
        index = header.index(column)
        for fila in lector:
            values.append(int(fila[index]))
    total = sum(values)
    avg = total / len(values)
    min_number = min(values)
    max_number = max(values)
    sort = sorted(values)
    median = sort[len(sort)//2]

    return avg,min_number,max_number,median,sort    


def menu():
    print("""
1. Listar archivos presentes en la ruta actual o ingresar una ruta donde buscar los archivos.
2. Procesar archivo de texto (.txt)
3. Procesar archivo separado por comas (.csv)
4. Salir
""")

opc = 0
while opc != 4:
    menu()
    opc = int(input("Por favor escoge una opción: "))
    if opc == 1:
        path = input("Ingresa una ruta para analizar los archivos o simplemente presiona enter: ")
        list_files(path)
    elif opc == 2:
        print("""
            1.Contar número de palabras.
            2.Reemplazar una palabra por otra.
            3.Contar el número de caracteres.
        """)
        subopc = int(input("Ingresa una opción:"))
        path = input("Ingresa la ruta del archivo: ")
        if subopc == 1:
            count_words(path)
        elif subopc ==2:
            find = input("Ingresa la palabra que quieres reemplazar: ")
            replace = input("Ingresa la palabra con la cuál harás el reemplazo: ")
            replace_word(find,replace,path)
        elif subopc==3:
            total_chars(path)
    elif opc == 3:
        print("""
            1.Mostrar las 15 primeras filas.
            2.Calcular Estadísticas.
            3.Graficar una columna completa con los datos.
        """)
        subopc = int(input("Escoge una opción: "))
        path = input("Ingrese el nombre del archivo: ")
        if subopc == 1:
            print(path)
            first_rows(path)
        elif subopc == 2:
            column = input("Ingresa el nombre de la columna:")
            print(compute_stats(column,path))
        elif subopc == 3:
            column = input("Ingresa el nombre de la columna:")
 
            plt.plot(compute_stats(column,path)[-1])
            plt.show()
            