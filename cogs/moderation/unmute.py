import discord
from discord import app_commands
from discord.ext import commands
from Helpers import validade_actions, safe_action, BaseCog
from Config import config

MUTED_ROLE_NAME = config["Roles"]["Muted"]

class UnmuteUser(BaseCog):    
    @commands.hybrid_command(name="unmute", description="unmute an user")
    @commands.has_permissions(manage_roles=True)
    @app_commands.default_permissions(manage_roles=True)
    async def unmute_hybrid(self, ctx: commands.Context, member: discord.Member, reason: str | None = None):
        if err_message := await validade_actions(ctx.author, member, "unmute"):
            return await ctx.send(err_message, ephemeral=True)
        if (muted_role := discord.utils.get(ctx.guild.roles, name=MUTED_ROLE_NAME)) is None:
            return await ctx.send(f"❌ Cannot find the role named {MUTED_ROLE_NAME}", ephemeral=True)
        await safe_action(lambda msg: ctx.send(msg, ephemeral=True),lambda: member.remove_roles(muted_role, reason=reason), "unmute")