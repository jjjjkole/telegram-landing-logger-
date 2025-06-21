
from flask import Flask, request
from flask_cors import CORS
import requests
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Разрешаем кросс-доменные запросы

BOT_TOKEN = "7796439721:AAGDOAFhAy3km1z7wyn7OHwGr6wlnxgxC_0"
CHAT_ID = 5206914915

@app.route('/log', methods=['POST'])
def log_data():
    data = request.json
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'unknown')
    product_id = data.get("product_id", "n/a")
    user_id = data.get("user_id", "n/a")
    city = data.get("city", "n/a")
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    message = f"""🔔 <b>Новый заход на лендинг</b>
🕒 {time}
🌐 IP: <code>{ip}</code>
📱 User-Agent: <code>{user_agent}</code>
🛒 Product ID: <b>{product_id}</b>
👤 User ID: <b>{user_id}</b>
📍 Город: <b>{city}</b>"""

    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    })

    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
