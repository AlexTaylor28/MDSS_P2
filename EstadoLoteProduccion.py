from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from datetime import datetime

if TYPE_CHECKING:
    from LotePrima import LotePrima
    from LoteProduccion import LoteProduccion
    from ProductoFinal import ProductoFinal

# -------------------------------------------------------------------------------- #
class EstadoLoteProduccion(ABC):

    def __init__(self, lote_produccion: LoteProduccion):
        self.lote_produccion = lote_produccion
        self.fecha_hora = datetime.now()

    def agregar_lote(self, lote_prima: LotePrima):
          self._no_permitido("agregar_lote")

    def quitar_lote(self, lote_prima: LotePrima):
        self._no_permitido("quitar_lote")

    def pasar_a_produccion(self):
        self._no_permitido("pasar_a_produccion")

    def finalizar_produccion(self):
        self._no_permitido("finalizar_produccion")

    def registrar_producto_final(self, producto_final: ProductoFinal):
        self._no_permitido("registrar_producto_final")

    def _no_permitido(self, metodo: str):
        raise Exception(f"Estado {self.__class__.__name__} no permite: {metodo}()")

    def __str__(self):
        return f"{self.__class__.__name__} - {self.fecha_hora.strftime('%H:%M:%S | %d/%m/%Y')}"

# -------------------------------------------------------------------------------- #

class EnPreparacion(EstadoLoteProduccion):

    def agregar_lote(self, lote_prima: LotePrima):
        self.lote_produccion.lotes_prima.append(lote_prima)

    def quitar_lote(self, lote_prima: LotePrima):
        self.lote_produccion.lotes_prima.remove(lote_prima)

    def pasar_a_produccion(self):
        self.lote_produccion.cambiar_estado(EnProduccion(self.lote_produccion))

# -------------------------------------------------------------------------------- #

class EnProduccion(EstadoLoteProduccion):

    def finalizar_produccion(self):
        self.lote_produccion.cambiar_estado(Finalizado(self.lote_produccion))

# -------------------------------------------------------------------------------- #

class Finalizado(EstadoLoteProduccion):

    def registrar_producto_final(self, producto_final: ProductoFinal):
        self.lote_produccion.productos_finales.append(producto_final)
