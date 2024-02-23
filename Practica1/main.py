from Instruccion import Instruccion;

def splitContenido(contenido, separador):
    listaAux = contenido.split(f'{separador}')
    return listaAux;

def leerArchivo(nombreArchivo):
    archivo = open(f'{nombreArchivo}.humanworld', "r")
    contenido = archivo.read()
    archivo.close()
    return contenido

def main():
    instrucciones = [];
    print("Bienvenido a Human World")
    print("Por favor ingrese el nombre del archivo que desea leer")
    nombreArchivo = input()
    contenido = leerArchivo(nombreArchivo);
    lista = splitContenido(contenido, "\n");
    for i in range(len(lista)):
        instruccion = splitContenido(lista[i], ":");
        for j in range(len(instruccion)):
            parametros = [];
            if (len(instruccion) > 1):
                parametros = splitContenido(instruccion[1], ",");
        instrucciones.append(Instruccion(instruccion[0], parametros));

    for instruccion in instrucciones:
        print(instruccion.instruccion);
        print(instruccion.parametros);

main();