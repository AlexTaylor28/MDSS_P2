from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from datetime import date, datetime

if TYPE_CHECKING:
    from LotePrima import LotePrima, Imagen
    from Productor import Productor
    from Producto import Producto
    from Analizador import Analizador

# -------------------------------------------------------------------------------- #
class EstadoLotePrima(ABC):

    def __init__(self, lote: LotePrima):
        self.lote = lote
        self.fecha_hora = datetime.now()

    def editar(self, productor: Productor, fecha_cosecha: date, fecha_llegada: datetime, peso_bruto: float, peso_tara: float, producto_destino: Producto):
        self._no_permitido("editar")

    def enviar_a_analisis(self):
        self._no_permitido("enviar_a_analisis")

    def finalizar_analisis(self):
        self._no_permitido("finalizar_analisis")

    def volver_a_ingresado(self):
        self._no_permitido("volver_a_ingresado")

    def enviar_a_produccion(self):
        self._no_permitido("enviar_a_produccion")

    def retirar_de_produccion(self):
        self._no_permitido("retirar_de_produccion")

    def registrar_imagen(self, imagen: Imagen):
        self._no_permitido("registrar_imagen")

    def analizar(self, analizador: Analizador):
        self._no_permitido("analizar")

    def _no_permitido(self, metodo: str):
        raise Exception(f"Estado {self.__class__.__name__} no permite: {metodo}()")

    def __str__(self):
        return f"{self.__class__.__name__} - {self.fecha_hora.strftime('%H:%M:%S | %d/%m/%Y')}"

# -------------------------------------------------------------------------------- #

class Ingresado(EstadoLotePrima):

    def editar(self, productor: Productor, fecha_cosecha: date, fecha_llegada: datetime, peso_bruto: float, peso_tara: float, producto_destino: Producto):
        self.lote.productor = productor
        self.lote.fecha_cosecha = fecha_cosecha
        self.lote.fecha_llegada = fecha_llegada
        self.lote.peso_bruto = peso_bruto
        self.lote.peso_tara = peso_tara
        self.lote.producto_destino = producto_destino

    def enviar_a_analisis(self):
        self.lote.cambiar_estado(EnAnalisis(self.lote))

    def registrar_imagen(self, imagen: Imagen):
        self.lote.imagenes.append(imagen)

# -------------------------------------------------------------------------------- #

class EnAnalisis(EstadoLotePrima):

    def finalizar_analisis(self):
        self.lote.cambiar_estado(Analizado(self.lote))

    def volver_a_ingresado(self):
        self.lote.borrar_imagenes()
        self.lote.borrar_analisis()
        self.lote.cambiar_estado(Ingresado(self.lote))

    def analizar(self, analizador: Analizador):
        self.lote.producto_destino.analizar_lote_con(self.lote, analizador)       
        
# -------------------------------------------------------------------------------- #

class Analizado(EstadoLotePrima):
    
    def enviar_a_produccion(self):
        self.lote.cambiar_estado(EnProduccion(self.lote))

# -------------------------------------------------------------------------------- #

class EnProduccion(EstadoLotePrima):

    def retirar_de_produccion(self):
        self.lote.cambiar_estado(Analizado(self.lote))

 # -------------------------------------------------------------------------------- #   