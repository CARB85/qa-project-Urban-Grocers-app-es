# data.py
import copy

kit_body_1_char = {"name": "a"}  # Nombre con 1 carácter
kit_body_511_chars = {
    "name": "Abcd" * 127 + "A"
}  # Nombre con 511 caracteres

kit_body_512_chars = {
    "name": "Abcd" * 127 + "Abc"
}  # Nombre con 512 caracteres

kit_body_empty = {"name": ""}  # Nombre vacío
kit_body_special_chars = {"name": "№%@,"}  # Nombre con caracteres especiales
kit_body_spaces = {"name": " A Aaa "}  # Nombre con espacios
kit_body_numbers = {"name": "123"}  # Nombre con números
kit_body_no_param = {}  # Sin parámetro 'name'
kit_body_numeric = {"name": 123}  # Nombre como número

# función copy() para duplicar los cuerpos de solicitud.
def get_kit_body(body):
    return copy.deepcopy(body)


