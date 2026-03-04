import discord
from  discord.ext import commands
from dotenv import load_dotenv
from discord import app_commands
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX", "$")
GID = os.getenv("GUILD_ID")

intents = discord.Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    async def setup_hook(self):
        # Cargar cogs
        await self.load_extension("cogs.moderation")
        await self.load_extension("cogs.fun")

        # Sincronización rápida solo en tu servidor de desarrollo
        guild = discord.Object(id=int(GID))
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)
        #print("Slash commands sincronizados en global 🌍")
        print("Slash commands sincronizados en desarrollo ⚡")

client = MyBot(command_prefix=PREFIX, intents=intents, help_command=None)

@client.event
async def on_ready():
    print(f"{client.user} sirviendo...")

if __name__ == "__main__":
    client.run(TOKEN)

#! Version: 1.3.0