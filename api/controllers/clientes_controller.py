from flask import jsonify, request
from api.models.clientes_model import Cliente

def obtener_clientes():
    cliente = Cliente()
    clientes = cliente.obtener_todos()
    return jsonify(clientes)

def crear_cliente():
    nombre = request.json['nombre']
    numero_id = request.json['numero_id']
    direccion = request.json['direccion']
    ciudad = request.json['ciudad']
    email = request.json['email']
    celular = request.json['celular']
    cliente = Cliente()
    cliente.crear(nombre, numero_id, direccion, ciudad, email, celular)
    return jsonify({'mensaje': 'cliente creado correctamente'})

def actualizar_cliente(id):
    nombre = request.json['nombre']
    numero_id = request.json['numero_id']
    direccion = request.json['direccion']
    ciudad = request.json['ciudad']
    email = request.json['email']
    celular = request.json['celular']
    cliente = Cliente()
    cliente.actualizar(id, nombre, numero_id, direccion, ciudad, email, celular)
    return jsonify({'mensaje': 'cliente actualizado correctamente'})

def eliminar_cliente(id):
    cliente = Cliente()
    cliente.eliminar(id)
    return jsonify({'mensaje': 'cliente eliminado correctamente'})