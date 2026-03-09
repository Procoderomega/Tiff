from .sync_command import SyncSlashCommands

async def setup(bot):
    await bot.add_cog(SyncSlashCommands(bot))