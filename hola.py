import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import sqlite3
conn = sqlite3.connect("registro.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS registro (id INTEGER PRIMARY KEY, usuario TEXT, contraseña TEXT)")
#cur.execute("INSERT INTO registro(usuario, contraseña) VALUES(?, ?)",("leo","1234",))
conn.commit()
datos = cur.execute("SELECT usuario, contraseña FROM registro")
date = datos.fetchall()
registro = []
for dat in date:
    val = dat[0]
    registro.append(dat)
registro = registro[0]
def boton(usuario, contra, datos):
    data = usuario.get()
    data1 = contra.get()
    if data in datos and data1 in datos:
        label3.configure(image=photo)
    else:
        label3.configure(image=photo1)
root = tk.Tk()
root.title("Hola mundo")
root.geometry("400x600")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

photo = PhotoImage(file="si.png")
photo1 = PhotoImage(file="noo.png")

label1 = ttk.Label(root, text="Ingrese su nombre de usario:")
entrada1 = ttk.Entry(root)

label2 = ttk.Label(root, text="Ingrese su contraseña:")
entrada2 = ttk.Entry(root)

btn = ttk.Button(text="Enviar",  command=lambda:boton(entrada1, entrada2, registro))
label3 = ttk.Label(root, image=photo)


label1.pack()
entrada1.pack()
label2.pack()
entrada2.pack()
btn.pack()
label3.pack()

root.mainloop()