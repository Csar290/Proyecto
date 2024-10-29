import requests

def obtener_ubicacion():
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        return data['lat'], data['lon']
    except Exception as error:
        print("Error al obtener ubicación:", error)
        return None, None