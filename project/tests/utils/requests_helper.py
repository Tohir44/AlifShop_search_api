import requests

def get_with_auth(url, token):
    """GET-запрос с токеном"""
    headers = {"Authorization": f"Bearer {token}"}
    return requests.get(url, headers=headers)

