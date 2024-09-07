import pytest
from sender_stand_request import post_new_user, post_new_client_kit
from data import get_kit_body

def get_new_user_token():
    return post_new_user()

def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

@pytest.mark.parametrize("kit_body", [get_kit_body("a"), get_kit_body("A" * 511), get_kit_body(""), get_kit_body("A" * 512), get_kit_body("!@#$%^&*()"), get_kit_body(" A Aaa "), get_kit_body("123")])
def test_valid_kit_name(kit_body):
    if len(kit_body["name"]) in [1, 511, 0, 512]:
        negative_assert_code_400(kit_body)
    else:
        positive_assert(kit_body)

@pytest.mark.parametrize("kit_body", [get_kit_body("!@#$%^&*()"), get_kit_body(" A Aaa "), get_kit_body("123")])
def test_valid_kit_name_characters(kit_body):
    positive_assert(kit_body)

