import discord
from discord import app_commands
from discord.ext import commands
from Helpers import validade_actions, safe_action, BaseCog

class BanMeta(BaseCog):
    @commands.hybrid_command(name="ban", description="Ban a user")
    @commands.has_permissions(ban_members=True)
    @app_commands.default_permissions(ban_members=True)
    async def ban_hybrid(self, ctx: commands.Context, member: discord.Member, reason: str | None = None):
        if err_message := await validade_actions(ctx.author, member, "ban"):
            return await ctx.send(err_message, ephemeral=True)
        await safe_action(lambda msg: ctx.send(msg, ephemeral=True),lambda: member.ban(reason=reason), "ban")