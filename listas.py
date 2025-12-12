list = [1, 2, 3, 4, 5]

list = list + [6, 7]
list += [8, 9, 10]

# list.append(11)  # Add un solo elemento al final de la lista
list.insert(5, 5.5)  # Insert en una posicion en concreto en el codigo
list.remove(5.5)  # eliamina el valor del indice asignado
list.extend([12, 13, 14, 15])  # Add varios elementos al final de la lista, []
list.insert(10, 11)
u = list.pop()  # Elimina el ultimo elemento de la lista y ademas te lo devuelve
# list.clear()  # Elimina todos los elementos de la lista.
print(u)
print(list)

list2 = [5, 1, 2, 3, 4]

list2.sort()  # Modifica la lista sin guardarla
print(list2)


sorted_list = sorted(list2)  # Crea nueva lista ordenada a partir de una desordenada
print(5 in sorted_list)
print(sorted_list)

list4 = list.copy()

referencia = list[3]
list[4] = 100
print(list)
print(list4)
print(referencia)
