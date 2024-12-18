import requests
from flask import Flask, request

app = Flask(__name__)

# Webhook yang akan menerima pesan WhatsApp dari Twilio
@app.route('/whatsapp-webhook', methods=['POST'])
def whatsapp_webhook():
    # Ambil data dari Twilio
    data = request.form
    print("Data yang diterima dari Twilio:", data)
    # Ambil isi pesan WhatsApp
    message_body = data.get('Body')  # Isi pesan WhatsApp
    print(f"Pesan WhatsApp: {message_body}")

    
    # Kirim pesan ke Discord
    send_to_discord(message_body)

    return 'OK', 200

# Kirim pesan ke Discord menggunakan Webhook
def send_to_discord(message):
    discord_webhook_url = 'https://discord.com/api/webhooks/1318698406536941570/C6wjA-2tookp1ORs_9YztN_jpu-DdLvFiZlTl71Zp_M6SV1LyYfR5o0scJhn5lJ8Bqzr'  # Ganti dengan URL webhook Discord
    payload = {'content': message}
    requests.post(discord_webhook_url, json=payload)

if __name__ == '__main__':
    # Jalankan server pada port 5000
    app.run(port=5000)
