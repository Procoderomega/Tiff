from .kick import KickMeta
from .ban import BanMeta
from .mute import MuteMeta
from .unmute import UnmuteUser
from .clear import PurgeMeta

async def setup(bot):
    await bot.add_cog(KickMeta(bot)) #~ Kick command
    await bot.add_cog(BanMeta(bot)) #~ Ban command
    await bot.add_cog(MuteMeta(bot)) #~ Mute command
    await bot.add_cog(UnmuteUser(bot)) #~ Unmute command
    await bot.add_cog(PurgeMeta(bot)) #~ Clear command