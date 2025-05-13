from flask import Flask, render_template, request
import requests
import re

app = Flask(__name__)

# Configuración de API Keys
IPINFO_API_KEY = "208de512423486"
TELEGRAM_BOT_TOKEN = "6485736942:AAGlVxaxzZT93yC9JG8QE44HijwkhnKfJ8k"
CHAT_ID = "2044147106"

# Función para escapar caracteres especiales en MarkdownV2
def escape_markdown(text):
    return re.sub(r'([_*\[\]()~`>#+-=|{}.!])', r'\\\1', text)

# Función para enviar mensaje a Telegram
def send_telegram_message(ip_data):
    message = (
        f"🚀 *Nueva Visita en la Página*\n\n"
        f"📍 *IP:* {escape_markdown(ip_data.get('ip', 'Desconocida'))}\n"
        f"🌍 *Ciudad:* {escape_markdown(ip_data.get('city', 'Desconocida'))}\n"
        f"🗺️ *Región:* {escape_markdown(ip_data.get('region', 'Desconocida'))}\n"
        f"🌎 *País:* {escape_markdown(ip_data.get('country', 'Desconocido'))}\n"
        f"📍 *Ubicación:* {escape_markdown(ip_data.get('loc', 'Desconocida'))}\n"
        f"🌐 *ISP:* {escape_markdown(ip_data.get('org', 'Desconocido'))}\n"
        f"🕒 *Zona Horaria:* {escape_markdown(ip_data.get('timezone', 'Desconocida'))}"
    )

    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "MarkdownV2"
    }

    response = requests.post(telegram_url, json=payload)
    return response.status_code, response.json()

# Ruta principal
@app.route("/")
def home():
    visitor_ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    # Consultar IPInfo
    response = requests.get(f"https://ipinfo.io/{visitor_ip}/json?token={IPINFO_API_KEY}")
    ip_data = response.json()

    # Enviar a Telegram
    send_telegram_message(ip_data)

    return render_template("index.html")  # Muestra la página HTML

if __name__ == "__main__":
    app.run(debug=True)


#pip install python-telegram-bot
