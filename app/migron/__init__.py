from lib2to3.pytree import Base
import MySQLdb
# from MySQLdb import _mysql as MySQLdb
from app.migron.diccionario import *
from app.migron.configuracion import  acceso
import os

db=MySQLdb.connect(
    host=acceso['host'],
    user=acceso['usuario'],
    password=acceso['clave'],
    database=acceso['db'], 
    port=acceso['puerto'])

class Migron:
    def __init__(self, database=True, routes=True, gestor=True, controller=True):
        self.limpiar()
        
        
        # Inicializamos los procesos
        if database:
            # Creamos archivos necesarios para el Api REST
            self.file = open("app\\model\\basedatos.py", "w")
            self.crearBaseDatos()
        if gestor:
            self.gestor = open("app\\model\\gestor.py", "w")
            self.crearGestor()
        if controller:
            self.aplicacion = open("app\\controller\\__init__.py", "w")
            self.crearApp()
        if routes:
            self.rutas = open("app\\controller\\rutas.py", "w")
            self.crearRutas()
    
    def limpiar(self):
        # pass
        os.system ("cls") 
    
    def crearBaseDatos(self):
        self.c = db.cursor()
        self.c.execute("show tables;")
        # self.c.query("show tables;")
        # self.data = self.c.store_result()
        self.data = self.c.fetchall()
        
        print("Creando migracion...")
        self.file.write("from pony.orm import *\n")
        self.file.write("from datetime import date, datetime, time\n")
        self.file.write("from decimal import Decimal" + os.linesep)
        self.file.write("db = Database()")
        
        for juego in self.data:
            print(juego)
            tabla=juego[0]
            if tabla not in tables_views_not_permitted:
                print("creando tabla: {0}".format(tabla))
                self.file.write(os.linesep + "class {0}(db.Entity):\n".format(tabla.capitalize()))
                d = db.cursor()
                d.execute("describe {0};".format(tabla))
                d.fetchall()
                for reg in d:
                    tipo = reg[1].split("(")
                    auto = ''
                    
                    if tipo_dato[tipo[0]] not in ('date', 'datetime', 'LongStr', 'time'):
                        # print(tipo_dato[tipo[0]])
                        tamanho = tipo[1].split(")")
                    
                    requerido = "Required"
                    
                    if reg[2] == 'NO':
                        requerido = "Optional"
                    
                    if reg[3] == 'PRI':
                        requerido = "PrimaryKey"
                    
                    if requerido == "PrimaryKey":
                        if reg[5] == 'auto_increment':
                            auto = ", auto=True"

                    _tipo = tipo_dato[tipo[0]]
                    if _tipo == 'Decimal':
                        _tam = tamanho[0].split(",")
                        if _tam[1] == '0':
                            tamanho[0] = _tam[0]
                            _tipo = 'int'
                    
                    if _tipo == 'int':
                        self.file.write("\t{0} = {1}({2}{3})\n".format(reg[0], requerido, _tipo, auto))
                    else:
                        if _tipo in ('date', 'datetime', 'LongStr', 'time'):
                            self.file.write("\t{0} = {1}({2})\n".format(reg[0], requerido, _tipo))
                        else:                        
                            self.file.write("\t{0} = {1}({2}, {3} {4})\n".format(reg[0], requerido, _tipo, tamanho[0], auto))
                            
            self.limpiar()
        print("Migración satisfactoria...")
        self.file.close()

    def crearGestor(self):
        self.gestor.write("from app.model.basedatos import *\n")
        self.gestor.write("from app.libs.jsonapi import JSONAPI\n")
        self.gestor.write("from pony.orm.serialization import to_dict\n")
        self.gestor.write("from datetime import datetime, date\n")
        self.gestor.write("from app.migron.configuracion import acceso\n")
        self.gestor.write("import json\n" + os.linesep)
        self.gestor.write("class DBAdmin:\n")
        self.gestor.write("\tdef __init__(self):\n")
        self.gestor.write("\t\tdb.bind(provider=acceso['motor'], user=acceso['usuario'], password=acceso['clave'], host=acceso['host'], database=acceso['db'], port=acceso['puerto'])\n")
        self.gestor.write("\t\tdb.generate_mapping(create_tables=True)" + os.linesep)
        # crear gestor de tablas
        for a in self.c:
            if a[0] not in tables_views_not_permitted:
                self.gestor.write("\t@db_session\n")
                self.gestor.write("\tdef get_{0}(self):\n".format(a[0].capitalize()))
                self.gestor.write("\t\t{0} = {1}.select()\n".format(a[0], a[0].capitalize()))
                self.gestor.write("\t\treturn {'data': JSONAPI.parse("+a[0].capitalize()+", [item.to_dict() for item in "+a[0]+"])}" + os.linesep)
                self.gestor.write("\t@db_session\n")
                self.gestor.write("\tdef get_{0}_one(self, _id):\n".format(a[0].capitalize()))
                self.gestor.write("\t\t{0} = {1}[_id]\n".format(a[0], a[0].capitalize()))
                self.gestor.write("\t\tif {0}:\n".format(a[0]))
                self.gestor.write("\t\t\treturn {'data': " + a[0] + ".to_dict()}\n")
                self.gestor.write("\t\treturn {'data': 'sin data que mostrar'}" + os.linesep)
        #
        self.gestor.write("db = DBAdmin()\n")
        self.gestor.close()
        
    def crearApp(self):
        self.aplicacion.write("from flask import Flask\n")
        self.aplicacion.write("import flask.scaffold\n")
        self.aplicacion.write("flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func\n")
        self.aplicacion.write("from flask_restful import Api, Resource\n")
        self.aplicacion.write("from app.model.gestor import db\n")
        self.aplicacion.write("from app.controller.rutas import *\n")
        self.aplicacion.write("import os" + os.linesep)
        self.aplicacion.write("app = Flask(__name__)\n")
        self.aplicacion.write("api = Api(app)" + os.linesep)
        self.aplicacion.write("@app.route('/')\n")
        self.aplicacion.write("def index():\n")
        self.aplicacion.write("\treturn '<h1>Migracion Satisfactoria</h1>'" + os.linesep)
        # rutas
        for a in self.c:
            if a[0] not in tables_views_not_permitted:
                self.aplicacion.write("api.add_resource(Ruta{0}, '/api/{1}')\n".format(a[0].capitalize(), a[0]))
        self.aplicacion.write(os.linesep)
        # fin
        self.aplicacion.write("if __name__ == '__main__':\n")
        self.aplicacion.write("\tapp.run(debug=True)\n")
        self.aplicacion.close()
        
    def crearRutas(self):
        self.rutas.write("import flask.scaffold\n")
        self.rutas.write("flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func\n")
        self.rutas.write("from flask_restful import Resource\n")
        self.rutas.write("from flask import request\n")
        self.rutas.write("from flask import jsonify\n")
        self.rutas.write("import time\n")
        self.rutas.write("import json\n")
        self.rutas.write("from app.model.basedatos import *\n")
        self.rutas.write("from app.model.gestor import db" + os.linesep)
        
        for a in self.c:
            if a[0] not in tables_views_not_permitted:
                self.rutas.write("class Ruta{0}(Resource):\n".format(a[0].capitalize()))
                self.rutas.write("\t@db_session\n")
                self.rutas.write("\tdef get(self):\n")
                self.rutas.write("\t\t{0} = db.get_{1}()\n".format(a[0], a[0].capitalize()))
                self.rutas.write("\t\treturn jsonify(" + a[0] + ")" + os.linesep)

        self.rutas.close()


if __name__ == '__main__':
    gestor = Migron()
    