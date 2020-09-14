import discord
import requests
from discord.ext import commands
from jokeapi import Jokes

class metaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='joke', aliases=['tellme','life','thetelling'])
    async def nemamemes(self, ctx,):

        j = Jokes()
        joke = j.get_joke()[0]
        if joke["type"] == "single":
            await ctx.send(joke["joke"])
        else:
            await ctx.send(joke["setup"])
            await ctx.send("|| " + joke["delivery"] + " ||")

    @commands.command(name='program', aliases=['pgquotes'])
    async def programingquotes(self, ctx):

        response = requests.get("https://programming-quotes-api.herokuapp.com/quotes/random")

        await ctx.send(response.status_code)

def setup(bot):
    bot.add_cog(metaCog(bot))