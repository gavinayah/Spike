import time
import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
from utils import is_valid_signal

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)

def main_loop():
    while True:
        rsi4 = 3.1
        rsi6 = 7.4
        cci = -132
        rsi_m5 = 22.8
        asset = "Boom 500"

        if is_valid_signal(rsi4, rsi6, cci, rsi_m5, asset):
            text = (
                f"🚨 *[Pre-Spike] {asset} BUY 🔼 (TEST)*\n"
                f"RSI(4)={rsi4} | RSI(6)={rsi6} | CCI={cci}\n"
                f"✅ M5 RSI={rsi_m5} ➜ KONFIRMASI\n"
                f"🕒 Waktu: (Simulasi)"
            )
            send_message(text)
        time.sleep(60)

if __name__ == "__main__":
    main_loop()
