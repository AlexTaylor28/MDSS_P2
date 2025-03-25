from __future__ import annotations
from shlex import join
from typing import TYPE_CHECKING, List

from EstadoLoteProduccion import EnPreparacion
from Exportador import *
from ProductoFinal import ProductoFinal

if TYPE_CHECKING:
	from LotePrima import *
	from EstadoLoteProduccion import *
	from Producto import *

class LoteProduccion():
	
	def __init__(self, producto_destino: Producto):
		self.producto_destino = producto_destino
		self.lotes_prima: List[LotePrima] = []
		self.estado: EstadoLoteProduccion = EnPreparacion(self)
		self.historial_estados: List[EstadoLoteProduccion] = [self.estado]
		self.productos_finales: List[ProductoFinal] = []

	def agregar_lote_prima(self, lote_prima: LotePrima):
		self.estado.agregar_lote(lote_prima)

	def quitar_lote_prima(self, lote_prima: LotePrima):
		self.estado.quitar_lote(lote_prima)

	def cambiar_estado(self, estado: EstadoLoteProduccion):
		self.estado = estado
		self.historial_estados.append(estado)

	def pasar_a_produccion(self):
		self.estado.pasar_a_produccion()

	def finalizar_produccion(self):
		self.estado.finalizar_produccion()

	def registrar_producto_final(self, producto_final: ProductoFinal):
		self.estado.registrar_producto_final(producto_final)

	def mostrar_historial_estados(self):
		print("Historial de estados:")
		for estado in self.historial_estados:
			print(f" * {estado}")

	def exportar(self, exportador: Exportador = ExportadorPDF()):
		exportador.exportar(self)

	def __str__(self):
		ancho_total = 80
		producto_centrado = str(self.producto_destino).center(ancho_total)

		lotes_str = "".join(str(lote) for lote in self.lotes_prima)
		productos_str = "".join(str(producto) for producto in self.productos_finales) 

		return (
			f"{'=' * ancho_total}\n"
			f"{'Lote de Produccion'.center(ancho_total)}\n"
			f"{producto_centrado}\n\n"
			f"{'Lotes de Materia Prima'.center(ancho_total)}\n{lotes_str}\n"
			f"{'Productos Finales'.center(ancho_total)}\n{productos_str}\n"
			f"{'=' * ancho_total}\n"
		)

