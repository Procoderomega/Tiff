from .pong import Pong_Command

async def setup(bot):
    await bot.add_cog(Pong_Command(bot))