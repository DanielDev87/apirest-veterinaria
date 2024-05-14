from flask import Flask, jsonify
from config.conexion_bd import inicializar_db
from api.services.clientes_service import clientes_bp

app = Flask(__name__)

inicializar_db(app)

app.register_blueprint(clientes_bp)


@app.route('/', methods=['GET'])
def menu():
    menu_items = [
        {
            'ruta': '/dashboard',
            'descripción':'Obtener información general del sistema'
        },
        {
            'ruta': '/clientes',
            'descripción':'Crear y gestionar clientes'
        },
        {
            'ruta': '/pacientes',
            'descripción':'Crear y gestionar pacientes'
        },
        {
            'ruta': '/proveedores',
            'descripción':'Crear y gestionar proveedores'
        },
        {
            'ruta': '/facturacion',
            'descripción':'Gestión de facturas del sistema'
        },
        {
            'ruta': '/caja',
            'descripción':'Módulo de caja registradora'
        },

    ]
    
    return jsonify(menu_items)

if __name__=='__main__':
    app.run()