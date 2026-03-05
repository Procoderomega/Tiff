from .checks import validade_Actions
from .exceptHandler import safe_action

async def setup(bot):
    await bot.add_cog(validade_Actions(bot))
    await bot.add_cog(safe_action(bot))