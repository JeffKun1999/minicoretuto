from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    resultado = None

    # Usa GET y verifica que existan los parámetros
    if request.method == 'GET' and 'start_date' in request.GET and 'end_date' in request.GET:
        fecha_inicio = request.GET.get('start_date')
        fecha_fin = request.GET.get('end_date')

        url = 'http://127.0.0.1:8001/comisiones/'
        params = {'fecha_inicio': fecha_inicio, 'fecha_fin': fecha_fin}
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                resultado = response.json()
            else:
                resultado = [{"vendedor": "Error", "comision": f"FastAPI respondió {response.status_code}"}]
        except Exception as e:
            resultado = [{"vendedor": "Error", "comision": str(e)}]

    return render(request, 'home.html', {
        'resultado': resultado,
        'start_date': request.GET.get('start_date', ''),
        'end_date': request.GET.get('end_date', '')
    })
