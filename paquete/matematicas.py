import sys

from funciones_matematicas import *


if len(sys.argv) == 3:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    print(f"El resultado de {num1} + {num2} es {sumar(num1,num2)}")
    print(f"El resultado de {num1} - {num2} es {restar(num1,num2)}")
    print(f"El resultado de {num1} x {num2} es {multiplicar(num1,num2)}")
    print(f"El resultado de {num1} entre {num2} es {dividir(num1,num2)}")
    print(f"La Potencia de {num1} ** {num2} es {potencia(num1,num2)}")

else:
    print("Ojo con los argumentos...")
