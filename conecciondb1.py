import sqlite3

conexion=sqlite3.connect('ejemplo.db')

cursor=conexion.cursor()

#cursor.execute('CREATE TABLE usuarios (nombre VARCHAR(100),edad INTEGER,email VARCHAR(100))')
#cursor.execute("INSERT INTO usuarios VALUES ('Wilder Duran Yanes',39,'mcorleone24@gmail.com')")
#cursor.execute('SELECT * FROM usuarios')
#usuario=cursor.fetchone()
#print(usuario[0])
#usuarios=[('Steven Fonseca',38,'fonseca@gmail.com'),('Andreina Yepez',24,'andre@gmail.com'),
          #('Rodolfo Smith',55,'rodo@gmail.com'),]

#cursor.executemany("INSERT INTO usuarios VALUES(?,?,?)",usuarios)
cursor.execute('SELECT * FROM usuarios')
usuarios=cursor.fetchall()

for usuario in usuarios:
    print('Nombre:',usuario[0],' - Email:',usuario[2])
conexion.commit()

conexion.close()