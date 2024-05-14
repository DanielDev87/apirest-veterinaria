from config.conexion_bd import mysql

class Cliente:
    def obtener_todos(self):
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM clientes')
        clientes = cur.fetchall()
        cur.close()
        return clientes
    
    def crear(self, nombre, numero_id, direccion, ciudad, email, celular):
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO clientes (nombre, numero_id, direccion, ciudad, email, celular) VALUES (%s, %s, %s,%s, %s, %s,%s)', (nombre, numero_id, direccion, ciudad, email, celular))
        mysql.connection.commit()
        cur.close()
    
    def actualizar(self, id, nombre, numero_id, direccion, ciudad, email, celular):
        cur = mysql.connection.cursor()
        cur.execute('UPDATE clientes SET nombre = %s, numero_id = %s, direccion = %s, ciudad = %s, email = %s, celular = %s WHERE id = %s', (nombre, numero_id, direccion, ciudad, email, celular, id))
        mysql.connection.commit()
        cur.close()
    
    def eliminar(self, id):
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM clientes WHERE id = %s', (id,))
        mysql.connection.commit()
        cur.close()
    
    
