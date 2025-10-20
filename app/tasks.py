import time
from core.celery_app import app
from core.telegram import send_telegram_message
from logic import install_fs22, scrape_gta5

@app.task
def process_telegram_message(chat_id: int, text: str):
    """
    Verwerkt een inkomend Telegram-bericht op de achtergrond 
    en stuurt een antwoord terug.
    """
    print(f"BEGIN TAAK: Verwerk bericht van {chat_id}: '{text}'")
    send_telegram_message(chat_id, f"🤖 Taak ontvangen: `{text}`. Ik ga aan de slag...")
    try:
        if text.lower().startswith('/find gta5') or text.lower().startswith('/find gtav'):
            if text.lower().startswith('/find gta5'):
                query = text[len('/find gta5'):].strip()
            else:
                query = text[len('/find gtav'):].strip()
            result = scrape_gta5.find_mod(query)
            response_text = f"✅ *Zoekopdracht voltooid!*\n\n*Titel:* {result['title']}\n*URL:* {result['url']}"
            send_telegram_message(chat_id, response_text)
            
        elif text.startswith('/install'):
            url = text.replace('/install', '').strip()
            result = install_fs22.download_and_install(chat_id, url)
            response_text = f"✅ *Installatie voltooid!*\n\n{result}"
            send_telegram_message(chat_id, response_text)

        else:
            print("LOGIC: Commando niet herkend.")
            time.sleep(1)
            response_text = f"❓ Sorry, dat commando begrijp ik (nog) niet.\n\n(Probeer: `/find gtav [zoekterm]` of `/install [url]`)"
            send_telegram_message(chat_id, response_text)

    except Exception as e:
        print(f"FOUT: Taak mislukt: {e}")
        response_text = f"❌ *Oeps, er ging iets fout!*\n\nDe taak `{text}` is mislukt.\n*Foutmelding:* `{e}`"
        send_telegram_message(chat_id, response_text)
    
    return f"Taak voor {chat_id} voltooid."