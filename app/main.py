from fastapi import FastAPI, Request
from tasks import process_telegram_message
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"Status": "Mod Assistant API is online"}

@app.post("/webhook/telegram")
async def handle_telegram_webhook(request: Request):
    """
    Dit is het 'schakelbord'.
    Het vangt de Telegram webhook, parseert de basis-info
    en delegeert de taak onmiddellijk naar de Celery worker.
    """
    print("WEB: Webhook ontvangen!")
    try:
        data = await request.json()
        message = data.get('message', {})
        chat_id = message.get('chat', {}).get('id')
        text = message.get('text', '')

        if not chat_id or not text:
            print("WEB: Geen valide bericht (chat_id or text mist)")
            return {"status": "error", "message": "Geen valide bericht"}
        print(f"WEB: Delegeer taak naar worker: {text}")
        process_telegram_message.delay(chat_id, text)
        return {"status": "ok", "message": "Taak ontvangen"}

    except json.JSONDecodeError:
        print("WEB: Fout bij parsen van JSON")
        return {"status": "error", "message": "Invalide JSON"}, 400
    except Exception as e:
        print(f"WEB: Onbekende webhook Fout: {e}")
        return {"status": "error", "message": "Interne serverfout"}, 500