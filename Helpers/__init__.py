from .checks import validade_actions
from .except_handler import safe_action

async def setup(bot):
    await bot.add_cog(validade_actions(bot))
    await bot.add_cog(safe_action(bot))