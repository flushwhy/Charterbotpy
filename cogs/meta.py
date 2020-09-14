import discord
import requests
import json
from discord.ext import commands
from jokeapi import Jokes

class metaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='joke', aliases=['tellme','life','thetelling'])
    async def nemamemes(self, ctx,):
        '''Tells you a joke!'''


        j = Jokes()
        joke = j.get_joke()[0]
        if joke["type"] == "single":
            await ctx.send(joke["joke"])
        else:
            await ctx.send(joke["setup"])
            await ctx.send("|| " + joke["delivery"] + " ||")

    @commands.command(name='pg', aliases=['pgquotes', 'minds', 'ineedqq'])
    async def programingquotes(self, ctx):
        '''Post an embed of quotes from the minds of opensource.'''


        # The get request
        response = requests.get("https://programming-quotes-api.herokuapp.com/quotes/random")


        # Pulling the quote and author from the requests.
        # The "en" is the quote, that is how the API works-Not my chioce.
        quotes_qq = response.json()['en']
        author_qq = response.json()['author']

        embed=discord.Embed(title="Powered by Progamming quotes!",
                            url="https://programming-quotes-api.herokuapp.com",
                            description="Quote: " + quotes_qq,
                            color=0x69daf1)

        embed.set_image(url="https://robohash.org/RoFlush")
        embed.set_footer(text= "Author: " + author_qq + " // " + "Created by RoFlush")
        await ctx.send(embed=embed)

    # Doesn't work, Will fix later.
    @commands.command(name='ron', aliases=['Swanson', 'ronswanson', 'ron-swanson'])
    async def RonSwanson_parks(self, ctx):


        response = requests.get("https://ron-swanson-quotes.herokuapp.com/v2/quotes")

        quote_ron = response.json.dumps()

        await ctx.send(quote_ron)


def setup(bot):
    bot.add_cog(metaCog(bot))