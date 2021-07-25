import discord
import random
from discord.ext import commands


class cryptocog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(cryptocog(bot))