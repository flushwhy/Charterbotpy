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

        embed.set_image(url="https://robohash.org/RoFlush.png")
        embed.set_footer(text= "Author: " + author_qq + " // " + "Created by RoFlush")
        await ctx.send(embed=embed)

    # Doesn't work, Will fix later.
    @commands.command(name='ron', aliases=['Swanson', 'ronswanson', 'ron-swanson'])
    async def RonSwanson_parks(self, ctx):


        response = requests.get("https://ron-swanson-quotes.herokuapp.com/v2/quotes")

        quote_ron = response.json.dumps()

        await ctx.send(quote_ron)


    @commands.command(name='mcode', aliases=['mosecode'])
    async def mose(self, ctx):


        await ctx.send("Coming soon")


    @commands.command(name='deepfake', aliases=['FakeDI'])
    async def randomuserid(self, ctx):

        response = requests.get("https://randomuser.me/api/")

        # Pullling info from the request
        gender_qq = response.json()['gender']
        name_qq = response.json()['first', 'last']
        email_qq = response.json()['email']
        username_qq = response.json()['username']
        picture_qq = response.json()['large']

        embed=discord.Embed(title="Powered by Random names",
                            url="randomuser.me",
                            description="Thought it would be cool if I used it to get fake IDs!",
                            color=0x69daf1)

        embed.add_field(name="gender",value=gender_qq, inline=True)
        embed.add_field(name="name", value=name_qq, inline=True)
        embed.add_field(name="Email", value=email_qq, inline=True)
        embed.add_field(name="username", value=username_qq, inline=True)
        embed.set_image(url=picture_qq)
        embed.set_footer(text="Created by RoFlush")



    @commands.command(name='clean', aliases=['remove'], pass_context=True)
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx, limit: int):
        """Cleans out a textchat of trash."""
        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))

    @clean.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")

    @commands.command(name='avatar', aliases=['custom'])
    async def custom_avatar(self, ctx, name):

        response = requests.get(f"https://api.adorable.io/avatars/285/{name}@adorable.io.png")

        embed=discord.Embed(title="Powered by aborable.io",
                                    url="http://avatars.adorable.io/",
                                    color=0x69daf1)

        embed.set_image(url=response)
        embed.set_footer(text="Created by RoFlush")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(metaCog(bot))