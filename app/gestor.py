from app.basedatos import *
from app.libs.jsonapi import JSONAPI
from pony.orm.serialization import to_dict
from datetime import datetime, date
from app.migron.configuracion import acceso
import json

class DBAdmin:
	def __init__(self):
		db.bind(provider=acceso['motor'], user=acceso['usuario'], password=acceso['clave'], host=acceso['host'], database=acceso['db'], port=acceso['puerto'])
		db.generate_mapping(create_tables=True)
	@db_session
	def get_Accesos(self):
		accesos = Accesos.select()
		return {'data': JSONAPI.parse(Accesos, [item.to_dict() for item in accesos])}
	@db_session
	def get_Accesos_one(self, _id):
		accesos = Accesos[_id]
		if accesos:
			return {'data': accesos.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Acompanante(self):
		acompanante = Acompanante.select()
		return {'data': JSONAPI.parse(Acompanante, [item.to_dict() for item in acompanante])}
	@db_session
	def get_Acompanante_one(self, _id):
		acompanante = Acompanante[_id]
		if acompanante:
			return {'data': acompanante.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Agencias(self):
		agencias = Agencias.select()
		return {'data': JSONAPI.parse(Agencias, [item.to_dict() for item in agencias])}
	@db_session
	def get_Agencias_one(self, _id):
		agencias = Agencias[_id]
		if agencias:
			return {'data': agencias.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Almacen(self):
		almacen = Almacen.select()
		return {'data': JSONAPI.parse(Almacen, [item.to_dict() for item in almacen])}
	@db_session
	def get_Almacen_one(self, _id):
		almacen = Almacen[_id]
		if almacen:
			return {'data': almacen.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Aperturas(self):
		aperturas = Aperturas.select()
		return {'data': JSONAPI.parse(Aperturas, [item.to_dict() for item in aperturas])}
	@db_session
	def get_Aperturas_one(self, _id):
		aperturas = Aperturas[_id]
		if aperturas:
			return {'data': aperturas.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Areas(self):
		areas = Areas.select()
		return {'data': JSONAPI.parse(Areas, [item.to_dict() for item in areas])}
	@db_session
	def get_Areas_one(self, _id):
		areas = Areas[_id]
		if areas:
			return {'data': areas.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Articulo(self):
		articulo = Articulo.select()
		return {'data': JSONAPI.parse(Articulo, [item.to_dict() for item in articulo])}
	@db_session
	def get_Articulo_one(self, _id):
		articulo = Articulo[_id]
		if articulo:
			return {'data': articulo.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Articuloproveedor(self):
		articuloproveedor = Articuloproveedor.select()
		return {'data': JSONAPI.parse(Articuloproveedor, [item.to_dict() for item in articuloproveedor])}
	@db_session
	def get_Articuloproveedor_one(self, _id):
		articuloproveedor = Articuloproveedor[_id]
		if articuloproveedor:
			return {'data': articuloproveedor.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Articulotag(self):
		articulotag = Articulotag.select()
		return {'data': JSONAPI.parse(Articulotag, [item.to_dict() for item in articulotag])}
	@db_session
	def get_Articulotag_one(self, _id):
		articulotag = Articulotag[_id]
		if articulotag:
			return {'data': articulotag.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Asistencia(self):
		asistencia = Asistencia.select()
		return {'data': JSONAPI.parse(Asistencia, [item.to_dict() for item in asistencia])}
	@db_session
	def get_Asistencia_one(self, _id):
		asistencia = Asistencia[_id]
		if asistencia:
			return {'data': asistencia.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Auditor(self):
		auditor = Auditor.select()
		return {'data': JSONAPI.parse(Auditor, [item.to_dict() for item in auditor])}
	@db_session
	def get_Auditor_one(self, _id):
		auditor = Auditor[_id]
		if auditor:
			return {'data': auditor.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Cajachcab(self):
		cajachcab = Cajachcab.select()
		return {'data': JSONAPI.parse(Cajachcab, [item.to_dict() for item in cajachcab])}
	@db_session
	def get_Cajachcab_one(self, _id):
		cajachcab = Cajachcab[_id]
		if cajachcab:
			return {'data': cajachcab.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Cajachdet(self):
		cajachdet = Cajachdet.select()
		return {'data': JSONAPI.parse(Cajachdet, [item.to_dict() for item in cajachdet])}
	@db_session
	def get_Cajachdet_one(self, _id):
		cajachdet = Cajachdet[_id]
		if cajachdet:
			return {'data': cajachdet.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Cajadet(self):
		cajadet = Cajadet.select()
		return {'data': JSONAPI.parse(Cajadet, [item.to_dict() for item in cajadet])}
	@db_session
	def get_Cajadet_one(self, _id):
		cajadet = Cajadet[_id]
		if cajadet:
			return {'data': cajadet.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Cajagas(self):
		cajagas = Cajagas.select()
		return {'data': JSONAPI.parse(Cajagas, [item.to_dict() for item in cajagas])}
	@db_session
	def get_Cajagas_one(self, _id):
		cajagas = Cajagas[_id]
		if cajagas:
			return {'data': cajagas.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Cajamv(self):
		cajamv = Cajamv.select()
		return {'data': JSONAPI.parse(Cajamv, [item.to_dict() for item in cajamv])}
	@db_session
	def get_Cajamv_one(self, _id):
		cajamv = Cajamv[_id]
		if cajamv:
			return {'data': cajamv.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Cajati(self):
		cajati = Cajati.select()
		return {'data': JSONAPI.parse(Cajati, [item.to_dict() for item in cajati])}
	@db_session
	def get_Cajati_one(self, _id):
		cajati = Cajati[_id]
		if cajati:
			return {'data': cajati.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Cajero(self):
		cajero = Cajero.select()
		return {'data': JSONAPI.parse(Cajero, [item.to_dict() for item in cajero])}
	@db_session
	def get_Cajero_one(self, _id):
		cajero = Cajero[_id]
		if cajero:
			return {'data': cajero.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Cajeromv(self):
		cajeromv = Cajeromv.select()
		return {'data': JSONAPI.parse(Cajeromv, [item.to_dict() for item in cajeromv])}
	@db_session
	def get_Cajeromv_one(self, _id):
		cajeromv = Cajeromv[_id]
		if cajeromv:
			return {'data': cajeromv.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Canal(self):
		canal = Canal.select()
		return {'data': JSONAPI.parse(Canal, [item.to_dict() for item in canal])}
	@db_session
	def get_Canal_one(self, _id):
		canal = Canal[_id]
		if canal:
			return {'data': canal.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Cargos(self):
		cargos = Cargos.select()
		return {'data': JSONAPI.parse(Cargos, [item.to_dict() for item in cargos])}
	@db_session
	def get_Cargos_one(self, _id):
		cargos = Cargos[_id]
		if cargos:
			return {'data': cargos.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Categoria(self):
		categoria = Categoria.select()
		return {'data': JSONAPI.parse(Categoria, [item.to_dict() for item in categoria])}
	@db_session
	def get_Categoria_one(self, _id):
		categoria = Categoria[_id]
		if categoria:
			return {'data': categoria.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Cliempre(self):
		cliempre = Cliempre.select()
		return {'data': JSONAPI.parse(Cliempre, [item.to_dict() for item in cliempre])}
	@db_session
	def get_Cliempre_one(self, _id):
		cliempre = Cliempre[_id]
		if cliempre:
			return {'data': cliempre.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Colores(self):
		colores = Colores.select()
		return {'data': JSONAPI.parse(Colores, [item.to_dict() for item in colores])}
	@db_session
	def get_Colores_one(self, _id):
		colores = Colores[_id]
		if colores:
			return {'data': colores.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Comentarios(self):
		comentarios = Comentarios.select()
		return {'data': JSONAPI.parse(Comentarios, [item.to_dict() for item in comentarios])}
	@db_session
	def get_Comentarios_one(self, _id):
		comentarios = Comentarios[_id]
		if comentarios:
			return {'data': comentarios.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Comisionescab(self):
		comisionescab = Comisionescab.select()
		return {'data': JSONAPI.parse(Comisionescab, [item.to_dict() for item in comisionescab])}
	@db_session
	def get_Comisionescab_one(self, _id):
		comisionescab = Comisionescab[_id]
		if comisionescab:
			return {'data': comisionescab.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Comisionesdet(self):
		comisionesdet = Comisionesdet.select()
		return {'data': JSONAPI.parse(Comisionesdet, [item.to_dict() for item in comisionesdet])}
	@db_session
	def get_Comisionesdet_one(self, _id):
		comisionesdet = Comisionesdet[_id]
		if comisionesdet:
			return {'data': comisionesdet.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Compatible(self):
		compatible = Compatible.select()
		return {'data': JSONAPI.parse(Compatible, [item.to_dict() for item in compatible])}
	@db_session
	def get_Compatible_one(self, _id):
		compatible = Compatible[_id]
		if compatible:
			return {'data': compatible.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Compatibles(self):
		compatibles = Compatibles.select()
		return {'data': JSONAPI.parse(Compatibles, [item.to_dict() for item in compatibles])}
	@db_session
	def get_Compatibles_one(self, _id):
		compatibles = Compatibles[_id]
		if compatibles:
			return {'data': compatibles.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Compras(self):
		compras = Compras.select()
		return {'data': JSONAPI.parse(Compras, [item.to_dict() for item in compras])}
	@db_session
	def get_Compras_one(self, _id):
		compras = Compras[_id]
		if compras:
			return {'data': compras.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Concepto(self):
		concepto = Concepto.select()
		return {'data': JSONAPI.parse(Concepto, [item.to_dict() for item in concepto])}
	@db_session
	def get_Concepto_one(self, _id):
		concepto = Concepto[_id]
		if concepto:
			return {'data': concepto.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Condicion(self):
		condicion = Condicion.select()
		return {'data': JSONAPI.parse(Condicion, [item.to_dict() for item in condicion])}
	@db_session
	def get_Condicion_one(self, _id):
		condicion = Condicion[_id]
		if condicion:
			return {'data': condicion.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Consolidadocab(self):
		consolidadocab = Consolidadocab.select()
		return {'data': JSONAPI.parse(Consolidadocab, [item.to_dict() for item in consolidadocab])}
	@db_session
	def get_Consolidadocab_one(self, _id):
		consolidadocab = Consolidadocab[_id]
		if consolidadocab:
			return {'data': consolidadocab.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Consolidadodet(self):
		consolidadodet = Consolidadodet.select()
		return {'data': JSONAPI.parse(Consolidadodet, [item.to_dict() for item in consolidadodet])}
	@db_session
	def get_Consolidadodet_one(self, _id):
		consolidadodet = Consolidadodet[_id]
		if consolidadodet:
			return {'data': consolidadodet.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Correlativos(self):
		correlativos = Correlativos.select()
		return {'data': JSONAPI.parse(Correlativos, [item.to_dict() for item in correlativos])}
	@db_session
	def get_Correlativos_one(self, _id):
		correlativos = Correlativos[_id]
		if correlativos:
			return {'data': correlativos.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Departamento(self):
		departamento = Departamento.select()
		return {'data': JSONAPI.parse(Departamento, [item.to_dict() for item in departamento])}
	@db_session
	def get_Departamento_one(self, _id):
		departamento = Departamento[_id]
		if departamento:
			return {'data': departamento.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Dias(self):
		dias = Dias.select()
		return {'data': JSONAPI.parse(Dias, [item.to_dict() for item in dias])}
	@db_session
	def get_Dias_one(self, _id):
		dias = Dias[_id]
		if dias:
			return {'data': dias.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Direcciones(self):
		direcciones = Direcciones.select()
		return {'data': JSONAPI.parse(Direcciones, [item.to_dict() for item in direcciones])}
	@db_session
	def get_Direcciones_one(self, _id):
		direcciones = Direcciones[_id]
		if direcciones:
			return {'data': direcciones.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Documentos(self):
		documentos = Documentos.select()
		return {'data': JSONAPI.parse(Documentos, [item.to_dict() for item in documentos])}
	@db_session
	def get_Documentos_one(self, _id):
		documentos = Documentos[_id]
		if documentos:
			return {'data': documentos.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Empresas(self):
		empresas = Empresas.select()
		return {'data': JSONAPI.parse(Empresas, [item.to_dict() for item in empresas])}
	@db_session
	def get_Empresas_one(self, _id):
		empresas = Empresas[_id]
		if empresas:
			return {'data': empresas.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Escalas(self):
		escalas = Escalas.select()
		return {'data': JSONAPI.parse(Escalas, [item.to_dict() for item in escalas])}
	@db_session
	def get_Escalas_one(self, _id):
		escalas = Escalas[_id]
		if escalas:
			return {'data': escalas.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Existencia(self):
		existencia = Existencia.select()
		return {'data': JSONAPI.parse(Existencia, [item.to_dict() for item in existencia])}
	@db_session
	def get_Existencia_one(self, _id):
		existencia = Existencia[_id]
		if existencia:
			return {'data': existencia.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Formapago(self):
		formapago = Formapago.select()
		return {'data': JSONAPI.parse(Formapago, [item.to_dict() for item in formapago])}
	@db_session
	def get_Formapago_one(self, _id):
		formapago = Formapago[_id]
		if formapago:
			return {'data': formapago.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Habitacion(self):
		habitacion = Habitacion.select()
		return {'data': JSONAPI.parse(Habitacion, [item.to_dict() for item in habitacion])}
	@db_session
	def get_Habitacion_one(self, _id):
		habitacion = Habitacion[_id]
		if habitacion:
			return {'data': habitacion.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Imagenesps(self):
		imagenesps = Imagenesps.select()
		return {'data': JSONAPI.parse(Imagenesps, [item.to_dict() for item in imagenesps])}
	@db_session
	def get_Imagenesps_one(self, _id):
		imagenesps = Imagenesps[_id]
		if imagenesps:
			return {'data': imagenesps.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Iniciocab(self):
		iniciocab = Iniciocab.select()
		return {'data': JSONAPI.parse(Iniciocab, [item.to_dict() for item in iniciocab])}
	@db_session
	def get_Iniciocab_one(self, _id):
		iniciocab = Iniciocab[_id]
		if iniciocab:
			return {'data': iniciocab.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Iniciodetalle(self):
		iniciodetalle = Iniciodetalle.select()
		return {'data': JSONAPI.parse(Iniciodetalle, [item.to_dict() for item in iniciodetalle])}
	@db_session
	def get_Iniciodetalle_one(self, _id):
		iniciodetalle = Iniciodetalle[_id]
		if iniciodetalle:
			return {'data': iniciodetalle.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Kardex(self):
		kardex = Kardex.select()
		return {'data': JSONAPI.parse(Kardex, [item.to_dict() for item in kardex])}
	@db_session
	def get_Kardex_one(self, _id):
		kardex = Kardex[_id]
		if kardex:
			return {'data': kardex.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Listaprecios(self):
		listaprecios = Listaprecios.select()
		return {'data': JSONAPI.parse(Listaprecios, [item.to_dict() for item in listaprecios])}
	@db_session
	def get_Listaprecios_one(self, _id):
		listaprecios = Listaprecios[_id]
		if listaprecios:
			return {'data': listaprecios.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Lotes(self):
		lotes = Lotes.select()
		return {'data': JSONAPI.parse(Lotes, [item.to_dict() for item in lotes])}
	@db_session
	def get_Lotes_one(self, _id):
		lotes = Lotes[_id]
		if lotes:
			return {'data': lotes.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Marca(self):
		marca = Marca.select()
		return {'data': JSONAPI.parse(Marca, [item.to_dict() for item in marca])}
	@db_session
	def get_Marca_one(self, _id):
		marca = Marca[_id]
		if marca:
			return {'data': marca.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Monedas(self):
		monedas = Monedas.select()
		return {'data': JSONAPI.parse(Monedas, [item.to_dict() for item in monedas])}
	@db_session
	def get_Monedas_one(self, _id):
		monedas = Monedas[_id]
		if monedas:
			return {'data': monedas.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Motivos(self):
		motivos = Motivos.select()
		return {'data': JSONAPI.parse(Motivos, [item.to_dict() for item in motivos])}
	@db_session
	def get_Motivos_one(self, _id):
		motivos = Motivos[_id]
		if motivos:
			return {'data': motivos.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Motivos_caja(self):
		motivos_caja = Motivos_caja.select()
		return {'data': JSONAPI.parse(Motivos_caja, [item.to_dict() for item in motivos_caja])}
	@db_session
	def get_Motivos_caja_one(self, _id):
		motivos_caja = Motivos_caja[_id]
		if motivos_caja:
			return {'data': motivos_caja.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Movimientodet(self):
		movimientodet = Movimientodet.select()
		return {'data': JSONAPI.parse(Movimientodet, [item.to_dict() for item in movimientodet])}
	@db_session
	def get_Movimientodet_one(self, _id):
		movimientodet = Movimientodet[_id]
		if movimientodet:
			return {'data': movimientodet.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Movimientoscab(self):
		movimientoscab = Movimientoscab.select()
		return {'data': JSONAPI.parse(Movimientoscab, [item.to_dict() for item in movimientoscab])}
	@db_session
	def get_Movimientoscab_one(self, _id):
		movimientoscab = Movimientoscab[_id]
		if movimientoscab:
			return {'data': movimientoscab.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Movimientosdet(self):
		movimientosdet = Movimientosdet.select()
		return {'data': JSONAPI.parse(Movimientosdet, [item.to_dict() for item in movimientosdet])}
	@db_session
	def get_Movimientosdet_one(self, _id):
		movimientosdet = Movimientosdet[_id]
		if movimientosdet:
			return {'data': movimientosdet.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Nbf_anulado(self):
		nbf_anulado = Nbf_anulado.select()
		return {'data': JSONAPI.parse(Nbf_anulado, [item.to_dict() for item in nbf_anulado])}
	@db_session
	def get_Nbf_anulado_one(self, _id):
		nbf_anulado = Nbf_anulado[_id]
		if nbf_anulado:
			return {'data': nbf_anulado.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Nbf_respuesta(self):
		nbf_respuesta = Nbf_respuesta.select()
		return {'data': JSONAPI.parse(Nbf_respuesta, [item.to_dict() for item in nbf_respuesta])}
	@db_session
	def get_Nbf_respuesta_one(self, _id):
		nbf_respuesta = Nbf_respuesta[_id]
		if nbf_respuesta:
			return {'data': nbf_respuesta.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Opercom(self):
		opercom = Opercom.select()
		return {'data': JSONAPI.parse(Opercom, [item.to_dict() for item in opercom])}
	@db_session
	def get_Opercom_one(self, _id):
		opercom = Opercom[_id]
		if opercom:
			return {'data': opercom.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Opergast(self):
		opergast = Opergast.select()
		return {'data': JSONAPI.parse(Opergast, [item.to_dict() for item in opergast])}
	@db_session
	def get_Opergast_one(self, _id):
		opergast = Opergast[_id]
		if opergast:
			return {'data': opergast.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Opermv(self):
		opermv = Opermv.select()
		return {'data': JSONAPI.parse(Opermv, [item.to_dict() for item in opermv])}
	@db_session
	def get_Opermv_one(self, _id):
		opermv = Opermv[_id]
		if opermv:
			return {'data': opermv.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Operpag(self):
		operpag = Operpag.select()
		return {'data': JSONAPI.parse(Operpag, [item.to_dict() for item in operpag])}
	@db_session
	def get_Operpag_one(self, _id):
		operpag = Operpag[_id]
		if operpag:
			return {'data': operpag.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Operti(self):
		operti = Operti.select()
		return {'data': JSONAPI.parse(Operti, [item.to_dict() for item in operti])}
	@db_session
	def get_Operti_one(self, _id):
		operti = Operti[_id]
		if operti:
			return {'data': operti.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Pedidos_cab(self):
		pedidos_cab = Pedidos_cab.select()
		return {'data': JSONAPI.parse(Pedidos_cab, [item.to_dict() for item in pedidos_cab])}
	@db_session
	def get_Pedidos_cab_one(self, _id):
		pedidos_cab = Pedidos_cab[_id]
		if pedidos_cab:
			return {'data': pedidos_cab.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Pedidos_det(self):
		pedidos_det = Pedidos_det.select()
		return {'data': JSONAPI.parse(Pedidos_det, [item.to_dict() for item in pedidos_det])}
	@db_session
	def get_Pedidos_det_one(self, _id):
		pedidos_det = Pedidos_det[_id]
		if pedidos_det:
			return {'data': pedidos_det.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Periodo(self):
		periodo = Periodo.select()
		return {'data': JSONAPI.parse(Periodo, [item.to_dict() for item in periodo])}
	@db_session
	def get_Periodo_one(self, _id):
		periodo = Periodo[_id]
		if periodo:
			return {'data': periodo.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Personal(self):
		personal = Personal.select()
		return {'data': JSONAPI.parse(Personal, [item.to_dict() for item in personal])}
	@db_session
	def get_Personal_one(self, _id):
		personal = Personal[_id]
		if personal:
			return {'data': personal.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Planilla_cab(self):
		planilla_cab = Planilla_cab.select()
		return {'data': JSONAPI.parse(Planilla_cab, [item.to_dict() for item in planilla_cab])}
	@db_session
	def get_Planilla_cab_one(self, _id):
		planilla_cab = Planilla_cab[_id]
		if planilla_cab:
			return {'data': planilla_cab.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Planilla_det(self):
		planilla_det = Planilla_det.select()
		return {'data': JSONAPI.parse(Planilla_det, [item.to_dict() for item in planilla_det])}
	@db_session
	def get_Planilla_det_one(self, _id):
		planilla_det = Planilla_det[_id]
		if planilla_det:
			return {'data': planilla_det.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Premisoprecio(self):
		premisoprecio = Premisoprecio.select()
		return {'data': JSONAPI.parse(Premisoprecio, [item.to_dict() for item in premisoprecio])}
	@db_session
	def get_Premisoprecio_one(self, _id):
		premisoprecio = Premisoprecio[_id]
		if premisoprecio:
			return {'data': premisoprecio.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Prestamocab(self):
		prestamocab = Prestamocab.select()
		return {'data': JSONAPI.parse(Prestamocab, [item.to_dict() for item in prestamocab])}
	@db_session
	def get_Prestamocab_one(self, _id):
		prestamocab = Prestamocab[_id]
		if prestamocab:
			return {'data': prestamocab.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Prestamodet(self):
		prestamodet = Prestamodet.select()
		return {'data': JSONAPI.parse(Prestamodet, [item.to_dict() for item in prestamodet])}
	@db_session
	def get_Prestamodet_one(self, _id):
		prestamodet = Prestamodet[_id]
		if prestamodet:
			return {'data': prestamodet.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Primercosteo(self):
		primercosteo = Primercosteo.select()
		return {'data': JSONAPI.parse(Primercosteo, [item.to_dict() for item in primercosteo])}
	@db_session
	def get_Primercosteo_one(self, _id):
		primercosteo = Primercosteo[_id]
		if primercosteo:
			return {'data': primercosteo.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Procedencia(self):
		procedencia = Procedencia.select()
		return {'data': JSONAPI.parse(Procedencia, [item.to_dict() for item in procedencia])}
	@db_session
	def get_Procedencia_one(self, _id):
		procedencia = Procedencia[_id]
		if procedencia:
			return {'data': procedencia.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Prodtallacolor(self):
		prodtallacolor = Prodtallacolor.select()
		return {'data': JSONAPI.parse(Prodtallacolor, [item.to_dict() for item in prodtallacolor])}
	@db_session
	def get_Prodtallacolor_one(self, _id):
		prodtallacolor = Prodtallacolor[_id]
		if prodtallacolor:
			return {'data': prodtallacolor.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Productofoto(self):
		productofoto = Productofoto.select()
		return {'data': JSONAPI.parse(Productofoto, [item.to_dict() for item in productofoto])}
	@db_session
	def get_Productofoto_one(self, _id):
		productofoto = Productofoto[_id]
		if productofoto:
			return {'data': productofoto.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Profesion(self):
		profesion = Profesion.select()
		return {'data': JSONAPI.parse(Profesion, [item.to_dict() for item in profesion])}
	@db_session
	def get_Profesion_one(self, _id):
		profesion = Profesion[_id]
		if profesion:
			return {'data': profesion.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Promocab(self):
		promocab = Promocab.select()
		return {'data': JSONAPI.parse(Promocab, [item.to_dict() for item in promocab])}
	@db_session
	def get_Promocab_one(self, _id):
		promocab = Promocab[_id]
		if promocab:
			return {'data': promocab.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Promodet(self):
		promodet = Promodet.select()
		return {'data': JSONAPI.parse(Promodet, [item.to_dict() for item in promodet])}
	@db_session
	def get_Promodet_one(self, _id):
		promodet = Promodet[_id]
		if promodet:
			return {'data': promodet.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Proveedores(self):
		proveedores = Proveedores.select()
		return {'data': JSONAPI.parse(Proveedores, [item.to_dict() for item in proveedores])}
	@db_session
	def get_Proveedores_one(self, _id):
		proveedores = Proveedores[_id]
		if proveedores:
			return {'data': proveedores.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Provincia(self):
		provincia = Provincia.select()
		return {'data': JSONAPI.parse(Provincia, [item.to_dict() for item in provincia])}
	@db_session
	def get_Provincia_one(self, _id):
		provincia = Provincia[_id]
		if provincia:
			return {'data': provincia.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Region(self):
		region = Region.select()
		return {'data': JSONAPI.parse(Region, [item.to_dict() for item in region])}
	@db_session
	def get_Region_one(self, _id):
		region = Region[_id]
		if region:
			return {'data': region.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Reservacab(self):
		reservacab = Reservacab.select()
		return {'data': JSONAPI.parse(Reservacab, [item.to_dict() for item in reservacab])}
	@db_session
	def get_Reservacab_one(self, _id):
		reservacab = Reservacab[_id]
		if reservacab:
			return {'data': reservacab.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Reservadet(self):
		reservadet = Reservadet.select()
		return {'data': JSONAPI.parse(Reservadet, [item.to_dict() for item in reservadet])}
	@db_session
	def get_Reservadet_one(self, _id):
		reservadet = Reservadet[_id]
		if reservadet:
			return {'data': reservadet.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Rutas(self):
		rutas = Rutas.select()
		return {'data': JSONAPI.parse(Rutas, [item.to_dict() for item in rutas])}
	@db_session
	def get_Rutas_one(self, _id):
		rutas = Rutas[_id]
		if rutas:
			return {'data': rutas.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Surtidor(self):
		surtidor = Surtidor.select()
		return {'data': JSONAPI.parse(Surtidor, [item.to_dict() for item in surtidor])}
	@db_session
	def get_Surtidor_one(self, _id):
		surtidor = Surtidor[_id]
		if surtidor:
			return {'data': surtidor.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Tabla01(self):
		tabla01 = Tabla01.select()
		return {'data': JSONAPI.parse(Tabla01, [item.to_dict() for item in tabla01])}
	@db_session
	def get_Tabla01_one(self, _id):
		tabla01 = Tabla01[_id]
		if tabla01:
			return {'data': tabla01.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Tabla02(self):
		tabla02 = Tabla02.select()
		return {'data': JSONAPI.parse(Tabla02, [item.to_dict() for item in tabla02])}
	@db_session
	def get_Tabla02_one(self, _id):
		tabla02 = Tabla02[_id]
		if tabla02:
			return {'data': tabla02.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Tabla05(self):
		tabla05 = Tabla05.select()
		return {'data': JSONAPI.parse(Tabla05, [item.to_dict() for item in tabla05])}
	@db_session
	def get_Tabla05_one(self, _id):
		tabla05 = Tabla05[_id]
		if tabla05:
			return {'data': tabla05.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Tabla06(self):
		tabla06 = Tabla06.select()
		return {'data': JSONAPI.parse(Tabla06, [item.to_dict() for item in tabla06])}
	@db_session
	def get_Tabla06_one(self, _id):
		tabla06 = Tabla06[_id]
		if tabla06:
			return {'data': tabla06.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Tabla10(self):
		tabla10 = Tabla10.select()
		return {'data': JSONAPI.parse(Tabla10, [item.to_dict() for item in tabla10])}
	@db_session
	def get_Tabla10_one(self, _id):
		tabla10 = Tabla10[_id]
		if tabla10:
			return {'data': tabla10.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Tags(self):
		tags = Tags.select()
		return {'data': JSONAPI.parse(Tags, [item.to_dict() for item in tags])}
	@db_session
	def get_Tags_one(self, _id):
		tags = Tags[_id]
		if tags:
			return {'data': tags.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Tallas(self):
		tallas = Tallas.select()
		return {'data': JSONAPI.parse(Tallas, [item.to_dict() for item in tallas])}
	@db_session
	def get_Tallas_one(self, _id):
		tallas = Tallas[_id]
		if tallas:
			return {'data': tallas.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Tareas(self):
		tareas = Tareas.select()
		return {'data': JSONAPI.parse(Tareas, [item.to_dict() for item in tareas])}
	@db_session
	def get_Tareas_one(self, _id):
		tareas = Tareas[_id]
		if tareas:
			return {'data': tareas.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Tempserie(self):
		tempserie = Tempserie.select()
		return {'data': JSONAPI.parse(Tempserie, [item.to_dict() for item in tempserie])}
	@db_session
	def get_Tempserie_one(self, _id):
		tempserie = Tempserie[_id]
		if tempserie:
			return {'data': tempserie.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Tipohabitacion(self):
		tipohabitacion = Tipohabitacion.select()
		return {'data': JSONAPI.parse(Tipohabitacion, [item.to_dict() for item in tipohabitacion])}
	@db_session
	def get_Tipohabitacion_one(self, _id):
		tipohabitacion = Tipohabitacion[_id]
		if tipohabitacion:
			return {'data': tipohabitacion.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Tipomovalmacen(self):
		tipomovalmacen = Tipomovalmacen.select()
		return {'data': JSONAPI.parse(Tipomovalmacen, [item.to_dict() for item in tipomovalmacen])}
	@db_session
	def get_Tipomovalmacen_one(self, _id):
		tipomovalmacen = Tipomovalmacen[_id]
		if tipomovalmacen:
			return {'data': tipomovalmacen.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Tiporeserva(self):
		tiporeserva = Tiporeserva.select()
		return {'data': JSONAPI.parse(Tiporeserva, [item.to_dict() for item in tiporeserva])}
	@db_session
	def get_Tiporeserva_one(self, _id):
		tiporeserva = Tiporeserva[_id]
		if tiporeserva:
			return {'data': tiporeserva.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Tmpsaldos(self):
		tmpsaldos = Tmpsaldos.select()
		return {'data': JSONAPI.parse(Tmpsaldos, [item.to_dict() for item in tmpsaldos])}
	@db_session
	def get_Tmpsaldos_one(self, _id):
		tmpsaldos = Tmpsaldos[_id]
		if tmpsaldos:
			return {'data': tmpsaldos.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Tmptablacompras(self):
		tmptablacompras = Tmptablacompras.select()
		return {'data': JSONAPI.parse(Tmptablacompras, [item.to_dict() for item in tmptablacompras])}
	@db_session
	def get_Tmptablacompras_one(self, _id):
		tmptablacompras = Tmptablacompras[_id]
		if tmptablacompras:
			return {'data': tmptablacompras.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Tmptablaventas(self):
		tmptablaventas = Tmptablaventas.select()
		return {'data': JSONAPI.parse(Tmptablaventas, [item.to_dict() for item in tmptablaventas])}
	@db_session
	def get_Tmptablaventas_one(self, _id):
		tmptablaventas = Tmptablaventas[_id]
		if tmptablaventas:
			return {'data': tmptablaventas.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Transporte(self):
		transporte = Transporte.select()
		return {'data': JSONAPI.parse(Transporte, [item.to_dict() for item in transporte])}
	@db_session
	def get_Transporte_one(self, _id):
		transporte = Transporte[_id]
		if transporte:
			return {'data': transporte.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Turnos(self):
		turnos = Turnos.select()
		return {'data': JSONAPI.parse(Turnos, [item.to_dict() for item in turnos])}
	@db_session
	def get_Turnos_one(self, _id):
		turnos = Turnos[_id]
		if turnos:
			return {'data': turnos.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Ubigeo(self):
		ubigeo = Ubigeo.select()
		return {'data': JSONAPI.parse(Ubigeo, [item.to_dict() for item in ubigeo])}
	@db_session
	def get_Ubigeo_one(self, _id):
		ubigeo = Ubigeo[_id]
		if ubigeo:
			return {'data': ubigeo.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Unidades(self):
		unidades = Unidades.select()
		return {'data': JSONAPI.parse(Unidades, [item.to_dict() for item in unidades])}
	@db_session
	def get_Unidades_one(self, _id):
		unidades = Unidades[_id]
		if unidades:
			return {'data': unidades.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Usuarios(self):
		usuarios = Usuarios.select()
		return {'data': JSONAPI.parse(Usuarios, [item.to_dict() for item in usuarios])}
	@db_session
	def get_Usuarios_one(self, _id):
		usuarios = Usuarios[_id]
		if usuarios:
			return {'data': usuarios.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Vendedor(self):
		vendedor = Vendedor.select()
		return {'data': JSONAPI.parse(Vendedor, [item.to_dict() for item in vendedor])}
	@db_session
	def get_Vendedor_one(self, _id):
		vendedor = Vendedor[_id]
		if vendedor:
			return {'data': vendedor.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Zona(self):
		zona = Zona.select()
		return {'data': JSONAPI.parse(Zona, [item.to_dict() for item in zona])}
	@db_session
	def get_Zona_one(self, _id):
		zona = Zona[_id]
		if zona:
			return {'data': zona.to_dict()}
		return {'data': 'sin data que mostrar'}
	@db_session
	def get_Zonas(self):
		zonas = Zonas.select()
		return {'data': JSONAPI.parse(Zonas, [item.to_dict() for item in zonas])}
	@db_session
	def get_Zonas_one(self, _id):
		zonas = Zonas[_id]
		if zonas:
			return {'data': zonas.to_dict()}
		return {'data': 'sin data que mostrar'}
db = DBAdmin()
