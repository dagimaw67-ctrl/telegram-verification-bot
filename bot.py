import os
import requests

TOKEN = os.environ["BOT_TOKEN"]
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
offset = 0

while True:
    data = requests.get(
        url,
        params={"offset": offset + 1, "timeout": 30}
    ).json()

    for update in data.get("result", []):
        offset = update["update_id"]
        message = update.get("message", {})

        if message.get("text") == "/start":
            chat_id = message["chat"]["id"]
            requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                data={
                    "chat_id": chat_id,
                    "text": "Your verification code is\nMd12amu_hayolestu"
                }
            )
