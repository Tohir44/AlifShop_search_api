import pytest
import os
import json

@pytest.fixture(scope="session", autouse=True)
def configure_allure():
    """Создаёт папки и категории для Allure"""
    os.makedirs("allure-results", exist_ok=True)
    categories = [
        {"name": "Failed tests", "matchedStatuses": ["failed"]},
        {"name": "Broken tests", "matchedStatuses": ["broken"]},
        {"name": "Skipped tests", "matchedStatuses": ["skipped"]}
    ]
    with open("allure-results/categories.json", "w") as f:
        json.dump(categories, f, indent=2)

