from tkinter import *

def sumar():
    r.set(float(n1.get())+float(n2.get()) )

def restar():
    r.set(float(n1.get())-float(n2.get()) )

def producto():
    r.set(float(n1.get())*float(n2.get()) )

def division():
    r.set(float(n1.get())/float(n2.get()) )


# Configuracion de la raiz

root=Tk()
root.config(bd=15,bg='lightblue')

n1=StringVar()
n2=StringVar()
r=StringVar()

Label(root,text='Numero 1').pack()
Entry(root,justify='center',textvariable=n1).pack() # Primer numero
Label(root,text='Numero 2').pack()
Entry(root,justify='center',textvariable=n2).pack() # Segundo numero
Label(root,text='Resultado').pack()
Entry(root,justify='center',textvariable=r,state='disabled').pack() # Resultado
Button(root,text='sumar',command=sumar).pack(side='left')
Button(root,text='restar',command=restar).pack(side='left')
Button(root,text='Producto',command=producto).pack(side='left')
Button(root,text='Division',command=division).pack(side='left')




root.mainloop()