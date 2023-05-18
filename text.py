from tkinter import *

# Configuracion de la raiz

root=Tk()

texto=Text(root)
texto.pack()
texto.config(width=60,height=30,font=('hollywood,14'),padx=5,pady=5,selectbackground='orange')

root.mainloop()