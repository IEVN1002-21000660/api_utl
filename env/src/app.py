from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

'''from flask_cors import CORS'''

from config import config

app=Flask(__name__)

con=MySQL(app)

@app.route("/alumnos", methods=['GET'])
def lista_alumnos():
    try:
        cursor = con.connection.cursor()
        sql = 'select * from alumnos'
        cursor.execute(sql)
        datos = cursor.fetchall()
        alumnos = []
        for fila in datos:
            alumno = {'matricula': fila[0], 'nombre': fila[1], 'apaterno': fila[2], 'amaterno': fila[3], 'correo': fila[4]}
            alumnos.append(alumno)
        # El return debe estar fuera del for
        return jsonify({'alumnos': alumnos, 'mensaje': 'Lista de alumnos', 'exito': True})
    except Exception as ex:
        return jsonify({"message": "Error al conectar a la base de datos {}".format(ex), 'exito': False})
    
def pagina_no_encontrada(error):  # Agregamos el parámetro `error`
    return "<h1>LA PAGINA QUE ESTAS BUSCANDO NO EXISTE</h1>", 404

if __name__=="__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(host='0.0.0.0',port=5000)

    import MySQLdb

try:
    db = MySQLdb.connect(host='localhost', user='yafet', passwd='1234', db='api_utl')
    print("Conexión exitosa")
except MySQLdb.Error as e:
    print(f"Error al conectar a la base de datos: {e}")