import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Resource
from flask import request
from flask import jsonify
import time
import json
from app.basedatos import *
from app.gestor import db
class RutaAccesos(Resource):
	@db_session
	def get(self):
		accesos = db.get_Accesos()
		return jsonify(accesos)
class RutaAcompanante(Resource):
	@db_session
	def get(self):
		acompanante = db.get_Acompanante()
		return jsonify(acompanante)
class RutaAgencias(Resource):
	@db_session
	def get(self):
		agencias = db.get_Agencias()
		return jsonify(agencias)
class RutaAlmacen(Resource):
	@db_session
	def get(self):
		almacen = db.get_Almacen()
		return jsonify(almacen)
class RutaAperturas(Resource):
	@db_session
	def get(self):
		aperturas = db.get_Aperturas()
		return jsonify(aperturas)
class RutaAreas(Resource):
	@db_session
	def get(self):
		areas = db.get_Areas()
		return jsonify(areas)
class RutaArticulo(Resource):
	@db_session
	def get(self):
		articulo = db.get_Articulo()
		return jsonify(articulo)
class RutaArticuloproveedor(Resource):
	@db_session
	def get(self):
		articuloproveedor = db.get_Articuloproveedor()
		return jsonify(articuloproveedor)
class RutaArticulotag(Resource):
	@db_session
	def get(self):
		articulotag = db.get_Articulotag()
		return jsonify(articulotag)
class RutaAsistencia(Resource):
	@db_session
	def get(self):
		asistencia = db.get_Asistencia()
		return jsonify(asistencia)
class RutaAuditor(Resource):
	@db_session
	def get(self):
		auditor = db.get_Auditor()
		return jsonify(auditor)
class RutaCajachcab(Resource):
	@db_session
	def get(self):
		cajachcab = db.get_Cajachcab()
		return jsonify(cajachcab)
class RutaCajachdet(Resource):
	@db_session
	def get(self):
		cajachdet = db.get_Cajachdet()
		return jsonify(cajachdet)
class RutaCajadet(Resource):
	@db_session
	def get(self):
		cajadet = db.get_Cajadet()
		return jsonify(cajadet)
class RutaCajagas(Resource):
	@db_session
	def get(self):
		cajagas = db.get_Cajagas()
		return jsonify(cajagas)
class RutaCajamv(Resource):
	@db_session
	def get(self):
		cajamv = db.get_Cajamv()
		return jsonify(cajamv)
class RutaCajati(Resource):
	@db_session
	def get(self):
		cajati = db.get_Cajati()
		return jsonify(cajati)
class RutaCajero(Resource):
	@db_session
	def get(self):
		cajero = db.get_Cajero()
		return jsonify(cajero)
class RutaCajeromv(Resource):
	@db_session
	def get(self):
		cajeromv = db.get_Cajeromv()
		return jsonify(cajeromv)
class RutaCanal(Resource):
	@db_session
	def get(self):
		canal = db.get_Canal()
		return jsonify(canal)
class RutaCargos(Resource):
	@db_session
	def get(self):
		cargos = db.get_Cargos()
		return jsonify(cargos)
class RutaCategoria(Resource):
	@db_session
	def get(self):
		categoria = db.get_Categoria()
		return jsonify(categoria)
class RutaCliempre(Resource):
	@db_session
	def get(self):
		cliempre = db.get_Cliempre()
		return jsonify(cliempre)
class RutaColores(Resource):
	@db_session
	def get(self):
		colores = db.get_Colores()
		return jsonify(colores)
class RutaComentarios(Resource):
	@db_session
	def get(self):
		comentarios = db.get_Comentarios()
		return jsonify(comentarios)
class RutaComisionescab(Resource):
	@db_session
	def get(self):
		comisionescab = db.get_Comisionescab()
		return jsonify(comisionescab)
class RutaComisionesdet(Resource):
	@db_session
	def get(self):
		comisionesdet = db.get_Comisionesdet()
		return jsonify(comisionesdet)
class RutaCompatible(Resource):
	@db_session
	def get(self):
		compatible = db.get_Compatible()
		return jsonify(compatible)
