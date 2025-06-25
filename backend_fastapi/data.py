# backend_fastapi/data.py

vendedores = [
    {"id": 1, "usuario": "Ana Torres"},
    {"id": 2, "usuario": "Carlos Ruiz"},
    {"id": 3, "usuario": "María López"},
    {"id": 4, "usuario": "Luis Pérez"},
]

ventas = [
    {"fecha": "2025-06-01", "vendedor_id": 1, "cuota_monto": 300},  # Total = 300 → sin regla
    {"fecha": "2025-06-02", "vendedor_id": 2, "cuota_monto": 400},  # Total = 400 → sin regla
    {"fecha": "2025-06-03", "vendedor_id": 3, "cuota_monto": 500},
    {"fecha": "2025-06-04", "vendedor_id": 3, "cuota_monto": 200},  # Total = 700 → regla 600 → 0.06
    {"fecha": "2025-06-05", "vendedor_id": 4, "cuota_monto": 900},  # Total = 900 → regla 800 → 0.10
    {"fecha": "2025-06-06", "vendedor_id": 4, "cuota_monto": 200},  # Total = 1100 → regla 1000 → 0.08
]

reglas = [
    {"id_regla": 1, "rule": 0.06, "monto": 600},
    {"id_regla": 2, "rule": 0.08, "monto": 1000},
    {"id_regla": 3, "rule": 0.10, "monto": 800},
]
