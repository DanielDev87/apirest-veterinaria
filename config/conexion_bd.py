from flaskext.mysql import MySQL

mysql = MySQL()

def inicializar_db(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'veterinaria_bd'
    mysql.init_app(app)
