# CLASE 01 - 26 de Enero 2024

# Esto es un comentario de una sola linea
'''
Esto es un comentario de varias lineas
'''

# Declaración de variables 
miVariable = 10;
# imprimir en consola
print(miVariable);
# imprimir el tipo de dato de la variable
print(type(miVariable));
# asignar un nuevo valor a la variable
miVariable = "Hola Mundo";
print(f'nuevo valor de miVariable: {miVariable}');
print(f"nuevo tipo de miVariable: {type(miVariable)}");

# Operadores aritmeticos
n1 = 10;
n2 = 3;
print(f"Suma: {n1 + n2}");
print(f"Resta: {n1 - n2}");
print(f"Multiplicacion: {n1 * n2}");
print(f"Division: {n1 / n2}");
print("suma: " + str(n1 + n2));

# listas
lista = [1, 2, 3, 4, 5];
print(f"lista: {lista}");
# imprimir un elemento de la lista
print(f"elemento 0: {lista[0]}");
# imprimir un rango de elementos de la lista
print(f"elementos 0 al 2: {lista[0:3]}");
# imprimir ultimo elemento de la lista
print(f"ultimo elemento: {lista[-1]}");
print(f"ultimo elemento: {lista[len(lista) - 1]}");
# agregar un elemento a la lista
lista.append(6);
print(f"lista: {lista}");
# eliminar un elemento de la lista
lista.pop();
print(f"lista: {lista}");
# eliminar un elemento de la lista por indice
lista.pop(0);
print(f"lista: {lista}");
# insertar un elemento en la lista
lista.insert(0, 1);
print(f"lista: {lista}");
# eliminar un elemento de la lista por valor
lista.remove(1);
# unir dos listas
lista2 = [6, 7, 8, 9, 10];
lista2.extend(lista);
print(f"lista2 extendida: {lista2}");

# tuplas
tupla = (1, "hola", True, 5.5);
print(f"tupla: {tupla}");
# las tuplas son inmutables, no se pueden modificar
# tupla[0] = 2; # error

# estructuras de control
# if
if n1 > n2:
    print("n1 es mayor que n2");
elif n1 == n2:
    print("n1 es igual a n2");
else:
    print("n1 es menor que n2");

# for
print("rango de 0 a 10");
for i in range(0, 10):
    print(i);

print("rango de 0 a 10 de 2 en 2");
for i in range(0, 10, 2):
    print(i);

print("rango de 10 a 0 de 1 en 1");
for i in range(10, 0, -1):
    print(i);

print("recorrer lista");
for i in lista:
    print(i);

# while
print("while");
i = 0;
while i < 10:
    print(i);
    if i == 5:
        break;
    i += 1;

# diccionarios
# clave: valor
diccionario = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 30
};
diccionario.update({"nombre": "Pedro"});
diccionario.pop("edad");
print(f"diccionario: {diccionario}");
# obtener un valor del diccionario
print(f"nombre: {diccionario.get('nombre')}");
