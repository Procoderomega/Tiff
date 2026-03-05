import discord
from discord.ext import commands
from typing import Optional
from Helpers import validade_Actions
from Helpers import safe_action
from discord import app_commands

class kick_User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick_command(self, ctx, member: discord.Member, reason=None):
        if error_message := await validade_Actions(ctx.author, member, "kick"):
            return await ctx.send(error_message)
        await safe_action(ctx.send, member.kick(reason=reason))
        

    @app_commands.command(name="kick", description="kick an user")
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick_slash(self, interaction: discord.Interaction, member: discord.Member, reason: Optional[str]=None):
        if err_message := await validade_Actions(interaction.user, member, "kick"):
            return await interaction.response.send_message(err_message, ephemeral=True)
        await safe_action(lambda msg: interaction.response.send_message(msg, ephemeral=True), member.kick(reason=reason))

async def setup(bot):
    await bot.add_cog(kick_User(bot))