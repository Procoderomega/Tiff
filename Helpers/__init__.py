from .checks import validade_Actions

async def setup(bot):
    await bot.add_cog(validade_Actions(bot))