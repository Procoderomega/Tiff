import discord
from  discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX", "$")

#? Configuramos intents
intents = discord.Intents.default()
intents.message_content=True
intents.members=True

client = commands.Bot(command_prefix=PREFIX, intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} sirviendo...")

if __name__ == "__main__":
    client.run(TOKEN)

#! Version: 1.0.0