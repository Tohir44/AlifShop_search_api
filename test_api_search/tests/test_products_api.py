import requests
import allure

BASE_URL = "https://gw.alifshop.uz/web/client/search"

@allure.feature("Products API")
@allure.story("Позитивный тест")
def test_products_positive():
    payload = {"query": "iphone"}
    response = requests.post(f"{BASE_URL}/full-text", json=payload)
    assert response.status_code == 200
    json_data = response.json()
    assert "items" in json_data
    assert isinstance(json_data["items"], list)
    assert len(json_data["items"]) > 0

@allure.story("Негативный тест — некорректные символы")
def test_products_negative_symbols():
    payload = {"query": "@@@###!!!"}
    response = requests.post(f"{BASE_URL}/full-text", json=payload)
    assert response.status_code == 200
    json_data = response.json()
    assert "items" in json_data
    assert isinstance(json_data["items"], list)
