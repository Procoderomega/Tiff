import discord
from datetime import datetime, UTC
from Config import config

LOG_CHANNEL = int(config["Server"]["Log_Channel"])

class LoggingService():
    def __init__(self, bot):
        self.bot = bot
    
    async def log_ban(self, moderator, target, reason=None):
        
        embed = discord.Embed(
            title="User banned.",
            color=discord.Color.red(),
            timestamp=datetime.now(UTC)
        )
        
        embed.add_field(name="Moderator", value=moderator.mention, inline=True)
        embed.add_field(name="Target", value=target.mention, inline=True)
        embed.add_field(name="Reason", value=reason or "No reason provided", inline=False)
        
        channel = self.bot.get_channel(LOG_CHANNEL)
        if not channel:
            channel = await self.bot.fetch_channel(LOG_CHANNEL)
        await channel.send(embed=embed)