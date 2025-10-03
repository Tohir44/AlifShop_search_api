# import requests
# import json
#
# BASE_URL = "https://gw.alifshop.uz"
# TOKEN = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vc2VydmljZS1jb3JlLmFsaWZuYXNpeWEuaW50ZXJuYWwvZ2F0ZXdheS9hbGlmc2hvcC9hdXRoL2xvZ2luIiwic3ViIjoiNDQyNzAyOCIsImp0aSI6ImJkZGZkOGE3LWVmZTUtNDM4Ni1hNDgwLTAwMWYxNmJkYzY4YyIsImlhdCI6MTc1ODg5OTE5NS4zMzE5OTEsIm5iZiI6MTc1ODg5OTE5NS4zMzE5OTEsImV4cCI6MTkxNDQxOTE5NS4zMzE5OTF9.KKAQer3s0QFnKNC-Edc7pVq4a0ANuPYwpIAtFweluhg"
#
# HEADERS = {
#     "Authorization": TOKEN,
#     "Content-Type": "application/json"
# }
#
#
# def fetch(path: str):
#     url = BASE_URL + path
#     response = requests.get(url, headers=HEADERS)
#     print(f"\n🔹 {path} | status: {response.status_code}")
#     try:
#         data = response.json()
#         print(json.dumps(data, indent=2, ensure_ascii=False)[:500], "...\n")
#         return data
#     except Exception as e:
#         print("Ошибка парсинга JSON:", e)
#         return None
#
#
# if __name__ == "__main__":
#     # Исправленные пути
#     events = fetch("/web/client/events/active")  # если такой существует
#     offers = fetch("/web/client/recommend/offers/v2")
#
#     if offers:
#         # Попробуем найти список "offers" внутри ответа
#         # Допустим API возвращает {"offers": [...]}
#         offer_list = offers.get("offers") or offers.get("data") or []
#         if isinstance(offer_list, list) and len(offer_list) > 0:
#             first = offer_list[0]
#             offer_id = first.get("id") or first.get("offer_id")
#             slug = first.get("slug")
#             print(f"➡️ Берем товар id={offer_id}, slug={slug}")
#
#             fetch("/web/client/recommend/delivery-time-estimation/duplicate")
#             if slug:
#                 fetch(f"/web/client/recommend/moderated-offers/{slug}")
#             if offer_id:
#                 fetch(f"/web/client/recommend/{offer_id}/reviews")
