import re

# patron para validar un email
def esEmail(email):
    if re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return True
    return False

# patron para validar un telefono
def esTelefono(telefono):
    if re.match("^\d{4}-\d{4}$", telefono):
        return True
    return False

# patron para validar un identificador
def esIdentificador(identificador):
    if re.match("^[a-zA-Z_][a-zA-Z0-9_]*$", identificador):
        return True
    return False

print(esEmail("example@example.com"))
print(esEmail("example@example@gmail.com"))
print(esTelefono("1234-5678"))
print(esTelefono("123455-5678"))
print(esIdentificador("_miVariable"))
print(esIdentificador("9miVariable"))