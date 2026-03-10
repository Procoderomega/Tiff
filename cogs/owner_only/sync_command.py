import discord
from Config import config
from Helpers import BaseCog
from discord.ext import commands

GUILD_ID = config["Server"]["Guild_Id"]

class SyncSlashCommands(BaseCog):
    @commands.command(name="syncSlash")
    @commands.is_owner()
    async def sync_prefix(self, ctx: commands.Context, target: str):
        if (target:=target.lower()) not in ["global", "ts"]:
            return await ctx.send("❌ Invalid option, use 'global' or 'ts'.")
        
        if target == "global":
            synced = await self.bot.tree.sync()
            await ctx.send(f"🌍 Synced {len(synced)} global commands")
        else:
            guild_obj = discord.Object(id=GUILD_ID)
            synced = await self.bot.tree.sync(guild=guild_obj)
            await ctx.send(f"⚡ Synced {len(synced)} commands on development server")