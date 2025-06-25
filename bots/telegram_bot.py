from telethon import TelegramClient, events
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_BOT_TOKEN

client = TelegramClient("bot", TELEGRAM_API_ID, TELEGRAM_API_HASH).start(bot_token=TELEGRAM_BOT_TOKEN)

HELP_TEXT = (
    "/start – Welcome message\n"
    "/detect – Get vehicle license plate\n"
    "/help – Get all commands\n"
)

result = ""

@client.on(events.NewMessage(pattern="/start"))
async def start(evt):
    await evt.respond("👋 Hi! I'm active on Telegram, Discord and Slack.\nType /help to see my commands.")

@client.on(events.NewMessage(pattern="/detect"))
async def detect(evt):
    # You would call your function here
    await evt.respond(f"Vehicle is detected with number plate: \n {result}")

@client.on(events.NewMessage(pattern="/help"))
async def help_cmd(evt):
    await evt.respond(HELP_TEXT)

def run():
    client.run_until_disconnected()
    client.start()
    print("Telegram bot is running...")