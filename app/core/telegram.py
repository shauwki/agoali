import os
import telegram
import asyncio 
from telegram.error import TelegramError
from telegram import constants

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN ontbreekt in de environment!")

try:
    bot = telegram.Bot(token=TOKEN)
except TelegramError as e:
    print(f"Fout bij initialiseren van Telegram Bot: {e}")
    bot = None

def send_telegram_message(chat_id: int, text: str):
    """
    Een robuuste, herbruikbare functie om een bericht te sturen.
    Deze functie is synchroon, maar roept intern de async API correct aan.
    """
    if not bot:
        print(f"Fout: Bot is niet geïnitialiseerd. Kan bericht niet sturen naar {chat_id}.")
        return

    async def _send_async():
        """Interne async functie om de call te wrappen."""
        try:
            await bot.send_message(
                chat_id=chat_id,
                text=text,
                parse_mode=constants.ParseMode.MARKDOWN
            )
            print(f"TELEGRAM: Bericht succesvol verstuurd naar {chat_id}")
        except TelegramError as e:
            print(f"TELEGRAM: Fout bij sturen van bericht naar {chat_id}: {e}")

    try:
        asyncio.run(_send_async())
    except Exception as e:
        print(f"ASYNCIO Fout in send_telegram_message: {e}")