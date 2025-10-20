import time
from core.celery_app import app

# Importeer de *modules* uit je logic-package
from logic import install_fs22, scrape_gta5

@app.task
def process_telegram_message(chat_id: int, text: str):
    """
    Verwerkt een inkomend Telegram-bericht op de achtergrond.
    """
    print(f"BEGIN TAAK: Verwerk bericht van {chat_id}: '{text}'")
    
    try:
        if text.startswith('/find gta5'):
            query = text.replace('/find gta5', '').strip()
            # Roep de mock-functie aan uit de geïmporteerde module
            result = scrape_gta5.find_mod(query)
            print(f"TAAK VOLTOOID: {result['title']}")
            
        elif text.startswith('/install'):
            url = text.replace('/install', '').strip()
            # Roep de mock-functie aan
            result = install_fs22.download_and_install(chat_id, url)
            print(f"TAAK VOLTOOID: {result}")

        else:
            print("LOGIC: Commando niet herkend, simuleer 1 seconde werk.")
            time.sleep(1)
            print("TAAK VOLTOOID: Onbekend commando verwerkt.")

    except Exception as e:
        print(f"FOUT: Taak mislukt: {e}")
        # Hier kun je later een Telegram-bericht terugsturen
    
    return f"Taak voor {chat_id} voltooid."