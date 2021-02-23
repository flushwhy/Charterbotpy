import discord
import requests
import json
import time
from discord.ext import commands


rapidapi_token = open('src/cogs/rapidapi-key.txt', 'r').read()

class metaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    
    @commands.command(name='ron', aliases=['Swanson', 'ronswanson', 'ron-swanson'])
    async def RonSwanson_parks(self, ctx):
        '''This returns a random line form Ron Swason.'''

        response = requests.get("https://ron-swanson-quotes.herokuapp.com/v2/quotes")

        quote_ron = response.json()

        embed=discord.Embed(title="Powered by the Ron Swanson Quotes API",
                            url="https://ron-swanson-quotes.herokuapp.com",
                            description=quote_ron[0],
                            color=0xf1c40f)
        embed.set_footer(text="Created by Roflush // Para")

        await ctx.send(embed=embed)


    @commands.command(name='mcode', aliases=['mosecode'])
    async def mose(self, ctx, message):
        '''Morse code Translatior. It goes from text to Morse'''
    

        message = message.upper()

        MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}

        cipher = ' '
        for letter in message:
            if letter != ' ':
                
                cipher += MORSE_CODE_DICT[letter] + ' '
            else:
                cipher += ' '
                #Trying to fix it sending more then one message
            ch = cipher
            
            #time.sleep(2)
            await ctx.send(ch)
        else:
            await ctx.send("Sorry something when wrong \o/. Try again!")


    @commands.command(name='deepfake', aliases=['FakeDI'])
    async def randomuserid(self, ctx):
        '''Retruns randomly made user info. Don't use it doesn't work'''

        response = requests.get("https://randomuser.me/api/")

        # Pullling info from the request
        info_qq = response.json()['results']

        embed=discord.Embed(title="Powered by Random User . ME",
                            url="randomuser.me",
                            description="Thought it would be cool if I used it to get fake IDs!",
                            color=0xe67e22)

        #Defining Vars because discord
        gender_qq = info_qq[0]['gender']
        name_qq = info_qq[0]['name']
        email_qq = info_qq[0]['email']
        username_qq = info_qq[0]['login']['username']
        large_pic_qq = info_qq[0]['picture']['large']

        embed.add_field(name="gender",value=gender_qq, inline=True)
        embed.add_field(name="name", value=name_qq, inline=True)
        embed.add_field(name="Email", value=email_qq, inline=True)
        embed.add_field(name="Username", value=username_qq, inline=True)
        embed.set_image(url=large_pic_qq)
        embed.set_footer(text="Created by RoFlush")

        await ctx.send(embed= embed)

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

    @commands.command(name='avatar', aliases=['custom'])
    async def custom_avatar(self, ctx, name: str):
        '''This doesn't work please don't use.'''

        response = requests.get(f"https://api.adorable.io/avatars/285/{name}@adorable.io.png")

        get_img = response.json()[0]

        embed=discord.Embed(title="Powered by aborable.io",
                                    url="http://avatars.adorable.io/",
                                    color=0x69daf1)

        embed.set_image(url=get_img[0])
        embed.set_footer(text="Created by RoFlush")

        await ctx.send(embed=embed)

    @commands.command(name='fcompress', aliases=['filecom','filecompress','smallfile'])
    async def filecomp(self, ctx, fcomp_op: str):
        '''You can upload a file to discord, and the bot will compress it for you.'''
        
        await ctx.send("hahaha, Got you!")

    @commands.command(name="mememkr", aliases=['mememaker', 'makemememes'])
    async def makemorememes(self, ctx, top_name: str, bottom_name: str, memetype: str):
        '''You can make memes in discord now!'''

        url = "https://ronreiter-meme-generator.p.rapidapi.com/meme"

        querystring = {"meme":memetype,"bottom":bottom_name,"top":top_name,"font_size":"50","font":"Impact"}

        headers = {
            'x-rapidapi-key': rapidapi_token,
            'x-rapidapi-host': "ronreiter-meme-generator.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        await ctx.send(response)



def setup(bot):
    bot.add_cog(metaCog(bot))