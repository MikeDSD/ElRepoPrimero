import sys

if len(sys.argv) == 3:

    palabra = sys.argv[1]
    repeticiones = int(sys.argv[2])

    for i in range(repeticiones):
        print(palabra)
else:
    print("Epa, no pusiste bien los argumentos...")