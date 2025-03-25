from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from Analizador import Analizador
    from LotePrima import LotePrima

class Producto(ABC):
    
    @abstractmethod
    def analizar_lote_con(self, lote: LotePrima, analizador: Analizador):
        pass

class AceiteDeOliva(Producto):

    def analizar_lote_con(self, lote: LotePrima, analizador: Analizador):
        analizador.analizar_aceite_de_oliva(lote)

    def __str__(self):
        return "AceiteDeOliva"

class OlivaDeMesa(Producto):

    def analizar_lote_con(self, lote: LotePrima, analizador: Analizador):
        analizador.analizar_oliva_de_mesa(lote)

    def __str__(self):
        return "OlivaDeMesa"




