import requests
import allure
import json


def get_with_auth(url, token):
    """GET-запрос с токеном + логирование в Allure"""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    attach_request_response(response, url, headers)
    return response


def attach_request_response(response, url, headers):
    """Прикрепляет детали запроса и ответа в Allure"""
    with allure.step("Attach request and response details"):
        # Request info
        allure.attach(
            f"URL: {url}\nHeaders: {json.dumps(headers, indent=2)}",
            name="Request",
            attachment_type=allure.attachment_type.TEXT
        )

        # Response status + headers
        allure.attach(
            f"Status code: {response.status_code}\nHeaders: {dict(response.headers)}",
            name="Response Info",
            attachment_type=allure.attachment_type.TEXT
        )

        # Response body
        try:
            allure.attach(
                json.dumps(response.json(), indent=2, ensure_ascii=False),
                name="Response Body (JSON)",
                attachment_type=allure.attachment_type.JSON
            )
        except Exception:
            allure.attach(
                response.text,
                name="Response Body (RAW)",
                attachment_type=allure.attachment_type.TEXT
            )
