from .pong import PongMeta

async def setup(bot):
    await bot.add_cog(PongMeta(bot))