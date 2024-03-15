import re;

# lista de tokens
tokens = [];
# lista de errores
errores = [];

def analizar(contenido):
    # inicializar variables
    linea = 1;
    columna = 1;
    buffer = "";
    centinela = "$"; # caracter final
    estado = 0;
    i = 0;
    contenido += centinela; # agregar centinela al final del contenido

    # recorrido del automata
    while i < len(contenido):
        # leer caracter por caracter
        c = contenido[i];

        # estado 0
        if estado == 0:
            if c == "=": # si viene un igual
                buffer += c;
                tokens.append(Token(buffer, "Signo igual", linea, columna));
                buffer = "";
                columna += 1;
                estado = 0;
            elif c == "{": # si viene un corchete abierto
                buffer += c;
                tokens.append(Token(buffer, "CorcheteAbre", linea, columna));
                buffer = "";
                columna += 1;
                estado = 0;