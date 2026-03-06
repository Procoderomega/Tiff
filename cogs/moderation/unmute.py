import discord
from discord import app_commands
from discord.ext import commands
from Helpers import validade_Actions
from Helpers import safe_action
from typing import Optional
MUTED_ROLE_NAME = "Muted role"

class Unmute_User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def unmute_command(self, ctx, member: discord.Member, reason=None):
        if err_message := await validade_Actions(ctx.author, member, reason=reason):
            return await ctx.send(err_message)
        if not (muted_role:=discord.utils.get(ctx.guild.roles, name=MUTED_ROLE_NAME)):
            return await ctx.send(f"❌ Cannot find the role named {MUTED_ROLE_NAME}")
        await safe_action(ctx.send, member.remove_roles(muted_role))
    
    @app_commands.command(name="unmute", description="Unmute a user")
    @app_commands.checks.has_permissions(manage_roles=True)
    async def unmute_slash(self, interaction: discord.Interaction, member: discord.Member, reason: Optional[str]=None):
        if err_message:=await validade_Actions(interaction.user, member, "unmute"):
            await interaction.response.send_message(err_message, ephemeral=True)
        if not (muted_role:=discord.utils.get(interaction.guild.roles, name=MUTED_ROLE_NAME)):
            return await interaction.response.send_message(f"❌ Cannot find the role named {MUTED_ROLE_NAME}", ephemeral=True)
        await safe_action(lambda msg: interaction.response.send_message(msg, ephemeral=True), member.remove_roles(muted_role), "unmute")