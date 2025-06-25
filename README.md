# Tutorial Django + FastAPI: Consulta de Comisiones

Este proyecto demuestra cómo integrar un frontend en **Django** con un backend **FastAPI** para calcular comisiones sobre ventas ficticias, usando datos quemados (hardcoded).

---

## 🧩 Estructura del Proyecto

```
django_fastapi_comisiones/
│
├── backend_fastapi/
│   ├── data.py         # Datos de vendedores, ventas y reglas
│   ├── logic.py        # Lógica de cálculo de comisiones
│   └── main.py         # API FastAPI
│
├── core/               # App de Django
│   ├── views.py        # Vista que consulta a FastAPI
│   └── urls.py
│
├── frontend_django/    # Proyecto Django
│   ├── settings.py     # Configuración del proyecto
│   └── urls.py
│
├── templates/
│   └── home.html       # Interfaz para consultar comisiones
│
├── db.sqlite3          # Base de datos por defecto de Django
├── manage.py
├── render.yaml         # Configuración de despliegue en Render
└── requirements.txt
```

---

## 🔧 Paso a Paso

### 1. Clonar el proyecto

```bash
git clone https://github.com/JeffKun1999/minicoretuto.git
cd django_fastapi_comisiones
```

### 2. Crear entorno virtual

```bash
python -m venv env
source env\Scripts\activate  
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Correr FastAPI localmente

```bash
uvicorn backend_fastapi.main:app --reload --port 8001
```

### 5. Correr Django localmente

```bash
python manage.py runserver
```

### 6. Probar la app

Visita `http://127.0.0.1:8000/`, selecciona un rango de fechas y haz clic en **Calcular**.

---

## 🧠 Lógica del Cálculo de Comisiones

El backend de FastAPI calcula comisiones según reglas como:

- Si el monto total del vendedor ≥ 600 → comisión del 6%
- Si el monto total ≥ 800 → 10%
- Si el monto total ≥ 1000 → 8%
- Si ninguna regla aplica → 0%

El resultado se devuelve en JSON, y Django lo renderiza en una tabla.

---

## 🌐 Despliegue en Render
Te recomiendo esperar un poco a que se despliegue, dado que está desplegado con recursos free y no hay disponibilidad del 100%

- **FastAPI** se desplegó en:  
  `https://fastapi-backend-jnxh.onrender.com/comisiones/`



- **Django** se desplegó en:  
  `https://django-frontend-3cq5.onrender.com`
---

## 📎 Enlaces útiles

| Recurso | Enlace |
|--------|--------|
| Documentación Django | https://docs.djangoproject.com/en/5.2/ |
| Documentación FastAPI | https://fastapi.tiangolo.com/ |
| Video explicativo |https://youtu.be/ce9iPn-VX_o |
| Repositorio GitHub | https://github.com/JeffKun1999/minicoretuto.git |
| App desplegada | https://django-frontend-3cq5.onrender.com/ |

---

## 🧪 Créditos de ejemplo

Los datos están quemados (hardcoded) para fines demostrativos, tanto los vendedores como las reglas de comisión y ventas.

