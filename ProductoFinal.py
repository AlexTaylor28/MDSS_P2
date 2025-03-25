from __future__ import annotations
from typing import TYPE_CHECKING, List, Tuple

import random

if TYPE_CHECKING:
    from Enumeradores import *
    from EstrategiaCalidad import *

# ----------------------------------------------------------------------------------------------------------- #

class ProductoFinal:

    def generar_codigo():
        return ''.join(random.choices("0123456789", k = 20))

    def __init__(self, cantidad: float, unidades: Unidades, lugar_almacenaje: str, estrategia_calidad: EstrategiaCalidad):
        self.codigo = ProductoFinal.generar_codigo()
        self.cantidad = cantidad
        self.unidades = unidades
        self.lugar_almacenaje = lugar_almacenaje
        self.estrategia_calidad: EstrategiaCalidad = estrategia_calidad

    def cambiar_estrategia_calidad(self, estrategia_calidad: EstrategiaCalidad):
        self.estrategia_calidad = estrategia_calidad

    def calcular_calidad(self):
        return self.estrategia_calidad.calcular_calidad(self)

    def __str__(self):
        ancho_total = 80
        return (
            f"{'-' * ancho_total}\n"
            f"{'Codigo:':<20} {self.codigo}\n"
            f"{'Cantidad:':<20} {self.cantidad}\n"
            f"{'Lugar Almacenaje:':<20} {self.lugar_almacenaje}\n"
            f"{'Calidad:':<20} {self.calcular_calidad()}\n"
            f"{'-' * ancho_total}\n"
        )

# ----------------------------------------------------------------------------------------------------------- #

class AceiteDeOlivaProductoFinal(ProductoFinal):

    def __init__(self, 
                 cantidad: float,
                 unidades: Unidades,
                 lugar_almacenaje: str,
                 estrategia_calidad: EstrategiaCalidad,
                 metodo_extraccion: MetodoExtraccion,
                 acidez: float,
                 cantidad_polifenoles: int,
                 color: str,
                 defectos_sensoriales: List[Tuple[str, GravedadDefecto]],
                 perfil_frutado: str,
                 nivel_frutado: NivelFrutado,
                 resistencia_termica: ResistenciaTermica = None
                 ):
        super().__init__(cantidad, unidades, lugar_almacenaje, estrategia_calidad)        
        self.metodo_extraccion = metodo_extraccion
        self.acidez = acidez
        self.cantidad_polifenoles = cantidad_polifenoles
        self.color = color
        self.defectos_sensoriales = defectos_sensoriales
        self.perfil_frutado = perfil_frutado
        self.nivel_frutado = nivel_frutado
        self.resistencia_termica = resistencia_termica

# ----------------------------------------------------------------------------------------------------------- #
    
class OlivasDeMesaProductoFinal(ProductoFinal):

    def __init__(self,
                 cantidad: float,
                 unidades: Unidades,
                 lugar_almacenaje: str,
                 estrategia_calidad: EstrategiaCalidad,
                 uniformidad_color: UniformidadColor,
                 tamano_promedio: float,
                 desvio_estandar: float,
                 perfil_sabor: PerfilSabor,
                 proceso_curado: ProcesoCurado,
                 contenido_sal: float,
                 defectos_visuales: float,
                 ph: float
                 ):
        super().__init__(cantidad, unidades, lugar_almacenaje, estrategia_calidad)     
        self.uniformidad_color = uniformidad_color
        self.tamano_promedio = tamano_promedio
        self.desvio_estandar = desvio_estandar
        self.perfil_sabor = perfil_sabor
        self.proceso_curado = proceso_curado
        self.contenido_sal = contenido_sal
        self.defectos_visuales = defectos_visuales
        self.ph = ph

# ----------------------------------------------------------------------------------------------------------- #

