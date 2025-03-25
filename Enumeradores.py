from enum import Enum

class Unidades(Enum):
    KILOGRAMOS = 1
    LITROS = 2

class GravedadDefecto(Enum):
    LEVE = 1
    NORMAL = 2
    GRAVE = 2

class MetodoExtraccion(Enum):
    PRENSADO_EN_FRIO = 1
    CENTRIFUGADO = 2
    REFINADO_ALTA_CALIDAD = 3
    REFINADO_ESTANDAR = 4
    CON_DISOLVENTES = 5

class NivelFrutado(Enum):
    ALTO = 1
    MEDIO = 2
    BAJO = 3

class ResistenciaTermica(Enum):
    MUY_ESTABLE = 1
    ESTABLE = 2
    INESTABLE = 3

class UniformidadColor(Enum):
    ALTO = 1
    MEDIO = 2
    BAJO = 3

class PerfilSabor(Enum):
    AMARGO = 1
    SALADO = 2
    ACIDO = 3

class ProcesoCurado(Enum):
    NATURAL = 1
    SALMUERA = 2
    SOSA_CAUSTICA = 3
    FERMENTACION = 4