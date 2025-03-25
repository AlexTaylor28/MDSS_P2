from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING, List
import random
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from LotePrima import LotePrima

# ---------------------------------------- #

class Resultado:
    
    def __init__(self, nombre: str, valor):
        self.nombre = nombre
        self.valor = valor

    def __str__(self):
        return ''.join(f"{self.nombre}\t: {self.valor}")

# ---------------------------------------- #

class Analisis:

    def __init__(self, nombre: str, fecha_hora: datetime):
        self.nombre = nombre
        self.fecha_hora = fecha_hora
        self.resultados: List[Resultado] = []

    def registrar_resultado(self, resultado):
        self.resultados.append(resultado)

    def __str__(self):
        print(self.fecha_hora.strftime("%H:%M:%S | %d-%m-%Y"))
        print(self.nombre)
        return '\n'.join(f"{r}" for r in self.resultados)
       
# ---------------------------------------- #

class Analizador(ABC):
    
    @abstractmethod
    def analizar_aceite_de_oliva(self, lote: LotePrima):
        pass

    @abstractmethod
    def analizar_oliva_de_mesa(self, lote: LotePrima):
        pass

# ---------------------------------------- #

class AnalizadorMadurez(Analizador):

    def analizar_aceite_de_oliva(self, lote: LotePrima):    
        analisis = Analisis("Aceite De Oliva - Analisis Madurez", datetime.now())
        analisis.registrar_resultado(Resultado("nivel_madurez", random.randint(0, 100)))
        analisis.registrar_resultado(Resultado("acido_oleico", round(random.uniform(0.0, 100.0), 1)))
        analisis.registrar_resultado(Resultado("indice_grasa", round(random.uniform(0.0, 100.0), 1)))
        lote.analisis.append(analisis)

    def analizar_oliva_de_mesa(self, lote: LotePrima):
        analisis = Analisis("Oliva De Mesa - Analisis Madurez", datetime.now())
        analisis.registrar_resultado(Resultado("estado_madurez", random.choice(["verde", "envero", "negro"])))
        analisis.registrar_resultado(Resultado("firmeza_piel", round(random.uniform(0.0, 10.0), 1)))
        lote.analisis.append(analisis)

# ---------------------------------------- #

class AnalizadorDefectos(Analizador):

    def analizar_aceite_de_oliva(self, lote: LotePrima):
        analisis = Analisis("Aceite De Oliva - Analisis Defectos", datetime.now())
        analisis.registrar_resultado(Resultado("hongos_detectados", random.choice([True, False])))
        analisis.registrar_resultado(Resultado("fermentacion_anomala", random.choice([True, False])))
        analisis.registrar_resultado(Resultado("danos_fisicos", random.choice(["leve", "moderado", "severo"])))
        lote.analisis.append(analisis)
    
    def analizar_oliva_de_mesa(self, lote: LotePrima):
        analisis = Analisis("Oliva De Mesa - Analisis Defectos", datetime.now())
        analisis.registrar_resultado(Resultado("golpes", random.randint(0, 100)))
        analisis.registrar_resultado(Resultado("arrugas", random.randint(0, 100)))
        analisis.registrar_resultado(Resultado("presencia_insectos", random.choice([True, False])))
        analisis.registrar_resultado(Resultado("pudricion", random.choice(["nulo", "leve", "moderado", "severo"])))
        lote.analisis.append(analisis)

# ---------------------------------------- #

class AnalizadorHumedad(Analizador):

    def analizar_aceite_de_oliva(self, lote: LotePrima):
        analisis = Analisis("Aceite De Oliva - Analisis Humedad", datetime.now())
        analisis.registrar_resultado(Resultado("porcentaje_humedad", round(random.uniform(0.0, 100.0), 1)))
        lote.analisis.append(analisis)
    
    def analizar_oliva_de_mesa(self, lote: LotePrima):
        analisis = Analisis("Oliva De Mesa - Analisis Humedad", datetime.now())
        analisis.registrar_resultado(Resultado("porcentaje_humedad", round(random.uniform(0.0, 100.0), 1)))
        analisis.registrar_resultado(Resultado("riesgo_moho", random.choice(["bajo", "medio", "alto"])))
        analisis.registrar_resultado(Resultado("idoneidad_conservacion", random.choice(["mala", "regular", "buena", "excelente"])))
        lote.analisis.append(analisis)

# ---------------------------------------- #

class AnalizadorColor(Analizador):

    def analizar_aceite_de_oliva(self, lote: LotePrima):
        analisis = Analisis("Aceite De Oliva - Analisis Color", datetime.now())
        analisis.registrar_resultado(Resultado("color_preponderante", random.choice(["verde claro", "verde oscuro", "negro"])))
        analisis.registrar_resultado(Resultado("indice_color_esperado", random.choice(["verde-amarillo", "amarillo-dorado", "ámbar"])))
        analisis.registrar_resultado(Resultado("transparencia", random.choice(["baja", "media", "alta"])))
        lote.analisis.append(analisis)
    
    def analizar_oliva_de_mesa(self, lote: LotePrima):
        analisis = Analisis("Oliva De Mesa - Analisis Color", datetime.now())
        analisis.registrar_resultado(Resultado("clasificacion_color", {
            "verde claro": round(random.uniform(0.0, 100.0), 1),
            "verde oscuro": round(random.uniform(0.0, 100.0), 1),
            "negro": round(random.uniform(0.0, 100.0), 1),
        }))
        analisis.registrar_resultado(Resultado("uniformidad_color", round(random.uniform(0.0, 100.0), 1)))
        lote.analisis.append(analisis)

# ---------------------------------------- #

class AnalizadorTamaño(Analizador):

    def analizar_aceite_de_oliva(self, lote: LotePrima):
        analisis = Analisis("Aceite De Oliva - Analisis Tamaño", datetime.now())
        analisis.registrar_resultado(Resultado("tamano_promedio", round(random.uniform(0.0, 30.0), 1)))
        analisis.registrar_resultado(Resultado("frutos_fuera_estandar", round(random.uniform(0.0, 100.0), 1)))
        lote.analisis.append(analisis)
    
    def analizar_oliva_de_mesa(self, lote: LotePrima):
        analisis = Analisis("Oliva De Mesa - Analisis Tamaño", datetime.now())
        analisis.registrar_resultado(Resultado("clasificacion_calibre", random.choice(["chico", "mediano", "grande"])))
        analisis.registrar_resultado(Resultado("frutos_fuera_estandar", round(random.uniform(0.0, 100.0), 1)))
        lote.analisis.append(analisis)

# ---------------------------------------- #

class AnalizadorVariedad(Analizador):
    
    def analizar_aceite_de_oliva(self, lote: LotePrima):
        self.analizar(lote)

    def analizar_oliva_de_mesa(self, lote: LotePrima):
        self.analizar(lote)

    def analizar(self, lote: LotePrima):
        analisis = Analisis("Analisis Variedad", datetime.now())
        variedades = ["Arbequina", "Picual", "Hojiblanca", "Cornicabra", "Manzanilla"]
        distribucion = [{"variedad": v, "porcentaje": round(random.uniform(0.0, 100.0), 1)} for v in random.sample(variedades, random.randint(1, len(variedades)))]  # NO SUMA A 100%!!
        analisis.registrar_resultado(Resultado("distribucion_variedades", distribucion))
        lote.analisis.append(analisis)

