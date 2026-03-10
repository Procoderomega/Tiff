import discord
from  discord.ext import commands
from dotenv import load_dotenv
from Config import config
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
PREFIX = config["Bot"]["Prefix"]
GID = config["Server"]["Guild_Id"]

intents = discord.Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    async def setup_hook(self):
        # Loading da cogs
        await self.load_extension("cogs.moderation")
        await self.load_extension("cogs.fun")
        await self.load_extension("cogs.owner_only")

client = MyBot(command_prefix=PREFIX, intents=intents, help_command=None)

@client.event
async def on_ready():
    print(f"{client.user} sirviendo...")

if __name__ == "__main__":
    client.run(TOKEN)

#! Version: 1.12.7