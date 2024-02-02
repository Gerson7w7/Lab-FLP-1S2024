# inserción 
def insertionSort(lista):
    print("insertion sort");
    for i in range(1, len(lista)):
        # obtener el valor de la posición actual
        actual = lista[i];
        j = i;
        # comparación de elemnentos anteriores a actual
        while j > 0 and lista[j-1] > actual:
            lista[j] = lista[j-1];
            j = j - 1;
        # insertar el elemento en la posición correcta si en caso estuviera desordenado
        lista[j] = actual;

# selection sort 
def selectionSort(lista):
    print("selection sort");
    longitud = len(lista);
    for indiceActual in range(0, longitud):
        # indice del elemento más pequeño (por ahora)
        masPequenio = indiceActual;
        for j in range(indiceActual + 1, longitud):
            # comparar el elemento actual con el más pequeño
            if lista[j] < lista[masPequenio]:
                masPequenio = j;
        # intercambiar los valores
        if masPequenio is not indiceActual:
            temp = lista[indiceActual];
            lista[indiceActual] = lista[masPequenio];
            lista[masPequenio] = temp;

# bubble sort
def bubbleSort(lista):
    print("bubble sort");
    # flag para indicar si hubo un intercambio
    intercambio = True;
    while intercambio:
        # suponer que no hay intercambio
        intercambio = False;
        for j in range(0, len(lista) - 1):
            # comparar elemento adyacente
            if lista[j] > lista[j + 1]:
                # intercambiar valores
                intercambio = True;
                temp = lista[j];
                lista[j] = lista[j + 1];
                lista[j + 1] = temp;


lista = [5, 2, 4, 6, 1, 3];
#insertionSort(lista);
#selectionSort(lista);
bubbleSort(lista);
print(lista);
