# create_kit_name_kit_test.py
import pytest
from sender_stand_request import post_new_user, post_new_client_kit
from data import (
    kit_body_1_char, kit_body_511_chars, kit_body_512_chars,
    kit_body_empty, kit_body_special_chars, kit_body_spaces,
    kit_body_numbers, kit_body_no_param, kit_body_numeric
)

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

def test_name_with_1_character():
    positive_assert(kit_body_1_char)

def test_name_with_511_characters():
    positive_assert(kit_body_511_chars)

def test_name_with_512_characters():
    negative_assert_code_400(kit_body_512_chars)

def test_name_empty():
    negative_assert_code_400(kit_body_empty)

def test_name_with_special_chars():
    positive_assert(kit_body_special_chars)

def test_name_with_spaces():
    positive_assert(kit_body_spaces)

def test_name_with_numbers():
    positive_assert(kit_body_numbers)

def test_name_missing_param():
    negative_assert_code_400(kit_body_no_param)

def test_name_with_numeric_value():
    negative_assert_code_400(kit_body_numeric)
