from __future__ import annotations
from typing import TYPE_CHECKING, List, Tuple
from abc import ABC, abstractmethod

from Enumeradores import *

if TYPE_CHECKING:
    from ProductoFinal import ProductoFinal, AceiteDeOlivaProductoFinal, OlivasDeMesaProductoFinal
    from Enumeradores import *

# ----------------------------------------------------------------------------------------------------------- #

class EstrategiaCalidad(ABC):

    def evaluar_puntuacion(self, puntuacion: int) -> str:
        if puntuacion > 8:
            return "ALTA"
        if puntuacion > 4:
            return "MEDIA"
        return "BAJA"

    @abstractmethod
    def calcular_calidad(self, producto: ProductoFinal) -> str:
        pass

# ----------------------------------------------------------------------------------------------------------- #

class EstrategiaCalidadAceite(EstrategiaCalidad):

    def calcular_calidad(self, producto: AceiteDeOlivaProductoFinal) -> str:
        puntuacion = 0
        puntuacion += self.calcular_acidez(producto.acidez)
        puntuacion += self.calcular_metodo_extraccion(producto.metodo_extraccion)
        puntuacion += self.calcular_defectos_sensoriales(producto.defectos_sensoriales)
        puntuacion += self.calcular_polifenoles(producto.cantidad_polifenoles)
        puntuacion += self.calcular_caracteristicas_extras(producto)
        return self.evaluar_puntuacion(puntuacion)
    
    @abstractmethod
    def calcular_acidez(self, acidez: float) -> int:
        pass

    @abstractmethod
    def calcular_metodo_extraccion(self, metodo_extraccion: MetodoExtraccion) -> int:
        pass

    @abstractmethod
    def calcular_defectos_sensoriales(self, defectos_sensoriales: List[Tuple[str, GravedadDefecto]]) -> int:
        pass

    @abstractmethod
    def calcular_polifenoles(self, cantidad_polifenoles: int) -> int:
        pass

    @abstractmethod
    def calcular_caracteristicas_extras(self, producto: AceiteDeOlivaProductoFinal) -> int:
        pass

# ----------------------------------------------------------------------------------------------------------- #

class EstrategiaCalidadAceiteVirgenExtra(EstrategiaCalidadAceite):
       
    def calcular_acidez(self, acidez: float) -> int:
        if acidez <= 0.3:
            return 2
        if acidez <= 0.8:
            return 1
        return 0

    def calcular_metodo_extraccion(self, metodo_extraccion: MetodoExtraccion) -> int:
        if metodo_extraccion == MetodoExtraccion.PRENSADO_EN_FRIO:
            return 2
        if metodo_extraccion == MetodoExtraccion.CENTRIFUGADO:
            return 1
        return 0

    def calcular_defectos_sensoriales(self, defectos_sensoriales: List[Tuple[str, GravedadDefecto]]) -> int:
        defectos = len(defectos_sensoriales)
        defectos_leves = 0

        for _, gravedad in defectos_sensoriales:
            if gravedad == GravedadDefecto.LEVE:
                defectos_leves += 1

        if defectos == 0:
            return 2
        if defectos_leves == 1 and defectos == 1:
            return 1
        return 0

    def calcular_polifenoles(self, cantidad_polifenoles: int) -> int:
        if cantidad_polifenoles >= 300:
            return 2
        if cantidad_polifenoles >= 200:
            return 1
        return 0

    def calcular_caracteristicas_extras(self, producto: AceiteDeOlivaProductoFinal) -> int:
        if producto.nivel_frutado == NivelFrutado.ALTO:
            return 2
        if producto.nivel_frutado == NivelFrutado.MEDIO:
            return 1
        return 0

# ----------------------------------------------------------------------------------------------------------- #

