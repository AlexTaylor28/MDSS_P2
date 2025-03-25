from __future__ import annotations
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from LotePrima import *
    from EstadoLotePrima import *
    from LoteProduccion import *

class GestorLotes:

    def __init__(self):
        self.lotes_prima: List[LotePrima] = []
        self.lotes_produccion: List[LoteProduccion] = []

    def ingresar_lote_prima(self, lote_prima: LotePrima):
        self.lotes_prima.append(lote_prima)

    def ingresar_lote_produccion(self, lote_produccion: LoteProduccion):
        self.lotes_produccion.append(lote_produccion)

    def asignar_lote_prima_a_produccion(self, lote_prima: LotePrima, lote_produccion: LoteProduccion):
        self._validar_asignacion(lote_prima, lote_produccion)
        lote_produccion.agregar_lote_prima(lote_prima)
        lote_prima.enviar_a_produccion()

    def desasignar_lote_prima_de_produccion(self, lote_prima: LotePrima, lote_produccion: LoteProduccion):
        self._validar_desasignacion(lote_prima, lote_produccion)
        lote_produccion.quitar_lote_prima(lote_prima)
        lote_prima.retirar_de_produccion()

    def _validar_asignacion(self, lote_prima: LotePrima, lote_produccion: LoteProduccion):
        self._verificar_lotes_registrados(lote_prima, lote_produccion)

        if lote_prima in lote_produccion.lotes_prima:
            raise ValueError("LotePrima ya esta asignado a este LoteProduccion.")

        if type(lote_produccion.producto_destino) != type(lote_prima.producto_destino):
            raise ValueError("Producto destino no coincide")

    def _validar_desasignacion(self, lote_prima: LotePrima, lote_produccion: LoteProduccion):
        self._verificar_lotes_registrados(lote_prima, lote_produccion)

        if lote_prima not in lote_produccion.lotes_prima:
            raise ValueError("LotePrima no esta asignado a este LoteProduccion.")

    def _verificar_lotes_registrados(self, lote_prima: LotePrima, lote_produccion: LoteProduccion):
        if lote_prima not in self.lotes_prima:
            raise ValueError("LotePrima no registrado en el GestorLotes.")
        if lote_produccion not in self.lotes_produccion:
            raise ValueError("LoteProduccion no registrado en el GestorLotes.")





