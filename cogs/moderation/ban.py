import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional
from Helpers import validade_Actions
from Helpers import safe_action

class Ban_User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def Ban_command(self, ctx, member: discord.Member, reason=None):
        if error_message := await validade_Actions(ctx.author, member, "ban"):
            return await ctx.send(error_message)
        safe_action(ctx.send(), member.ban(reason=reason))
    
    @app_commands.command(name="ban", description="Ban a user")
    async def Ban_slash(self, interaction: discord.Interaction, member: discord.Member, reason: Optional[str]=None):
        if error_message := await validade_Actions(interaction.user, member, "ban"):
            return await interaction.response.send_message(error_message, ephemeral=True)
        safe_action(interaction.response.send_message(), member.ban(reason=reason))