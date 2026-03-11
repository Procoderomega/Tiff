from .pong import PongMeta
from .bot_mood import BotEstateMeta

async def setup(bot):
    await bot.add_cog(PongMeta(bot))
    await bot.add_cog(BotEstateMeta(bot))