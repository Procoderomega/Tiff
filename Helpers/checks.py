import discord

#^ ========================= VALIDADOR DE BANEOS ====================================================== ^#
async def validade_Actions(moderator: discord.Member, target: discord.Member, accion: str) -> str | None:
    guild = moderator.guild
    bot_member = guild.me
    # Auto ban
    if moderator == target:
        return f"No te puedes {accion}te a ti mismo 😭"
    # Owner
    if target == guild.owner:
        return f"No puedes {accion} al dueño del servidor 👑"
    # User jerarchy
    if target.top_role >= moderator.top_role:
        return f"No puedes {accion} a alguien con un rol igual o superior al tuyo ❌"
    # bot jerarshi 🤔
    if target.top_role >= bot_member.top_role:
        return f"No puedo {accion} a alguien con un rol superior al mío ❌"
    return None