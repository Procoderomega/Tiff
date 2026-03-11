import discord
from Config import config
from Helpers import BaseCog
from discord.ext import commands

GUILD_ID = config["Server"]["Guild_Id"]

class SyncSlashCommands(BaseCog):
    @commands.command(name="syncSlash")
    @commands.is_owner()
    async def sync_prefix(self, ctx: commands.Context, target: str):
        if (target := target.lower()) not in ["global", "ts", "clear_global", "clear_ts"]:
            return await ctx.send("Invalid option, use 'global', 'ts', 'clear_global' or 'clear_ts'.")

        if target == "global":
            synced = await self.bot.tree.sync()
            await ctx.send(f"Synced {len(synced)} global commands")
        elif target == "ts":
            guild_obj = discord.Object(id=GUILD_ID)
            # ensure global commands are copied into the guild before syncing
            self.bot.tree.copy_global_to(guild=guild_obj)
            synced = await self.bot.tree.sync(guild=guild_obj)
            await ctx.send(f"Synced {len(synced)} commands on development server")
        elif target == "clear_global":
            self.bot.tree.clear_commands(guild=GUILD_ID)
            synced = await self.bot.tree.sync()
            await ctx.send(f"Cleared {len(synced)} global commands")
        else:
            guild_obj = discord.Object(id=GUILD_ID)
            self.bot.tree.clear_commands(guild=guild_obj)
            synced = await self.bot.tree.sync(guild=guild_obj)
            await ctx.send(f"Cleared {len(synced)} commands on development server")
