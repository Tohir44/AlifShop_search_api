import requests

telegram_bot_token = "8301114039:AAEwdqiB82zLkOGZsESSzQRmlkSbPMMaicI"
chat_id = "8146373270" 

def send_telegram_message(message: str):
    """Отправка форматированного сообщения в Telegram."""
    if not telegram_bot_token or not chat_id:
        print("Telegram токен или CHAT_ID не заданы. Уведомление пропущено.")
        return

    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True
    }

    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print(f"Ошибка Telegram API: {response.text}")