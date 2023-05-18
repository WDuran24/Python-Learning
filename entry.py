from tkinter import *

# Configuracion de la raiz

root=Tk()

"""
frame=Frame(root)
frame.pack()

entry=Entry(frame)
entry.pack(side='right')

label=Label(frame,text='Nombre  ')
label.pack(side='left')

frame2=Frame(root)
frame2.pack()

entry2=Entry(frame2)
entry2.pack(side='right')

label2=Label(frame2,text='Apellidos')
label2.pack(side='left')

# Finalmente bucle de la aplicacion

root.mainloop()"""

# Reubicacion por cuadricula

label=Label(root,text='Nombres')
label.grid(row=0,column=0,sticky='e',padx=5,pady=5)

entry=Entry(root)
entry.grid(row=0,column=1,padx=5,pady=5)
entry.config(justify='left',state='normal')

label2=Label(root,text='Password')
label2.grid(row=1,column=0,sticky='e',padx=5,pady=5)

entry2=Entry(root)
entry2.grid(row=1,column=1,padx=5,pady=5)
entry2.config(justify='left',show='*')

root.mainloop()



