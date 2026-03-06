import discord

async def safe_action(send_func, action_coroutine, action):
    try:
        await action_coroutine
        return await send_func(f"✅ User was {action}")
    except discord.Forbidden:
        await send_func("❌ I don't have enough permissions.")
    except discord.HTTPException:
        await send_func("❌ A Discord HTTP error occurred.")
    except Exception:
        await send_func("❌ An unknown error occurred.")
    
    return False