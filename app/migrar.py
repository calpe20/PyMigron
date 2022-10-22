from lib2to3.pytree import Base
import MySQLdb
from diccionario import tipo_dato
from configuracion import  acceso
import os

db=MySQLdb.connect(host=acceso['host'],user=acceso['usuario'],passwd=acceso['clave'],db=acceso['dbs'])

class BaseDatos:
    def __init__(self):
        self.limpiar()
        self.file = open("app\\basedatos.py", "w")
        self.gestor = open("app\\gestor.py", "w")
        self.aplicacion = open("app\\__init__.py", "w")
        self.rutas = open("app\\rutas.py", "w")
        self.crearBaseDatos()
        self.crearGestor()
        self.crearApp()
        self.crearRutas()
    
    def limpiar(self):
        os.system ("cls") 
    
    def crearBaseDatos(self):
        self.c=db.cursor()
        self.c.execute("show tables;")
        self.c.fetchall()
        
        print("Creando migracion...")
        self.file.write("from pony.orm import *\n")
        self.file.write("from datetime import date, datetime, time\n")
        self.file.write("from decimal import Decimal" + os.linesep)
        self.file.write("db = Database()")
        
        for juego in self.c:
            tabla=juego[0]
            if tabla not in ('viewdevoluciones','viewventas', 'cupon'):
                print("creando tabla: {0}".format(tabla))
                self.file.write(os.linesep + "class {0}(db.Entity):\n".format(tabla.capitalize()))
                d = db.cursor()
                d.execute("describe {0};".format(tabla))
                d.fetchall()
                for reg in d:
                    tipo = reg[1].split("(")
                    auto = ''
                    
                    if tipo_dato[tipo[0]] not in ('date', 'datetime', 'LongStr', 'time'):
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
        self.gestor.write("from app.basedatos import *\n")
        self.gestor.write("from app.libs.jsonapi import JSONAPI\n")
        self.gestor.write("from pony.orm.serialization import to_dict\n")
        self.gestor.write("from datetime import datetime, date\n")
        self.gestor.write("import json\n" + os.linesep)
        self.gestor.write("class DBAdmin:\n")
        self.gestor.write("\tdef __init__(self):\n")
        self.gestor.write("\t\tdb.bind(provider='mysql', user='calderon', password='@Ramoncito020286', host='158.69.1.214', database='adamakro2022')\n")
        self.gestor.write("\t\tdb.generate_mapping(create_tables=True)" + os.linesep)
        # crear gestor de tablas
        for a in self.c:
            if a[0] not in ('viewdevoluciones','viewventas'):
                self.gestor.write("\t@db_session\n")
                self.gestor.write("\tdef get_{0}(self):\n".format(a[0].capitalize()))
                self.gestor.write("\t\t{0} = {1}.select()\n".format(a[0], a[0].capitalize()))
                self.gestor.write("\t\treturn {'data': JSONAPI.parse("+a[0].capitalize()+", [item.to_dict() for item in "+a[0]+"])}" + os.linesep)
        self.gestor.write("db = DBAdmin()\n")
        self.gestor.close()
        
    def crearApp(self):
        self.aplicacion.write("from flask import Flask\n")
        self.aplicacion.write("import flask.scaffold\n")
        self.aplicacion.write("flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func\n")
        self.aplicacion.write("from flask_restful import Api, Resource\n")
        self.aplicacion.write("from app.gestor import db\n")
        self.aplicacion.write("from app.rutas import *\n")
        self.aplicacion.write("import os" + os.linesep)
        self.aplicacion.write("app = Flask(__name__)\n")
        self.aplicacion.write("api = Api(app)" + os.linesep)
        self.aplicacion.write("@app.route('/')\n")
        self.aplicacion.write("def index():\n")
        self.aplicacion.write("\treturn '<h1>Migracion Satisfactoria</h1>'" + os.linesep)
        # rutas
        for a in self.c:
            if a[0] not in ('viewdevoluciones','viewventas'):
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
        self.rutas.write("import time\n")
        self.rutas.write("import json\n")
        self.rutas.write("from app.basedatos import *\n")
        self.rutas.write("from app.gestor import db\n")
        self.rutas.write("from app.libs.jsonapi import JSONAPI" + os.linesep)
        
        for a in self.c:
            if a[0] not in ('viewdevoluciones','viewventas'):
                self.rutas.write("class Ruta{0}(Resource):\n".format(a[0].capitalize()))
                self.rutas.write("\t@db_session\n")
                self.rutas.write("\tdef get(self):\n")
                self.rutas.write("\t\t{0} = {1}.select()\n".format(a[0], a[0].capitalize()))
                self.rutas.write("\t\treturn {'data': JSONAPI.parse("+a[0].capitalize()+", [item.to_dict() for item in "+a[0]+"])}" + os.linesep)

        self.rutas.close()


if __name__ == '__main__':
    gestor = BaseDatos()
    