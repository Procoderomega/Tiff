import discord
import os
import dotenv
from Config import config
from discord import app_commands
from discord.ext import commands

GUILD_ID = os.getenv("GUILD_ID")

class SyncSlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="syncSlash")
    @commands.is_owner()
    async def sync_prefix(self, ctx: commands.Context, target: str):
        target = target.lower()
        if target not in ["global", "ts"]:
            return await ctx.send("❌ Invalid option, use 'global' or 'ts'.")
        
        if target == "global":
            synced = await self.bot.tree.sync()
            await ctx.send(f"🌍 Synced {len(synced)} global commands")
        else:
            guild_obj = discord.Object(id=GUILD_ID)
            synced = await self.bot.tree.sync(guild=guild_obj)
            await ctx.send(f"⚡ Synced {len(synced)} commands on development server")