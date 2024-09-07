import copy

kit_body_template = {
    "name": ""
}

def get_kit_body(name):
    body = copy.deepcopy(kit_body_template)
    body["name"] = name
    return body

