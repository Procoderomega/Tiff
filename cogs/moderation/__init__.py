from .kick import kick_User
from .ban import Ban_User

async def setup(bot):
    await bot.add_cog(kick_User(bot)) #~ Kick command
    await bot.add_cog(Ban_User(bot)) #~ Ban command