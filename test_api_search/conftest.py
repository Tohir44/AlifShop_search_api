import pytest
import os


@pytest.fixture(scope="session", autouse=True)
def configure_allure():
    """Настройка Allure для сессии тестов."""
    # Устанавливаем категории для Allure
    categories = [
        {
            "name": "Failed tests",
            "matchedStatuses": ["failed"],
            "messageRegex": ".*AssertionError.*"
        },
        {
            "name": "Broken tests",
            "matchedStatuses": ["broken"],
            "messageRegex": ".*Exception.*"
        },
        {
            "name": "Skipped tests",
            "matchedStatuses": ["skipped"]
        }
    ]

    # Создаем директорию для результатов Allure если её нет
    if not os.path.exists("allure-results"):
        os.makedirs("allure-results")

    # Создаём директорию для репортов Allure если её нет
    if not os.path.exists("allure-reports"):
        os.makedirs("allure-reports")

    # Записываем конфигурацию категорий
    import json
    with open("allure-results/categories.json", "w") as f:
        json.dump(categories, f, indent=2)


@pytest.fixture(scope="session")
def allure_results_dir():
    """Возвращает путь к директории с результатами Allure."""
    return "allure-results"