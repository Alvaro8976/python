
# Bucles, explicación y ejemplos

# bucle:
#    hace lo que hay aquí hasta que el bucle termina de alguna forma

#
#
# for variable in range:
#     Hace esto hasta que termina range
#
# función range:     range(desde, hasta)

print("Ejemplo for")
for i in range(10): # números del 0 al 10
    print(i)

# while
#    # 1. while condición:
#    # 2.    Hace esto mientras condición resulta verdadero

print("Ejemplo while")
a = 1
b = 10
while a < b:
    print(a)
    a += 1

#Tu turno:

#tareas:
#    propia rama del repositorio
# 2. Resuelve el problema de la tabla de multiplicar.
# 3. Puedes hacer "commit & push" para guardar los cambios en GitHub
numero = 3 #pon aquí el número del que quieres hacer la tabla
print("tabla de multiplicar del ", numero)

print("Ejemplo for")
for i in range(1,11): # números del 0 al 10
    print(numero, "por", i, "=", i*3)

#TABLA CON while
numero=int(input("escribe un numero"))
a = 1
while a < b:
    print(numero, "por", 1, "=", i*3)
    a += 1
