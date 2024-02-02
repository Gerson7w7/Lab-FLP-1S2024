# busqueda secuencial
def busquedaSecuencial(lista, elementoBuscado):
    for i in range(0, len(lista)):
        if lista[i] == elementoBuscado:
            return True;
    return False;

# busqueda binaria 
def busquedaBinaria(lista, elementoBuscado):
    # límites de la lista
    primero = 0;
    ultimo = len(lista) - 1;
    # mientras el límite inferior sea menor o igual al límite superior
    while primero <= ultimo:
        # punto medio de la lista
        medio = (primero + ultimo) // 2; # division entera
        # si el punto medio es el elemento buscado
        if lista[medio] == elementoBuscado:
            return True;
        # si el elemento buscado es menor que el punto medio
        elif lista[medio] > elementoBuscado:
            ultimo = medio - 1;
        # si el elemento buscado es mayor que el punto medio
        else:
            primero = medio + 1;
    return False;

elementoBuscado = 10;
lista = [5, 2, 4, 6, 1, 3];
print("Se encontró el elemento? ", busquedaSecuencial(lista, elementoBuscado));
lista.sort();
elementoBuscado = 5;
print("Se encontró el elemento? ", busquedaBinaria(lista, elementoBuscado));
