import random
lista = []

for i in range(100):
    lista.append(random.randint(100,200))

print(lista)

mayor = max(lista)

print(f"El mayor numero de la lista es {mayor}")

indice = 0
may = lista[0]
while indice < 99:
    if may < lista[indice + 1]:
        may = lista[indice + 1]
    indice += 1

print(f"El mayor numero calculado a mano es {may}")

indice = 0
men = lista[0]
while indice < 99:
    if men > lista[indice + 1]:
        men = lista[indice + 1]
    indice += 1

print(f"El mayor numero calculado a mano es {men}")