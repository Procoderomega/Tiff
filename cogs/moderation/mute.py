import discord
from discord import app_commands
from Helpers import validade_actions, safe_action, BaseCog
from services import LoggingService
from discord.ext import commands
from Config import config

MUTED_ROLE_NAME = config["Roles"]["Muted"]

class MuteMeta(BaseCog):
    @commands.hybrid_command(name="mute", description="mute an user")
    @commands.has_permissions(manage_roles=True)
    @app_commands.default_permissions(manage_roles=True)
    async def mute_hybrid(self, ctx: commands.Context, member: discord.Member, reason: str | None = None):
        if err_message := await validade_actions(ctx.author, member, "mute"):
            return await ctx.send(err_message, ephemeral=True)
        if (muted_role := discord.utils.get(ctx.guild.roles, name=MUTED_ROLE_NAME)) is None:
            return await ctx.send(f"❌ Cannot find the role named {MUTED_ROLE_NAME}", ephemeral=True)
        await safe_action(lambda msg: ctx.send(msg, ephemeral=True), lambda: member.add_roles(muted_role, reason=reason), "mute")
        await self.bot.log_service.log_mute(moderator=ctx.author, target=member, reason=reason) 