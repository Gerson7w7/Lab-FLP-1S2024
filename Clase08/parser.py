from Token import Token

# parser = analizador sintáctico 
class Parser():
    def __init__(self, tokens):
        self.tokens = tokens
        self.claves = []
        self.registros = []

        # flag para saber si llegamos al final del archivo
        tokenFin = Token("EOF", "EOF", 0, 0)
        self.tokens.append(tokenFin)

    def parse(self):
        self.inicio();

    # inicio -> claves registros funciones
    def inicio(self):
        self.claves()
        self.registros()
        self.funciones()

    # claves -> TK_CLAVES TK_IGUAL TK_CORCHETE_A TK_CADENA lista_claves TK_CORCHETE_C
    def claves(self):
        if self.tokens[0].nombre == "TK_CLAVES":
            self.tokens.pop(0);
            if self.tokens[0].nombre == "TK_IGUAL":
                self.tokens.pop(0);
                if self.tokens[0].nombre == "TK_CORCHETE_A":
                    self.tokens.pop(0);
                    if self.tokens[0].nombre == "TK_CADENA":
                        self.tokens.pop(0);
                        self.claves.append(self.tokens[0].lexema)
                        self.lista_claves()
                        if self.tokens[0].nombre == "TK_CORCHETE_C":
                            self.tokens.pop(0);
                        else:
                            print("Error: Se esperaba ']'")
                    else:
                        print("Error: Se esperaba una cadena")
                else:
                    print("Error: Se esperaba '['")
            else:
                print("Error: Se esperaba '='")
        else:
            print("Error: Se esperaba 'Claves'")

    # lista_claves -> TK_COMA TK_CADENA lista_claves
	#	            | e
    def lista_claves(self):
        if self.tokens[0].nombre == "TK_COMA":
            self.tokens.pop(0);
            if self.tokens[0].nombre == "TK_CADENA":
                self.tokens.pop(0);
                self.claves.append(self.tokens[0].lexema)
                self.lista_claves()
            else:
                print("Error: Se esperaba una cadena")
        else:
            pass; # pass = e = epsilon

    # registros -> TK_REGISTROS TK_IGUAL TK_CORCHETE_A registro lista_registros TK_CORCHETE_C
    def registros(self):
        if self.tokens[0].nombre == "TK_REGISTROS":
            self.tokens.pop(0);
            if self.tokens[0].nombre == "TK_IGUAL":
                self.tokens.pop(0);
                if self.tokens[0].nombre == "TK_CORCHETE_A":
                    self.tokens.pop(0);
                    self.registro()
                    self.lista_registros()
                    if self.tokens[0].nombre == "TK_CORCHETE_C":
                        self.tokens.pop(0);
                    else:
                        print("Error: Se esperaba ']'")
                else:
                    print("Error: Se esperaba '['")
            else:
                print("Error: Se esperaba '='")
        else:
            print("Error: Se esperaba 'Registros'")

    # lista_registros -> TK_COMA registro lista_registros 
	#	               | e
    def lista_registros(self):
        if self.tokens[0].nombre == "TK_COMA":
            self.tokens.pop(0);
            self.registro()
            self.lista_registros()
        else:
            pass;

    # registro -> TK_LLAVE_A valores TK_LLAVE_C 
    def registro(self):
        if self.tokens[0].nombre == "TK_LLAVE_A":
            self.tokens.pop(0);
            self.valores()
            if self.tokens[0].nombre == "TK_LLAVE_C":
                self.tokens.pop(0);
            else:
                print("Error: Se esperaba '}'")
        else:
            print("Error: Se esperaba '{'")

    # valores -> TK_COMA valor valores
	#          | e
    def valores(self):
        if self.tokens[0].nombre == "TK_COMA":
            self.tokens.pop(0);
            self.valor()
            self.valores()
        else:
            pass;

    # valor -> TK_CADENA
	#       |  TK_ENTERO
	#       |  TK_DECIMAL
    def valor(self):
        if self.tokens[0].nombre == "TK_CADENA":
            self.tokens.pop(0);
        elif self.tokens[0].nombre == "TK_ENTERO":
            self.tokens.pop(0);
        elif self.tokens[0].nombre == "TK_DECIMAL":
            self.tokens.pop(0);
        else:
            print("Error: Se esperaba un valor")

    # funciones -> funcion funciones
	#           |  e
    def funciones(self):
        self.funcion()
        self.funciones()

    # funcion -> palabra_reservada TK_PARENTESIS_A parametros TK_PARENTESIS_C TK_PUNTO_COMA
    def funcion(self):
        self.palabra_reservada()
        if self.tokens[0].nombre == "TK_PARENTESIS_A":
            self.tokens.pop(0);
            self.parametros()
            if self.tokens[0].nombre == "TK_PARENTESIS_C":
                self.tokens.pop(0);
                if self.tokens[0].nombre == "TK_PUNTO_COMA":
                    self.tokens.pop(0);
                else:
                    print("Error: Se esperaba ';'")
            else:
                print("Error: Se esperaba ')'")
        else:
            print("Error: Se esperaba '('")

    # palabra_reservada ->  TK_IMPRIMIR
 	#	    | TK_CONTEO
	#	    | TK_PROMEDIO
    def palabra_reservada(self):
        if self.tokens[0].nombre == "TK_IMPRIMIR":
            self.tokens.pop(0);
        elif self.tokens[0].nombre == "TK_CONTEO":
            self.tokens.pop(0);
        elif self.tokens[0].nombre == "TK_PROMEDIO":
            self.tokens.pop(0);
        else:
            print("Error: Se esperaba una palabra reservada")

    # parametros -> TK_COMA valor valores 
  	#              | e
    def parametros(self):
        if self.tokens[0].nombre == "TK_COMA":
            self.tokens.pop(0);
            self.valor()
            self.valores()
        else:
            pass;
