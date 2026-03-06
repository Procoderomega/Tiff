import discord
from discord import app_commands
from discord.ext import commands

async def safe_action(send_func, action_coroutine):
    try:
        await action_coroutine
        return True
    except discord.Forbidden:
        await send_func("❌ I don't have enough permissions.")
    except discord.HTTPException:
        await send_func("❌ A Discord HTTP error occurred.")
    except Exception:
        await send_func("❌ An unknown error occurred.")
    
    return False