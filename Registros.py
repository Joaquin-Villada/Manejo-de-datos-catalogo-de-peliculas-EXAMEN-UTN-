class Articulos():
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo #(un número entero)
        self.titulo = titulo #(una cadena de caracteres terminada en “.”)
        self.autor = autor #(cadena de caracteres)

    def __str__(self):
        cad = ("Codigo: {}. Titulo: {} Autor: {}.")
        return cad.format(self.codigo, self.titulo, self.autor)

#FUNCIONES AUXILIARES

def add_in_orden_codigo(vec, reg):
    n = len(vec)
    izq, der = 0, n - 1
    pos = n
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].codigo == reg.codigo:
            pos = c
            break
        if reg.codigo > vec[c].codigo:
            izq = c + 1
        else:
            der = c - 1
    if izq > der:
        pos = izq
    vec[pos:pos] = [reg]

def validar_mayor(inf, men):
    n = int(input(men))
    while n < inf:
        n = int(input("\nIngrese un numero mayor a " + str(inf - 1) + " "))
    return n

def validar_entre(inf, sup, men):
    n = int(input(men))
    while n < inf or n > sup:
        n = int(input("\nIngrese un numero entre " + str(inf) + " y " + str(sup) + " "))
    return n
