#MODULO funciones matematicas basicas...

def sumar (a,b):
    return a+b

def restar (a,b):
    return a-b

def multiplicar (a,b):
    return a*b

def dividir (a,b):
    return a/b

def potencia (a,b):
    return a**b

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return(f"Persona llamada: {self.nombre} {self.apellido}")

    def comer(self):
        print("toy comiendo")