from .kick import kick_User
from .ban import Ban_User
from .mute import Mute_User

async def setup(bot):
    await bot.add_cog(kick_User(bot)) #~ Kick command
    await bot.add_cog(Ban_User(bot)) #~ Ban command
    await bot.add_cog(Mute_User(bot)) #~ Mute command