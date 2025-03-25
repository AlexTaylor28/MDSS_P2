from __future__ import annotations
from typing import TYPE_CHECKING, List
from datetime import date, datetime
import random

from EstadoLotePrima import Ingresado

if TYPE_CHECKING:
    from Productor import Productor
    from Producto import Producto
    from EstadoLotePrima import EstadoLotePrima
    from Analizador import Analisis, Analizador

class Imagen:
    pass

class LotePrima:
   
    def generar_codigo():
        return ''.join(random.choices("0123456789", k = 20))

    def __init__(self, productor: Productor, fecha_cosecha: date, fecha_llegada: datetime, peso_bruto: float, peso_tara: float, producto_destino: Producto):    
        self.codigo = LotePrima.generar_codigo()
        self.productor = productor
        self.fecha_cosecha = fecha_cosecha
        self.fecha_llegada = fecha_llegada
        self.peso_bruto = peso_bruto
        self.peso_tara = peso_tara
        self.peso_neto = peso_bruto - peso_tara
        self.producto_destino = producto_destino
        self.estado: EstadoLotePrima = Ingresado(self);
        self.historial_estados: List[EstadoLotePrima] = [self.estado]
        self.imagenes: List[Imagen] = []
        self.analisis: List[Analisis] = []

    def editar(self, productor: Productor, fecha_cosecha: date, fecha_llegada: datetime, peso_bruto: float, peso_tara: float, producto_destino: Producto):
        self.estado.editar(productor, fecha_cosecha, fecha_llegada, peso_bruto, peso_tara, producto_destino)

    def cambiar_estado(self, estado: EstadoLotePrima):
        self.estado = estado
        self.historial_estados.append(estado)

    def enviar_a_analisis(self):
        self.estado.enviar_a_analisis()

    def finalizar_analisis(self):
        self.estado.finalizar_analisis()

    def volver_a_ingresado(self):
        self.estado.volver_a_ingresado()

    def enviar_a_produccion(self):
        self.estado.enviar_a_produccion()

    def retirar_de_produccion(self):
        self.estado.retirar_de_produccion()

    def registrar_imagen(self, imagen: Imagen):
        self.estado.registrar_imagen(imagen)

    def analizar(self, analizador: Analizador):
        self.estado.analizar(analizador)

    def borrar_imagenes(self):
        self.imagenes.clear()

    def borrar_analisis(self):
        self.analisis.clear()

    def mostrar_historial_estados(self):
        print("Historial de estados:")
        for estado in self.historial_estados:
            print(f" * {estado}")

    def __str__(self):
        ancho_total = 80
        return (
            f"{'-' * ancho_total}\n"
            f"{'Codigo:':<20} {self.codigo}\n"
            f"{'Productor:':<20} {self.productor}\n"
            f"{'Fecha Cosecha:':<20} {self.fecha_cosecha}\n"
            f"{'Fecha Llegada:':<20} {self.fecha_llegada.strftime('%H:%M:%S | %d/%m/%Y')}\n"
            f"{'Peso Neto:':<20} {self.peso_neto}\n"
            f"{'-' * ancho_total}\n"
        )

