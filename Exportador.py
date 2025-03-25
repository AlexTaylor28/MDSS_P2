from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
import json

if TYPE_CHECKING:
    from LoteProduccion import LoteProduccion
    from ProductoFinal import ProductoFinal

class Exportador(ABC):

    @abstractmethod    
    def exportar(self, lote_produccion: LoteProduccion):
        pass

class ExportadorJSON(Exportador):

    def exportar(self, lote_produccion: LoteProduccion):
        print("Exportando JSON...")
        datos = {
            "lotes_prima": [
                {
                    "codigo": lote_prima.codigo,
                    "productor": str(lote_prima.productor),
                    "fecha_cosecha": lote_prima.fecha_cosecha.strftime('%d/%m/%Y'),
                    "fecha_llegada": lote_prima.fecha_llegada.strftime('%H:%M:%S | %d/%m/%Y'),
                    "peso_neto": lote_prima.peso_neto
                } for lote_prima in lote_produccion.lotes_prima
            ],
            "productos_finales": [
                {
                    "codigo": producto.codigo,
                    "cantidad": producto.cantidad,
                    "unidades": str(producto.unidades),
                    "lugar_almacenaje": producto.lugar_almacenaje,
                    "calidad": producto.calcular_calidad()
                } for producto in lote_produccion.productos_finales
            ]
        }
        
        with open("reporte.json", "w", encoding = "utf-8") as f:
            json.dump(datos, f, indent = 4, ensure_ascii = False)

class ExportadorPDF(Exportador):

    def exportar(self, lote_produccion: LoteProduccion):
        print("Exportando PDF...")

class ExportadorCSV(Exportador):

    def exportar(self, lote_produccion: LoteProduccion):
        print("Exportando CSV...")

class ExportadorXSLS(Exportador):

    def exportar(self, lote_produccion: LoteProduccion):
        print("Exportando XLS...")