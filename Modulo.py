from Registros import *
import random
import pickle
import os

def menu():
    print("\n", "*" * 4, "Menu de opciones", "*" * 4)
    print("1) Cargar articulos.")
    print("2) Mostrar articulos previamente cargados")
    print("3) Crear archivo del articulo de x autor")
    print("4) Mostrar archivo creado en la opcion 3")
    print("5) Buscar un articulo")
    print("6) ¿Cuál es la cantidad de palabras de esa cadena que comienza con la letra “a” (en mayúsculas o minúsculas)?")
    print("7) Salir.")

def cargar_arreglo(vec, n):
    titulos = ("Alicia en el pais de las maravillas.", "Mad max.", "The eternal sunrise.", "Jhon Wick 4")
    nombres = ("Juan", "Joaquin", "Marcelo", "Nacho", "Agustin")
    apellidos = ("Villada", "Sosa", "Debard", "Guzman", "Frittelli")
    print("Se cargaron los registros, si desea verlos seleccione la opcion 2.")
    for i in range(n):
        codigo = random.randint(1111, 9999)
        titulo = random.choice(titulos)
        autor = random.choice(nombres) + " " + random.choice(apellidos)
        registro = Articulos(codigo, titulo, autor)
        add_in_orden_codigo(vec, registro)


def mostrar_articulos(vec):
    for i in vec:
        print(i)

def buscar_a(vec, a, archivo):
    band = True
    m = open(archivo, "wb")
    for i in vec:
        if i.autor == a:
            pickle.dump(i, m)
            print("Se cargo el archivo: ", i)
            band = False
    m.close()
    if band:
        print("No se encontro el autor...")

def mostrar_archivo(archivo):
    if not os.path.exists(archivo):
        print("\nCree primero el archivo en el punto 3...")
        return
    cont = 0
    t = os.path.getsize(archivo)
    m = open(archivo, "rb")
    print("\nLos registros del archivo son: \n")
    while t > m.tell():
        r = pickle.load(m)
        print(r)
        cont += 1
    print("\nSe encontraron ", str(cont), " registros.")

def buscar_codigo(vec, codigo):
    band = True
    for i in vec:
        if i.codigo == codigo:
            print("\nSe encontro el articulo: \n\t", i)
            band = False
            return i.titulo
            break
    if band:
        print("\nArticulo inexistente!.")
        return "Artículo inexistente!."

def comienza_a(cad):
    print("\n El titulo a analizar es: ", cad)
    cont = 0
    primeraletra = True
    for i in cad:
        if i == " ":
            primeraletra = True
        elif i in "aA" and primeraletra:
            cont += 1
            primeraletra = False
    print("\nLa cantidad de palabras que comienzan con 'a' o 'A' es de: " + str(cont))

def principal():
    op5 = True
    v = []
    archivo = "archivo.dat"
    op = -1
    while op != 7:
        menu()
        op = int(input("\nIngrese la opcion deseada..."))
        if op == 1:
            n = validar_mayor(1, "\nIngrese la cantidad de articulos que desea cargar...")
            cargar_arreglo(v, n)
        elif v == []:
            print("\nCargue primero el vector en el punto 1")
            op = -1
        elif op == 2:
            mostrar_articulos(v)
        elif op == 3:
            a = input("\nIngrese el nombre del autor que desea buscar...")
            buscar_a(v, a, archivo)
        elif op == 4:
            mostrar_archivo(archivo)
        elif op == 5:
            codigo = validar_entre(1111, 9999, "\nIngrese el codigo que desea buscar...")
            titulo = buscar_codigo(v, codigo)
            op5 = False
        elif op == 6:
            if op5:
                print("\nBusque un articulo en el punto 5...")
                op =  -1
            elif titulo == "Artículo inexistente!.":
                print("\nBusque un articulo existente!!")
            else:
                comienza_a(titulo)
        elif op == 7:
            print("\nGracias por usar el programa")
        else:
            print("\nIngrese una opcion correcta")

if __name__ == '__main__':
    principal()
