import discord
from  discord.ext import commands
from dotenv import load_dotenv
from Config import config
from services import LoggingService
from colorama import Fore, Style, init
import os

init(autoreset=True)
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
        print(f"moderation cogs [{Fore.GREEN}OK{Style.RESET_ALL}]")
        await self.load_extension("cogs.fun")
        print(f"fun cogs        [{Fore.GREEN}OK{Style.RESET_ALL}]")
        await self.load_extension("cogs.owner_only")
        print(f"owner_only cogs [{Fore.GREEN}OK{Style.RESET_ALL}]")

client = MyBot(command_prefix=PREFIX, intents=intents, help_command=None)
client.log_service = LoggingService(client)

@client.event
async def on_ready():
    print(f"Tiff            [{Fore.GREEN}OK{Style.RESET_ALL}]")
    print(f"{client.user} Serving \nID: {client.user.id}")

if __name__ == "__main__":
    client.run(TOKEN)

#! Version: 1.12.7