class RutaCompatibles(Resource):
	@db_session
	def get(self):
		compatibles = db.get_Compatibles()
		return jsonify(compatibles)
class RutaCompras(Resource):
	@db_session
	def get(self):
		compras = db.get_Compras()
		return jsonify(compras)
class RutaConcepto(Resource):
	@db_session
	def get(self):
		concepto = db.get_Concepto()
		return jsonify(concepto)
class RutaCondicion(Resource):
	@db_session
	def get(self):
		condicion = db.get_Condicion()
		return jsonify(condicion)
class RutaConsolidadocab(Resource):
	@db_session
	def get(self):
		consolidadocab = db.get_Consolidadocab()
		return jsonify(consolidadocab)
class RutaConsolidadodet(Resource):
	@db_session
	def get(self):
		consolidadodet = db.get_Consolidadodet()
		return jsonify(consolidadodet)
class RutaCorrelativos(Resource):
	@db_session
	def get(self):
		correlativos = db.get_Correlativos()
		return jsonify(correlativos)
class RutaDepartamento(Resource):
	@db_session
	def get(self):
		departamento = db.get_Departamento()
		return jsonify(departamento)
class RutaDias(Resource):
	@db_session
	def get(self):
		dias = db.get_Dias()
		return jsonify(dias)
class RutaDirecciones(Resource):
	@db_session
	def get(self):
		direcciones = db.get_Direcciones()
		return jsonify(direcciones)
class RutaDocumentos(Resource):
	@db_session
	def get(self):
		documentos = db.get_Documentos()
		return jsonify(documentos)
class RutaEmpresas(Resource):
	@db_session
	def get(self):
		empresas = db.get_Empresas()
		return jsonify(empresas)
class RutaEscalas(Resource):
	@db_session
	def get(self):
		escalas = db.get_Escalas()
		return jsonify(escalas)
class RutaExistencia(Resource):
	@db_session
	def get(self):
		existencia = db.get_Existencia()
		return jsonify(existencia)
class RutaFormapago(Resource):
	@db_session
	def get(self):
		formapago = db.get_Formapago()
		return jsonify(formapago)
class RutaHabitacion(Resource):
	@db_session
	def get(self):
		habitacion = db.get_Habitacion()
		return jsonify(habitacion)
class RutaImagenesps(Resource):
	@db_session
	def get(self):
		imagenesps = db.get_Imagenesps()
		return jsonify(imagenesps)
class RutaIniciocab(Resource):
	@db_session
	def get(self):
		iniciocab = db.get_Iniciocab()
		return jsonify(iniciocab)
class RutaIniciodetalle(Resource):
	@db_session
	def get(self):
		iniciodetalle = db.get_Iniciodetalle()
		return jsonify(iniciodetalle)
class RutaKardex(Resource):
	@db_session
	def get(self):
		kardex = db.get_Kardex()
		return jsonify(kardex)
class RutaListaprecios(Resource):
	@db_session
	def get(self):
		listaprecios = db.get_Listaprecios()
		return jsonify(listaprecios)
class RutaLotes(Resource):
	@db_session
	def get(self):
		lotes = db.get_Lotes()
		return jsonify(lotes)
class RutaMarca(Resource):
	@db_session
	def get(self):
		marca = db.get_Marca()
		return jsonify(marca)
class RutaMonedas(Resource):
	@db_session
	def get(self):
		monedas = db.get_Monedas()
		return jsonify(monedas)
class RutaMotivos(Resource):
	@db_session
	def get(self):
		motivos = db.get_Motivos()
		return jsonify(motivos)
class RutaMotivos_caja(Resource):
	@db_session
	def get(self):
		motivos_caja = db.get_Motivos_caja()
		return jsonify(motivos_caja)
class RutaMovimientodet(Resource):
	@db_session
	def get(self):
		movimientodet = db.get_Movimientodet()
		return jsonify(movimientodet)
class RutaMovimientoscab(Resource):
	@db_session
	def get(self):
		movimientoscab = db.get_Movimientoscab()
		return jsonify(movimientoscab)
