# AlifShop_search_api

Final QA project — API tests for Alif Shop (search).

## Structure
- tests/ - pytest tests
- conftest.py - fixtures
- pytest.ini - pytest config
- requirements.txt - dependencies

## Run locally
1. python -m venv .venv
2. .\.venv\Scripts\activate
3. pip install -r requirements.txt
4. pytest --alluredir=allure-results
5. (optional) allure serve allure-results

## CI
GitHub Actions запускает тесты и загружает allure-results в артефакты.
