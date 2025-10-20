import time

def download_and_install(chat_id: int, url: str):
    """
    Mock-functie om een installatie te simuleren.
    """
    print(f"LOGIC: Gestart met installatie voor {chat_id} van URL: {url}")
    time.sleep(5)
    print(f"LOGIC: Installatie voltooid voor {chat_id}")
    return f"Installatie van {url} is gelukt."