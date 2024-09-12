import requests
from configuration import URL_SERVICE, CREATE_USER_PATH, KITS_PATH, AUTH_HEADER, CONTENT_TYPE_HEADER

# Función para crear un nuevo usuario y obtener el token de autenticación
def post_new_user():
    response = requests.post(f"{URL_SERVICE}{CREATE_USER_PATH}")
    auth_token = response.json().get("authToken")
    return auth_token

# Función para crear un kit
def post_new_client_kit(kit_body, auth_token):
    headers = {
        AUTH_HEADER: f"Bearer {auth_token}",
        CONTENT_TYPE_HEADER: "application/json"
    }
    response = requests.post(f"{URL_SERVICE}{KITS_PATH}", headers=headers, json=kit_body)
    return response
