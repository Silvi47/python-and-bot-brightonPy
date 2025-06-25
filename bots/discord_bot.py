import asyncio
import discord
from discord.ext import commands
from config import DISCORD_BOT_TOKEN

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

HELP_TEXT = (
    "!start – Welcome message\n"
    "!detect – Get vehicle license plate\n"
    "!help – Get all commands\n"
)

result = ""

@client.event
async def on_ready():
    print(f"[Discord] Logged in as {client.user} (ID: {client.user.id})")

@client.command(name="start")
async def start(ctx):
    await ctx.send("👋 Hi! I'm live on Discord, Telegram and Slack — use !help to see commands.")

@client.command(name="detect")
async def detect(ctx):
    # You would call your detection function here
    await ctx.send(f"Vehicle is detected with number plate: \n")

@client.command(name="help77")
async def help_cmd(ctx):
    await ctx.send(HELP_TEXT)

def run():
    client.run(DISCORD_BOT_TOKEN)
    print("Discord bot is running...")