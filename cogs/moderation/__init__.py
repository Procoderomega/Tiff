from .kick import kick_User

async def setup(bot):
    await bot.add_cog(kick_User(bot))