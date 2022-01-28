# Usos de un ciclo

# 1. imprimir letras
nombre = "Ramona Alcachofa"

for letra in nombre:
  print(letra)

# 2. imprimir elementos de una lista
listado_nombres = ['Toshio', 'Marielisa', 'Sandro']

for nombre in listado_nombres:
  print(nombre)

######

numeros = [100, 50, 5, 11]

for n in numeros:
  print(n)

# 3. imprimir rango de numeros 
rango1 = range(40) # rango de 40 numeros (del 0 al 39)
rango2 = range(1,41) # rango de 40 numeros del (1 al 40)
rango3 = range(5,10) # (del 5 al 9) rango de 5 numeros

# 4. Repetir un codigo
veces = range(5) 

# Ejecutar este codigo 5 veces
for i in veces:
  print("Dime un nombre: ")
  input()

#####

print("Dime la cantidad de dias que trabajas")
cantidad = int( input() )

for fulano in range(cantidad):
  print("Digite el precio ganado: ")
  precio = int(input())

# alternativa
for fulano in "."*cantidad:
  print("Digite el precio ganado: ")
  precio = int(input())