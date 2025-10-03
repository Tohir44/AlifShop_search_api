import requests
from project.utils.requests_helper import get_with_auth

BASE_URL = "https://gw.alifshop.uz/web/client"

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."  # твой токен


def test_active_events():
    url = f"{BASE_URL}/events/active"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_popular_brands():
    url = f"{BASE_URL}/brands/popular"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)


def test_reviews():
    url = f"{BASE_URL}/moderated-offers/a57a02e4-cbb0-476b-ab3e-713a1682ef1d/reviews"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert "offer_reviews" in data
    assert isinstance(data["offer_reviews"], list)


def test_delivery_time():
    url = f"{BASE_URL}/catalog/moderated-offers/ad08d811-e10b-466b-a96a-0708d9c6fe43/delivery-time-estimation"
    response = get_with_auth(url, TOKEN)
    assert response.status_code == 200
    data = response.json()
    assert "delivery_time" in data or "days_to_deliver" in data


def test_offers_v2():
    url = f"{BASE_URL}/brands/popular"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)










# import requests
# from config.settings import BASE_URL
# from project.utils.requests_helper import get_with_auth
#
#
# def test_active_events():
#     url = f"{BASE_URL}/events/active"
#     response = requests.get(url)
#     assert response.status_code == 200
#     data = response.json()
#     assert isinstance(data, list)
#
#
# def test_popular_brands():
#     url = f"{BASE_URL}/brands/popular"
#     response = requests.get(url)
#     assert response.status_code == 200
#     data = response.json()
#     assert "data" in data
#     assert isinstance(data["data"], list)
#
#
# def test_reviews():
#     url = f"{BASE_URL}/moderated-offers/a57a02e4-cbb0-476b-ab3e-713a1682ef1d/reviews"
#     response = requests.get(url)
#     assert response.status_code == 200
#     data = response.json()
#     assert "offer_reviews" in data
#     assert isinstance(data["offer_reviews"], list)
#
#
# def test_delivery_time():
#     url = f"{BASE_URL}/catalog/moderated-offers/ad08d811-e10b-466b-a96a-0708d9c6fe43/delivery-time-estimation"
#     response = get_with_auth(url)
#     assert response.status_code == 200
#     data = response.json()
#     assert "delivery_time" in data or "days_to_deliver" in data
#
#
# def test_offers_v2():
#     url = f"{BASE_URL}/brands/popular"
#     response = requests.get(url)
#     assert response.status_code == 200
#     data = response.json()
#     assert "data" in data
#     assert isinstance(data["data"], list)











# import requests
#
# BASE_URL = "https://gw.alifshop.uz/web/client"
#
# # Братья, незабываем матерей! Токены бывуют разние
# TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vc2VydmljZS1jb3JlLmFsaWZuYXNpeWEuaW50ZXJuYWwvZ2F0ZXdheS9hbGlmc2hvcC9hdXRoL2xvZ2luIiwic3ViIjoiNDQyNzAyOCIsImp0aSI6ImJkZGZkOGE3LWVmZTUtNDM4Ni1hNDgwLTAwMWYxNmJkYzY4YyIsImlhdCI6MTc1ODg5OTE5NS4zMzE5OTEsIm5iZiI6MTc1ODg5OTE5NS4zMzE5OTEsImV4cCI6MTkxNDQxOTE5NS4zMzE5OTF9.KKAQer3s0QFnKNC-Edc7pVq4a0ANuPYwpIAtFweluhg"
#
#
# def test_active_events():
#     url = f"{BASE_URL}/events/active"
#     response = requests.get(url)
#     assert response.status_code == 200
#     data = response.json()
#     assert isinstance(data, list)
#
#
# def test_popular_brands():
#     url = f"{BASE_URL}/brands/popular"
#     response = requests.get(url)
#     assert response.status_code == 200
#     data = response.json()
#     assert "data" in data
#     assert isinstance(data["data"], list)
#
#
# def test_reviews():
#     url = f"{BASE_URL}/moderated-offers/a57a02e4-cbb0-476b-ab3e-713a1682ef1d/reviews"
#     response = requests.get(url)
#     assert response.status_code == 200
#     data = response.json()
#     assert "offer_reviews" in data
#     assert isinstance(data["offer_reviews"], list)
#
#
# def test_delivery_time():
#     url = f"{BASE_URL}/catalog/moderated-offers/ad08d811-e10b-466b-a96a-0708d9c6fe43/delivery-time-estimation"
#     headers = {"Authorization": f"Bearer {TOKEN}"}
#     response = requests.get(url, headers=headers)
#     assert response.status_code == 200
#     data = response.json()
#     assert "delivery_time" in data or "days_to_deliver" in data
#
#
# def test_offers_v2():
#     url = f"{BASE_URL}/brands/popular"
#     response = requests.get(url)
#     assert response.status_code == 200
#     data = response.json()
#     assert "data" in data
#     assert isinstance(data["data"], list)
