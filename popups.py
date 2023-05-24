'''from tkinter import * 
from tkinter import messagebox

# Configuracion de la raiz

root=Tk()

def test():
   #messagebox.showinfo('Que tal Bebe','Como te encuentras?')
   #messagebox.showwarning('ALERTA','Espacio solo para administradores')
  #messagebox.showerror('ERROR','Ha ocurrido un error inesperado')
  #resultado=messagebox.askquestion('Salir','Estas seguro de salir del sistena sin guardar?')
  #if resultado =='yes':
    #root.destroy()
    #resultado=messagebox.askokcancel('Salir','deseas sobreescribir el fichero actual?')
    #if resultado:
        #root.destroy()
    resultado=messagebox.askretrycancel('Reintentar','No se puede conectar')
    if resultado:
        root.destroy()


Button(root,text='Clicame',command=test).pack()


# Finalmente bucle de la aplicacion

root.mainloop()'''

#POPUPS AVANZADOS

from tkinter import * 
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog

#Configuracion de la raiz

root=Tk()

def test():

   #color=colorchooser.askcolor(title='Elige un color')
   #print(color)
   fichero=filedialog.askopenfilename(title='Abrir un fichero')
   print(fichero)

Button(root,text='Clicame',command=test).pack()


# Finalmente bucle de la aplicacion

root.mainloop()
