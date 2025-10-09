import subprocess
import pytest
import os
import json
 
from utils.telegram_bot_notifier import send_telegram_message 


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


def parse_allure_results(results_dir: str):
    """Собирает краткую статистику из allure-results."""
    summary = {
        "passed": 0,
        "failed": 0,
        "broken": 0,
        "skipped": 0,
        "total": 0,
        "report_url": "https://niyaz-ananev-khayrullayevich.github.io/AllureTest/"  
    }

    # Опционально: сгенерировать отчёт
    subprocess.run(
        ["allure", "generate", results_dir, "-o", "allure-reports", "--clean"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # Прочитаем файлы JSON из allure-results
    for file in os.listdir(results_dir):
        if file.endswith("-result.json"):
            with open(os.path.join(results_dir, file)) as f:
                data = json.load(f)
                status = data.get("status", "")
                if status in summary:
                    summary[status] += 1
                summary["total"] += 1

    return summary


def pytest_sessionfinish(session, exitstatus):
    """
    Хук pytest — вызывается после завершения всех тестов.
    Здесь собираем статистику и шлём уведомление в Telegram.
    """
    summary = parse_allure_results("allure-results")

    message = (
        f"*Результаты автотестов*\n\n"
        f"Успешно: {summary['passed']}\n"
        f"Провалено: {summary['failed']}\n"
        f"Сломано: {summary['broken']}\n"
        f"Пропущено: {summary['skipped']}\n"
        f"Всего: {summary['total']}\n\n"
        f"[Открыть Allure отчёт]({summary['report_url']})"
    )

    send_telegram_message(message) 