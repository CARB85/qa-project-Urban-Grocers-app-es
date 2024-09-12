import copy

# Plantilla base del cuerpo de la solicitud para el kit
base_kit_body = {
    "name": "default_name"
}

# 1. Datos de prueba con nombre de un solo carácter
short_name_kit_body = copy.copy(base_kit_body)
short_name_kit_body["name"] = "a"

# 2. Datos de prueba con nombre de máximo 511 caracteres
long_name_kit_body = copy.copy(base_kit_body)
long_name_kit_body["name"] = "Abcd" * 127 + "C"

# 3. Datos de prueba con nombre vacío (0 caracteres)
empty_name_kit_body = copy.copy(base_kit_body)
empty_name_kit_body["name"] = ""

# 4. Datos de prueba con nombre mayor a 512 caracteres
exceeds_limit_kit_body = copy.copy(base_kit_body)
exceeds_limit_kit_body["name"] = "Abcd" * 128 + "X"  # 512 caracteres

# 5. Datos de prueba con caracteres especiales
special_chars_kit_body = copy.copy(base_kit_body)
special_chars_kit_body["name"] = "" "№%@\","

# 6. Datos de prueba con espacios
spaces_in_name_kit_body = copy.copy(base_kit_body)
spaces_in_name_kit_body["name"] = " A Aaa "

# 7. Datos de prueba con números
numbers_in_name_kit_body = copy.copy(base_kit_body)
numbers_in_name_kit_body["name"] = "123"

# 8. Datos de prueba sin el parámetro 'name'
no_name_kit_body = {}

# 9. Datos de prueba con 'name' como un número
numeric_name_kit_body = copy.copy(base_kit_body)
numeric_name_kit_body["name"] = 123  # Enviar número en lugar de cadena de texto



