from discord.ext import commands

class AutoInit(type(commands.Cog)):
    def __new__(cls, name, bases, dct):
        if "__init__" not in dct:
            def __init__(self, bot):
                self.bot = bot
            dct["__init__"] = __init__
        return super().__new__(cls, name, bases, dct)

class BaseCog(commands.Cog, metaclass=AutoInit):
    pass