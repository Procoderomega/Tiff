import discord
from discord import app_commands
from discord.ext import commands
from Helpers import BaseCog

class PurgeMeta(BaseCog):
    @commands.hybrid_command(name="purge",)
    @commands.has_permissions(manage_messages=True)
    @app_commands.default_permissions(manage_messages=True)
    async def purge_hybrid(self, ctx: commands.Context, amount: int):
        if ctx.interaction:
            await ctx.defer()
        else:
            await ctx.typing()
        
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f"🧹 Deleted {amount} messages.", delete_after=5)