class EstrategiaCalidadAceiteVirgen(EstrategiaCalidadAceite):

    def calcular_acidez(self, acidez: float) -> int:
        if acidez <= 1.0:
            return 2
        if acidez <= 2.0:
            return 1
        return 0

    def calcular_metodo_extraccion(self, metodo_extraccion: MetodoExtraccion) -> int:
        if metodo_extraccion == MetodoExtraccion.PRENSADO_EN_FRIO:
            return 2
        if metodo_extraccion == MetodoExtraccion.CENTRIFUGADO:
            return 1
        return 0

    def calcular_defectos_sensoriales(self, defectos_sensoriales) -> int:
        defectos = len(defectos_sensoriales)
        defectos_leves = 0
        defectos_normales = 0

        for _, gravedad in defectos_sensoriales:    
            if gravedad == GravedadDefecto.LEVE:
                defectos_leves += 1
            if gravedad == GravedadDefecto.NORMAL:
                defectos_normales += 1

        if defectos_leves <= 1 and defectos_normales == 0:
            return 2
        if defectos == 2:
            return 1
        return 0

    def calcular_polifenoles(self, cantidad_polifenoles: int) -> int:
        if cantidad_polifenoles >= 200:
            return 2
        if cantidad_polifenoles >= 100:
            return 1
        return 0

    def calcular_caracteristicas_extras(self, producto: AceiteDeOlivaProductoFinal) -> int:
        if producto.nivel_frutado in (NivelFrutado.ALTO, NivelFrutado.MEDIO):
            return 2
        if producto.nivel_frutado == NivelFrutado.BAJO:
            return 1
        return 0

# ----------------------------------------------------------------------------------------------------------- #

class EstrategiaCalidadAceiteOrujo(EstrategiaCalidadAceite):
    
    def calcular_acidez(self, acidez: float) -> int:
        if acidez <= 0.3:
            return 2
        if acidez < 0.6:
            return 1
        return 0

    def calcular_metodo_extraccion(self, metodo_extraccion) -> int:
        if metodo_extraccion == MetodoExtraccion.REFINADO_ALTA_CALIDAD:
            return 2
        if metodo_extraccion == MetodoExtraccion.REFINADO_ESTANDAR:
            return 1
        return 0

    def calcular_defectos_sensoriales(self, defectos_sensoriales: List[Tuple[str, GravedadDefecto]]) -> int:
        defectos = len(defectos_sensoriales)
        defectos_leves = 0
        defectos_normales = 0

        for _, gravedad in defectos_sensoriales:    
            if gravedad == GravedadDefecto.LEVE:
                defectos_leves += 1
            if gravedad == GravedadDefecto.NORMAL:
                defectos_normales += 1

        if defectos_normales > 0:
            return 0
        if defectos_leves <= 2:
            return 2
        if defectos_leves <= 3:
            return 1
        return 0

    def calcular_polifenoles(self, cantidad_polifenoles: int) -> int:
        if cantidad_polifenoles >= 100:
            return 2
        if cantidad_polifenoles >= 50:
            return 1
        return 0

    def calcular_caracteristicas_extras(self, producto: AceiteDeOlivaProductoFinal) -> int:
        if producto.resistencia_termica == ResistenciaTermica.MUY_ESTABLE:
            return 2
        if producto.resistencia_termica == ResistenciaTermica.ESTABLE:
            return 1
        return 0

# ----------------------------------------------------------------------------------------------------------- #

class EstrategiaCalidadOlivas(EstrategiaCalidad):

    def calcular_calidad(self, producto: OlivasDeMesaProductoFinal) -> str:
        puntuacion = 0
        puntuacion += self.calcular_uniformidad_color(producto.uniformidad_color)
        puntuacion += self.calcular_tamano(producto.tamano_promedio, producto.desvio_tamano_promedio)
        puntuacion += self.calcular_contenido_sal(producto.contenido_sal)
        puntuacion += self.calcular_defectos_visuales(producto.defectos_visuales)
        puntuacion += self.calcular_ph(producto.ph)
        return self.evaluar_puntuacion(puntuacion)
    
    def calcular_uniformidad_color(self, uniformidad_color: UniformidadColor) -> int:
        if uniformidad_color == UniformidadColor.ALTO:
            return 2
        if uniformidad_color == UniformidadColor.MEDIO:
            return 1
        return 0

    def calcular_tamano(self, tamano_promedio: float, desviacion_estandar: float) -> int:
        if desviacion_estandar < tamano_promedio /10:
            return 2
        if desviacion_estandar < tamano_promedio /20:
            return 1
        return 0

    def calcular_contenido_sal(self, contenido_sal: float) -> int:
        if 5.5 < contenido_sal < 6.5:
            return 2
        if 4.5 < contenido_sal < 7.0:
            return 1
        return 0

    def calcular_defectos_visuales(self, defectos_visuales: float) -> int:
        if defectos_visuales < 5.0:
            return 2
        if defectos_visuales < 15.0:
            return 1
        return 0

    def calcular_ph(self, ph: float) -> int:
        if ph > 3.9 and ph < 4.1:
            return 2
        if ph > 3.7 and ph < 4.3:
            return 1
        return 0