class RutaMovimientosdet(Resource):
	@db_session
	def get(self):
		movimientosdet = db.get_Movimientosdet()
		return jsonify(movimientosdet)
class RutaNbf_anulado(Resource):
	@db_session
	def get(self):
		nbf_anulado = db.get_Nbf_anulado()
		return jsonify(nbf_anulado)
class RutaNbf_respuesta(Resource):
	@db_session
	def get(self):
		nbf_respuesta = db.get_Nbf_respuesta()
		return jsonify(nbf_respuesta)
class RutaOpercom(Resource):
	@db_session
	def get(self):
		opercom = db.get_Opercom()
		return jsonify(opercom)
class RutaOpergast(Resource):
	@db_session
	def get(self):
		opergast = db.get_Opergast()
		return jsonify(opergast)
class RutaOpermv(Resource):
	@db_session
	def get(self):
		opermv = db.get_Opermv()
		return jsonify(opermv)
class RutaOperpag(Resource):
	@db_session
	def get(self):
		operpag = db.get_Operpag()
		return jsonify(operpag)
class RutaOperti(Resource):
	@db_session
	def get(self):
		operti = db.get_Operti()
		return jsonify(operti)
class RutaPedidos_cab(Resource):
	@db_session
	def get(self):
		pedidos_cab = db.get_Pedidos_cab()
		return jsonify(pedidos_cab)
class RutaPedidos_det(Resource):
	@db_session
	def get(self):
		pedidos_det = db.get_Pedidos_det()
		return jsonify(pedidos_det)
class RutaPeriodo(Resource):
	@db_session
	def get(self):
		periodo = db.get_Periodo()
		return jsonify(periodo)
class RutaPersonal(Resource):
	@db_session
	def get(self):
		personal = db.get_Personal()
		return jsonify(personal)
class RutaPlanilla_cab(Resource):
	@db_session
	def get(self):
		planilla_cab = db.get_Planilla_cab()
		return jsonify(planilla_cab)
class RutaPlanilla_det(Resource):
	@db_session
	def get(self):
		planilla_det = db.get_Planilla_det()
		return jsonify(planilla_det)
class RutaPremisoprecio(Resource):
	@db_session
	def get(self):
		premisoprecio = db.get_Premisoprecio()
		return jsonify(premisoprecio)
class RutaPrestamocab(Resource):
	@db_session
	def get(self):
		prestamocab = db.get_Prestamocab()
		return jsonify(prestamocab)
class RutaPrestamodet(Resource):
	@db_session
	def get(self):
		prestamodet = db.get_Prestamodet()
		return jsonify(prestamodet)
class RutaPrimercosteo(Resource):
	@db_session
	def get(self):
		primercosteo = db.get_Primercosteo()
		return jsonify(primercosteo)
class RutaProcedencia(Resource):
	@db_session
	def get(self):
		procedencia = db.get_Procedencia()
		return jsonify(procedencia)
class RutaProdtallacolor(Resource):
	@db_session
	def get(self):
		prodtallacolor = db.get_Prodtallacolor()
		return jsonify(prodtallacolor)
class RutaProductofoto(Resource):
	@db_session
	def get(self):
		productofoto = db.get_Productofoto()
		return jsonify(productofoto)
class RutaProfesion(Resource):
	@db_session
	def get(self):
		profesion = db.get_Profesion()
		return jsonify(profesion)
class RutaPromocab(Resource):
	@db_session
	def get(self):
		promocab = db.get_Promocab()
		return jsonify(promocab)
class RutaPromodet(Resource):
	@db_session
	def get(self):
		promodet = db.get_Promodet()
		return jsonify(promodet)
class RutaProveedores(Resource):
	@db_session
	def get(self):
		proveedores = db.get_Proveedores()
		return jsonify(proveedores)
class RutaProvincia(Resource):
	@db_session
	def get(self):
		provincia = db.get_Provincia()
		return jsonify(provincia)
