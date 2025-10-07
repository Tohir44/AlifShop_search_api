import requests
import pytest
import allure

BASE_URL = "https://gw.alifshop.uz/web/client/search"

@allure.feature("Suggestions API")
@allure.story("Проверка корректного ответа при валидном запросе")
def test_suggestions_positive():
    payload = {"query": "iphone"}
    response = requests.post(f"{BASE_URL}/suggestions", json=payload)

    assert response.status_code == 200, f"Статус код: {response.status_code}"
    data = response.json()

    assert "suggestions" in data, "Нет ключа 'suggestions'"
    assert isinstance(data["suggestions"], dict)
    assert "queries" in data["suggestions"]


@allure.story("Проверка поведения при пустом запросе")
def test_suggestions_negative_empty():
    payload = {"query": ""}
    response = requests.post(f"{BASE_URL}/suggestions", json=payload)

    assert response.status_code in [200, 400], f"Статус код: {response.status_code}"
    data = response.json()
    assert "suggestions" in data, "Нет ключа 'suggestions'"