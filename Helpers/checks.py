import discord

#^ ========================= VALIDADOR DE BANEOS ====================================================== ^#
async def validade_Actions(moderator: discord.Member, target: discord.Member, accion: str) -> str | None:
    guild = moderator.guild
    bot_member = guild.me
    # Auto ban
    if moderator == target:
        return f"❌ You cannot {accion} yourself"
    # Owner
    if target == guild.owner:
        return f"❌ You cannot {accion} the owner"
    # User jerarchy
    if target.top_role >= moderator.top_role:
        return f"❌ You cannot {accion} a user with a higher role than yours"
    # bot jerarshi 🤔
    if target.top_role >= bot_member.top_role:
        return f"❌ I cannot {accion} someone with a higher role than mine"
    return None