class RutaRegion(Resource):
	@db_session
	def get(self):
		region = db.get_Region()
		return jsonify(region)
class RutaReservacab(Resource):
	@db_session
	def get(self):
		reservacab = db.get_Reservacab()
		return jsonify(reservacab)
class RutaReservadet(Resource):
	@db_session
	def get(self):
		reservadet = db.get_Reservadet()
		return jsonify(reservadet)
class RutaRutas(Resource):
	@db_session
	def get(self):
		rutas = db.get_Rutas()
		return jsonify(rutas)
class RutaSurtidor(Resource):
	@db_session
	def get(self):
		surtidor = db.get_Surtidor()
		return jsonify(surtidor)
class RutaTabla01(Resource):
	@db_session
	def get(self):
		tabla01 = db.get_Tabla01()
		return jsonify(tabla01)
class RutaTabla02(Resource):
	@db_session
	def get(self):
		tabla02 = db.get_Tabla02()
		return jsonify(tabla02)
class RutaTabla05(Resource):
	@db_session
	def get(self):
		tabla05 = db.get_Tabla05()
		return jsonify(tabla05)
class RutaTabla06(Resource):
	@db_session
	def get(self):
		tabla06 = db.get_Tabla06()
		return jsonify(tabla06)
class RutaTabla10(Resource):
	@db_session
	def get(self):
		tabla10 = db.get_Tabla10()
		return jsonify(tabla10)
class RutaTags(Resource):
	@db_session
	def get(self):
		tags = db.get_Tags()
		return jsonify(tags)
class RutaTallas(Resource):
	@db_session
	def get(self):
		tallas = db.get_Tallas()
		return jsonify(tallas)
class RutaTareas(Resource):
	@db_session
	def get(self):
		tareas = db.get_Tareas()
		return jsonify(tareas)
class RutaTempserie(Resource):
	@db_session
	def get(self):
		tempserie = db.get_Tempserie()
		return jsonify(tempserie)
class RutaTipohabitacion(Resource):
	@db_session
	def get(self):
		tipohabitacion = db.get_Tipohabitacion()
		return jsonify(tipohabitacion)
class RutaTipomovalmacen(Resource):
	@db_session
	def get(self):
		tipomovalmacen = db.get_Tipomovalmacen()
		return jsonify(tipomovalmacen)
class RutaTiporeserva(Resource):
	@db_session
	def get(self):
		tiporeserva = db.get_Tiporeserva()
		return jsonify(tiporeserva)
class RutaTmpsaldos(Resource):
	@db_session
	def get(self):
		tmpsaldos = db.get_Tmpsaldos()
		return jsonify(tmpsaldos)
class RutaTmptablacompras(Resource):
	@db_session
	def get(self):
		tmptablacompras = db.get_Tmptablacompras()
		return jsonify(tmptablacompras)
class RutaTmptablaventas(Resource):
	@db_session
	def get(self):
		tmptablaventas = db.get_Tmptablaventas()
		return jsonify(tmptablaventas)
class RutaTransporte(Resource):
	@db_session
	def get(self):
		transporte = db.get_Transporte()
		return jsonify(transporte)
class RutaTurnos(Resource):
	@db_session
	def get(self):
		turnos = db.get_Turnos()
		return jsonify(turnos)
class RutaUbigeo(Resource):
	@db_session
	def get(self):
		ubigeo = db.get_Ubigeo()
		return jsonify(ubigeo)
class RutaUnidades(Resource):
	@db_session
	def get(self):
		unidades = db.get_Unidades()
		return jsonify(unidades)
class RutaUsuarios(Resource):
	@db_session
	def get(self):
		usuarios = db.get_Usuarios()
		return jsonify(usuarios)
class RutaVendedor(Resource):
	@db_session
	def get(self):
		vendedor = db.get_Vendedor()
		return jsonify(vendedor)
class RutaZona(Resource):
	@db_session
	def get(self):
		zona = db.get_Zona()
		return jsonify(zona)
class RutaZonas(Resource):
	@db_session
	def get(self):
		zonas = db.get_Zonas()
		return jsonify(zonas)
