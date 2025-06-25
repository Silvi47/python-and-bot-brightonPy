from bots.telegram_bot import run as run_telegram
from bots.discord_bot import run as run_discord
from bots.slack_bot import run as run_slack

def start_telegram():
    print("[Telegram] starting…")
    run_telegram()

def start_discord():
    print("[Discord] starting…")
    run_discord() 

async def start_slack():
    print("[Slack] starting…")
    await run_slack()        # awaits RTM start()

def main():
    start_discord()
    start_telegram()
    start_slack()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nShutting down bots…")
