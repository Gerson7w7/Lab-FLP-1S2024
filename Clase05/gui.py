# interfaz hecha con tkinter
from tkinter import *
from tkinter import ttk

def funcion_mostrar():
    entrada = text_area.get("1.0", END);
    consola.insert("end-1c", entrada);

raiz = Tk();

etq = Label(raiz, text="Hola mundo");
etq.pack();

comboboxPaises = ttk.Combobox(state="readonly", values=["Guatemala", "Honduras", "El Salvador", "Nicaragua"]);
comboboxPaises.place(x=100, y=100); # Posiciona el combobox en la ventana

boton = Button(raiz, text="Mostrar", command=funcion_mostrar());
boton.place(x=400, y=100); # Posiciona el boton en la ventana

text_area = Text(raiz, width=20, height=10);
text_area.place(x=100, y=150); # Posiciona el text_area en la ventana

consola = Text(raiz, width=20, height=10);
consola.place(x=500, y=150); # Posiciona el text_area en la ventana

raiz.title("Ventana de pruebas");
raiz.geometry("900x500");
raiz.mainloop();