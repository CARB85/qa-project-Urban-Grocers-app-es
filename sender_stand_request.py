import requests
from configuration import BASE_URL, CREATE_USER_PATH, CREATE_KIT_PATH

def post_new_user():
    # Envía una solicitud para crear un nuevo usuario
    response = requests.post(f"{BASE_URL}{CREATE_USER_PATH}")
    return response.json()["authToken"]

def post_new_client_kit(kit_body, auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }
    response = requests.post(f"{BASE_URL}{CREATE_KIT_PATH}", json=kit_body, headers=headers)
    return response

