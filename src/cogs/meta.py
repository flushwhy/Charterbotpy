import discord
import requests
import json
import time
from discord.ext import commands


class metaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ron', aliases=['Swanson', 'ronswanson', 'ron-swanson'])
    async def RonSwanson_parks(self, ctx):
        """This returns a random line form Ron Swason."""

        response = requests.get("https://ron-swanson-quotes.herokuapp.com/v2/quotes")

        quote_ron = response.json()

        embed = discord.Embed(title="Powered by the Ron Swanson Quotes API",
                              url="https://ron-swanson-quotes.herokuapp.com",
                              description=quote_ron[0],
                              color=0xf1c40f)
        embed.set_footer(text="Created by Roflush // Para")

        await ctx.send(embed=embed)

    @commands.command(name='mcode', aliases=['mosecode'])
    async def mose(self, ctx, message):
        """Morse code Translatior. It goes from text to Morse"""

        message = message.upper()

        MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                           'C': '-.-.', 'D': '-..', 'E': '.',
                           'F': '..-.', 'G': '--.', 'H': '....',
                           'I': '..', 'J': '.---', 'K': '-.-',
                           'L': '.-..', 'M': '--', 'N': '-.',
                           'O': '---', 'P': '.--.', 'Q': '--.-',
                           'R': '.-.', 'S': '...', 'T': '-',
                           'U': '..-', 'V': '...-', 'W': '.--',
                           'X': '-..-', 'Y': '-.--', 'Z': '--..',
                           '1': '.----', '2': '..---', '3': '...--',
                           '4': '....-', '5': '.....', '6': '-....',
                           '7': '--...', '8': '---..', '9': '----.',
                           '0': '-----', ', ': '--..--', '.': '.-.-.-',
                           '?': '..--..', '/': '-..-.', '-': '-....-',
                           '(': '-.--.', ')': '-.--.-'}

        cipher = ' '
        for letter in message:
            if letter != ' ':

                cipher += MORSE_CODE_DICT[letter] + ' '
            else:
                cipher += ' '
                # Trying to fix it sending more then one message
            ch = cipher

            # time.sleep(2)
            await ctx.send(ch)
        else:
            await ctx.send("Sorry something when wrong \o/. Try again!")

    @commands.command(name='clean', aliases=['remove', 'clear'], pass_context=True)
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx, limit: int):
        """Cleans out a textchat of trash."""

        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))

    @clean.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")


def setup(bot):
    bot.add_cog(metaCog(bot))
