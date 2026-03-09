from .kick import KickUser
from .ban import BanUser
from .mute import MuteUser
from .unmute import UnmuteUser
from .clear import PurgeMessages

async def setup(bot):
    await bot.add_cog(KickUser(bot)) #~ Kick command
    await bot.add_cog(BanUser(bot)) #~ Ban command
    await bot.add_cog(MuteUser(bot)) #~ Mute command
    await bot.add_cog(UnmuteUser(bot)) #~ Unmute command
    await bot.add_cog(PurgeMessages(bot)) #~ Clear command