import discord
from discord.ext import commands
from jokeapi import Jokes

class metaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='joke', aliases=['tellme','life','thetelling'])
    async def nemamemes(self, ctx, oftype: str, ):

        j = Jokes()
        joke = j.get_joke()[0]
        if joke["type"] == "single":
            await ctx.send(joke["joke"])
        else:
            await ctx.send(joke["setup"])
            await ctx.send("|| " + joke["delivery"] + " ||")

def setup(bot):
    bot.add_cog(metaCog(bot))