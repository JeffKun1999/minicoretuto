# backend_fastapi/main.py

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from .logic import calcular_comisiones

app = FastAPI()

# Permitir llamadas desde Django
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción se debe limitar esto
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/comisiones/")
def get_comisiones(fecha_inicio: str = Query(...), fecha_fin: str = Query(...)):
    return calcular_comisiones(fecha_inicio, fecha_fin)
