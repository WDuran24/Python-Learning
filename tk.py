from tkinter import *

# Configuracion de la Raiz

root=Tk()
root.title('Importadora Triple V')
root.resizable(1,1)
root.config(cursor="arrow")
root.config(bg="darkblue")
root.config(bd=20)
root.config(relief="ridge")

#Variables Dinamicas

texto=StringVar()
texto.set('El Brujo Deportivo')

# Confifuracion de un Frame

frame=Frame(root,width=480,height=320)
frame.pack(fill='both',expand=1)
frame.config(cursor="spider")
frame.config(bg="red")
frame.config(bd=30)
frame.config(relief="raised")

# Configurando la etiqueta

label=Label(frame,text='Bienvenidos a Importadora Triple V')
label.pack(anchor='nw')
label.config(bg='pink',fg='darkblue',font=('comicsans',20))
label2=Label(frame,text='El mundo a tus pies')
label2.pack(anchor='center')
label2.config(bg='lightgreen',fg='orange',font=('comicsans',20))
label3=Label(frame,text='Unete a nosotros')
label3.config(bg='lightblue',fg='red',font=('comicsans',20))
label3.pack(anchor='se')
label.config(textvariable=texto)
imagen=PhotoImage(file='imagen.gif')
label4=Label(frame,image=imagen,bd=0).pack(side='left')

root.mainloop()