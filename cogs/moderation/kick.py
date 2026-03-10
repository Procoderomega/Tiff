import discord
from discord.ext import commands
from discord import app_commands
from Helpers import validade_actions, safe_action, BaseCog

class KickMeta(BaseCog):
    @commands.hybrid_command(name="kick", description="Kick an user")
    @commands.has_permissions(kick_members=True)
    @app_commands.default_permissions(kick_members=True)
    async def kick_command(self, ctx: commands.Context, member: discord.Member, reason: str | None = None):
        if err_message := await validade_actions(ctx.author, member, "kick"):
            return await ctx.send(err_message, ephemeral=True)
        await safe_action(lambda msg: ctx.send(msg, ephemeral=True), lambda: member.kick(reason=reason), "kick")