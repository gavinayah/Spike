# Deriv Pre-Spike Bot

Bot untuk mendeteksi sinyal pre-spike Boom/Crash dan mengirim ke Telegram.

## Cara Deploy (Render.com)

1. Upload semua file ini ke GitHub (public repo).
2. Deploy ke Render sebagai **Background Worker**.
3. Set Environment Variables:
   - `TELEGRAM_TOKEN`
   - `TELEGRAM_CHAT_ID`

Bot akan otomatis mengirim sinyal saat kondisi pre-spike terpenuhi.
