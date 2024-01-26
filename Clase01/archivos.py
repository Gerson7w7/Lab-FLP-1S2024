from Persona import Persona;
from pickle import dump, load; # importar funciones de pickle (serialización)

def leerPersona():
    print("===== Leer objeto =====")
    print("Ingrese el nombre del archivo: ");
    nombre = input();
    print("Leyendo objeto...");
    archivo = open(nombre, "rb");
    persona = load(archivo);
    archivo.close();
    print("Objeto leido con exito.");
    print("Nombre: " + persona.getNombre());
    print("Apellido: " + persona.getApellido());
    print("Edad: " + str(persona.getEdad()));
    print("Es mayor de edad: " + str(persona.esMayorDeEdad()));
    print("\n");

def guardarPersona():
    print("===== Guardar objeto =====")
    print("Ingrese el nombre del archivo: ");
    nombreArchivo = input();
    print("Ingrese el nombre de la persona: ");
    nombre = input();
    print("Ingrese el apellido de la persona: ");
    apellido = input();
    print("Ingrese la edad de la persona: ");
    edad = int(input());
    print("Creando objeto...");
    persona = Persona(nombre, apellido, edad);
    print("Objeto creado con exito.");
    print("Guardando objeto...");
    archivo = open(nombreArchivo, "wb");
    dump(persona, archivo);
    archivo.close();
    print("Objeto guardado con exito.");
    print("\n");

def leerArchivo():
    print("===== Leer archivo =====")
    print("Ingrese el nombre del archivo: ");
    nombre = input();
    print("Leyendo archivo...");
    archivo = open(nombre, "r");
    contenido = archivo.read();
    archivo.close();
    print("Contenido del archivo:");
    print(contenido);
    print("\n");

def agregarContenido():
    print("===== Agregar contenido =====")
    print("Ingrese el nombre del archivo: ");
    nombre = input();
    print("Ingrese el contenido: ");
    contenido = input();
    print("Agregando contenido...");
    archivo = open(nombre, "a");
    archivo.write(contenido);
    archivo.close();
    print("Contenido agregado con exito.");
    print("\n");

def crearArchivo():
    print("===== Crear archivo =====")
    print("Ingrese el nombre del archivo: ");
    nombre = input();
    print("Creando archivo...");
    archivo = open(nombre, "w");
    archivo.close();
    print("Archivo creado con exito.");
    print("\n");

def main():
    opcion = 0;
    while True:
        # menú 
        print("===== Menú =====");
        print("1. Crear archivo");
        print("2. Leer archivo");
        print("3. Agregar contenido al archivo");
        print("4. Guardar objeto en archivo");
        print("5. Leer objeto de archivo");
        print("6. Salir");
        # leer opción
        opcion = input("Ingrese una opción: ");
        # validar opción
        if opcion.isnumeric() == False:
            print("Opción no válida");
            continue;
        # convertir a entero
        opcion = int(opcion);
        # ejecutar opción
        if opcion == 1:
            crearArchivo();
        elif opcion == 2:
            leerArchivo();
        elif opcion == 3:
            agregarContenido();
        elif opcion == 4:
            guardarPersona();
        elif opcion == 5:
            leerPersona();
        elif opcion == 6:
            print("Saliendo...");
            break;
        else:
            print("Opción no válida");

# ejecutar main
if __name__ == "__main__":
    main();