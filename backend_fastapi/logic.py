# backend_fastapi/logic.py

from datetime import datetime
from collections import defaultdict
from .data import ventas, reglas, vendedores

def calcular_comisiones(fecha_inicio: str, fecha_fin: str):
    inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fin = datetime.strptime(fecha_fin, "%Y-%m-%d")

    # Sumar cuotas por vendedor dentro del rango
    totales_por_vendedor = defaultdict(float)

    for venta in ventas:
        fecha_venta = datetime.strptime(venta["fecha"], "%Y-%m-%d")
        if inicio <= fecha_venta <= fin:
            totales_por_vendedor[venta["vendedor_id"]] += venta["cuota_monto"]

    # Calcular comisión usando la regla aplicable
    resultado = []
    for vendedor_id, total in totales_por_vendedor.items():
        regla_aplicable = max(
            (r for r in reglas if r["monto"] <= total),
            key=lambda r: r["monto"],
            default=None
        )

        if regla_aplicable:
            comision = total * regla_aplicable["rule"]
        else:
            comision = 0.0

        nombre_vendedor = next((v["usuario"] for v in vendedores if v["id"] == vendedor_id), "Desconocido")
        resultado.append({
            "vendedor": nombre_vendedor,
            "comision": round(comision, 2)
        })

    return resultado
