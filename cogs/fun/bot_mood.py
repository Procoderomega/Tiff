from discord import app_commands
from discord.ext import commands
from Helpers import BaseCog
import discord
import json
import random
import os

class BotEstateMeta(BaseCog):
    @commands.hybrid_command(name="mood", description="Shows the bot's current mood")
    async def mood_hybrid(self, ctx: commands.Context):
        mood_file = os.path.join(os.path.dirname(__file__),"..","..","Config","moods.json")
        try:
            with open(mood_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            moods = data.get("moods", [])
        except Exception as e:
            await ctx.send("I have no moods right now 😅")
            return
        if not moods:
            await ctx.send("I have no moods right now 😅")
            return
        state = random.choice(moods)
        await ctx.send(f"I am {state}")
