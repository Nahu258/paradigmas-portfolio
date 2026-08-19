import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def ejecutar_peticion_get():
    print("=" * 60)
    print("1. PETICIÓN GET: Obtener lista de publicaciones")
    # print("=" * 60)
    
    try:
        response = requests.get(BASE_URL)
        
        print(f"Status Code: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        print("\nTodos los Headers de respuesta:")
        for header, value in response.headers.items():
            print(f"  {header}: {value}")
            
        datos = response.json()
        print(f"\nCantidad total de registros obtenidos: {len(datos)}")
        print("\nEjemplo de los primeros 2 elementos obtenidos:")
        print(json.dumps(datos[:2], indent=2, ensure_ascii=False))
        
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición GET: {e}")

def ejecutar_peticion_post():
    print("\n" + "=" * 60)
    print("2. PETICIÓN POST: Crear un nuevo registro")
    print("=" * 60)
    
    nuevo_post = {
        "title": "Publicación de prueba",
        "body": "Este es el contenido enviado mediante cliente_http.py",
        "userId": 1
    }
    
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }
    
    print("Cuerpo (payload) a enviar:")
    print(json.dumps(nuevo_post, indent=2, ensure_ascii=False))
    
    try:
        response = requests.post(BASE_URL, json=nuevo_post, headers=headers)
        
        print(f"\nStatus Code obtenido: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        
        # 3. Validar retorno 201 Created
        if response.status_code == 201:
            print("[OK] Validación exitosa: Se recibió el código esperado (201 Created).")
        else:
            print(f"[ALERTA] Validación fallida: Se esperaba 201 pero se recibió {response.status_code}.")
            
        print("\nRespuesta del servidor:")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición POST: {e}")

if __name__ == "__main__":
    print("Iniciando pruebas de cliente HTTP con API REST pública...")
    ejecutar_peticion_get()
    ejecutar_peticion_post()
    print("\n" + "=" * 60)
    print("Pruebas finalizadas con éxito.")
    print("=" * 60)
