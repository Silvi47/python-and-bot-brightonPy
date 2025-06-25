import asyncio
from slack import RTMClient               # imported from slackclient
from config import SLACK_BOT_TOKEN

HELP_TEXT = (
    "start – Welcome message\n"
    "detect – Get vehicle license plate\n"
    "help – Get all commands\n"
)

async def handle_messages(**payload):
    result = ""
    data = payload["data"]
    web_client = payload["web_client"]
    if "text" not in data:
        return

    channel = data["channel"]
    text = data["text"].strip().lower()

    if "start" in text:
        await web_client.chat_postMessage(channel=channel, text="👋 Hi! I'm active on Slack, Telegram and Discord.\nType *help* to see commands.")
    elif "detect" in text:
        # You would call your detection function here
        await web_client.chat_postMessage(channel=channel, text={f"Vehicle is detected with number plate:"})
    elif "help" in text:
        await web_client.chat_postMessage(channel=channel, text=HELP_TEXT)

async def run():
    rtm = RTMClient(token=SLACK_BOT_TOKEN, run_async=True)
    rtm.on(event="message")(handle_messages)
    await rtm.start()
