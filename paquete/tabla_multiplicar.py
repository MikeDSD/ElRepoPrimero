import sys

print(sys.argv)

numero = int(sys.argv[1])

for elemento in range(1,10):
    print(f"{numero} x {elemento} = {numero*elemento}")