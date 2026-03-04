import discord
from discord.ext import commands
from typing import Optional
from Helpers import validade_Actions
from discord import app_commands

class kick_User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick_command(self, ctx, member: discord.Member, reason=None):
        error_message = await validade_Actions(ctx.author, member, "kick")
        if error_message:
            return await ctx.send(error_message)
        try:
            await member.kick(reason=reason)
            await ctx.send("✅ User was kicked")
        except discord.Forbidden:
            await ctx.send("❌ I have not enough perms")
        except discord.HTTPException:
            await ctx.send("❌ An HTTP error was show")
        except Exception as e:
            await ctx.send("❌ An unknow error was show")

    @app_commands.command(name="kick", description="kick an user")
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick_slash(self, interaction: discord.Interaction, member: discord.Member, reason: Optional[str]=None):
        err = await validade_Actions(interaction.user, member, "kickear")
        if err:
            return await interaction.response.send_message(err, ephemeral=True)
        try:
            await member.kick(reason=reason)
            await interaction.response.send_message("✅ User was kicked", ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message("❌ I have not enough perms", ephemeral=True)
        except discord.HTTPException:
            await interaction.response.send_message("❌ An HTTP error was show", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message("❌ An unknow error was show", ephemeral=True)

async def setup(bot):
    await bot.add_cog(kick_User(bot))