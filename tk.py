from tkinter import *

# Configuracion de la Raiz

root=Tk()
root.title('Importadora Triple V')
root.resizable(1,1)
root.config(cursor="arrow")
root.config(bg="darkblue")
root.config(bd=20)
root.config(relief="ridge")
# Confifuracion de un Frame

frame=Frame(root,width=480,height=320)
frame.pack(fill='both',expand=1)
frame.config(cursor="spider")
frame.config(bg="red")
frame.config(bd=30)
frame.config(relief="raised")

root.mainloop()