from flask import Blueprint
from api.controllers.clientes_controller import obtener_clientes, crear_cliente, actualizar_cliente, eliminar_cliente


#Creación del blueprint para clientes
clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/clientes', methods=['GET'])
def obtener_clientes_route():
    return obtener_clientes()

@clientes_bp.route('/clientes', methods=['POST'])
def crear_cliente_route():
    return crear_cliente()

@clientes_bp.route('/clientes/<int:id>', methods=['PUT'])
def actualizar_cliente_route(id):
    return actualizar_cliente(id)

@clientes_bp.route('/clientes/<int:id>', methods=['DELETE'])
def eliminar_cliente_route(id):
    return eliminar_cliente(id)