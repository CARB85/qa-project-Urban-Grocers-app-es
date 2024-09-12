from sender_stand_request import post_new_client_kit, post_new_user
from data import (
    short_name_kit_body, long_name_kit_body, empty_name_kit_body,
    exceeds_limit_kit_body, special_chars_kit_body, spaces_in_name_kit_body, numbers_in_name_kit_body, no_name_kit_body,
    numeric_name_kit_body
)

# Función para obtener un nuevo token de usuario
def get_new_user_token():
    return post_new_user()

# Función para pruebas positivas (código 201)
def positive_assert(kit_body):
    token = get_new_user_token()
    response = post_new_client_kit(kit_body, token)
    print(f"El código de respuesta es: {response.status_code}")
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

# Función para pruebas negativas (código 400)
def negative_assert_code_400(kit_body):
    token = get_new_user_token()
    response = post_new_client_kit(kit_body, token)
    print(f"El código de respuesta es: {response.status_code}")
    assert response.status_code == 400

# Prueba con nombre de un solo carácter (Positiva)
def test_short_name_kit():
    positive_assert(short_name_kit_body)

# Prueba con nombre de 511 caracteres (Positiva)
def test_long_name_kit():
    positive_assert(long_name_kit_body)

# Prueba con nombre vacío (Negativa)
def test_empty_name_kit():
    negative_assert_code_400(empty_name_kit_body)

# Prueba con nombre mayor a 512 caracteres (Negativa)
def test_name_exceeds_limit_kit():
    negative_assert_code_400(exceeds_limit_kit_body)

# Prueba con caracteres especiales (Positiva)
def test_special_chars_name_kit():
    positive_assert(special_chars_kit_body)

# Prueba con espacios en el nombre (Positiva)
def test_spaces_in_name_kit():
    positive_assert(spaces_in_name_kit_body)

# Prueba con números en el nombre (Positiva)
def test_numbers_in_name_kit():
    positive_assert(numbers_in_name_kit_body)

# Prueba sin el parámetro 'name' (Negativa)
def test_no_name_kit():
    negative_assert_code_400(no_name_kit_body)

# Prueba con 'name' como un número (Negativa)
def test_numeric_name_kit():
    negative_assert_code_400(numeric_name_kit_body)
