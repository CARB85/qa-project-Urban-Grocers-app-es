import requests
from configuration import CREATE_USER_PATH, KITS_PATH

def post_new_user():
    response = requests.post(CREATE_USER_PATH, json={})
    if response.status_code != 201:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
    response.raise_for_status()
    return response.json().get('authToken')

def post_new_client_kit(kit_body, auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(KITS_PATH, json=kit_body, headers=headers)
    print(response.status_code, response.json())  # Imprime el código de estado y la respuesta para depuración
    return response




