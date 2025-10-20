import time

def find_mod(query: str):
    """
    Mock-functie om een zoekopdracht te simuleren.
    """
    print(f"LOGIC: Zoeken naar GTA5 mod: '{query}'")
    # Simuleer 2 seconden werk (scrapen)
    time.sleep(2)
    mock_result = {
        "title": "Gevonden Mock Mod",
        "url": "http://example.com/gta5-mod"
    }
    print(f"LOGIC: Zoekopdracht voltooid. Resultaat: {mock_result['title']}")
    return mock_result