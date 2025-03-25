from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date, datetime

from Analizador import *
from EstadoLotePrima import *
from Exportador import *
from LotePrima import *
from Producto import *
from Productor import *
from LoteProduccion import *
from GestorLotes import *
from EstadoLoteProduccion import *
from Enumeradores import *
from EstrategiaCalidad import *
from ProductoFinal import *

gestor = GestorLotes()

productor1 = Productor("Alejandro", "Taylor Sanjuan", "75924241E", "-", "1", "A@A")
productor2 = Productor("Pepe", "Ruiz", "15334257N", "-", "1", "A@A")

l1 = LotePrima(productor1, date.today(), datetime.now(), 20, 10, AceiteDeOliva())
l2 = LotePrima(productor2, date.today(), datetime.now(), 200, 10, AceiteDeOliva())

l1.enviar_a_analisis()
l1.finalizar_analisis()

l2.enviar_a_analisis()
l2.finalizar_analisis()



lp1 = LoteProduccion(AceiteDeOliva())

gestor.ingresar_lote_prima(l1)
gestor.ingresar_lote_prima(l2)
gestor.ingresar_lote_produccion(lp1)

gestor.asignar_lote_prima_a_produccion(l1, lp1)
gestor.asignar_lote_prima_a_produccion(l2, lp1)

# print(l1)
# l1.avanzar()
# l1.analizar(a1)
# l1.analizar(a2)
# l1.analizar(a3)

# for a in l1.analisis:
#     print(f"{a}\n")

# l1.mostrar_historial_estados()

lp1.pasar_a_produccion()
lp1.finalizar_produccion()

pfinal1 = AceiteDeOlivaProductoFinal(
    cantidad = 10.0,
    unidades = Unidades.LITROS,
    lugar_almacenaje = "Almacen 1",
    estrategia_calidad = EstrategiaCalidadAceiteVirgenExtra(),
    metodo_extraccion = MetodoExtraccion.PRENSADO_EN_FRIO,
    acidez = 0.2 ,
    cantidad_polifenoles = 350,
    color = "Verde",
    defectos_sensoriales = [("Amargo", GravedadDefecto.LEVE)],
    perfil_frutado = "",
    nivel_frutado = NivelFrutado.ALTO
)

lp1.registrar_producto_final(pfinal1)

#print(lp1)

lp1.exportar(ExportadorJSON())

