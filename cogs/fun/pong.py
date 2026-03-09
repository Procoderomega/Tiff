from discord.ext import commands
from discord import app_commands
from Helpers.auto_init_meta import BaseCog
import discord

class PongMeta(BaseCog):
    @commands.hybrid_command(name="ping", description="The bot replys whit 'Pong' and latency")
    async def ping_hybrid(self, ctx: commands.Context):
        bot_lat = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! 🏓\nLatency: {bot_lat} ms")