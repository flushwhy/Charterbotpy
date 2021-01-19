import discord
import random
from discord.ext import commands


class bisonCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(name='crybison', aliases=['bimeme','nick','thesearemystations'])
    async def cryingbison(self, ctx):
        '''Displays memes about the eve corp Bison.'''

        bisonmemes =[               
                 "https://i.imgflip.com/4bkxt9.jpg", "https://i.imgflip.com/4bl473.jpg", "https://i.imgflip.com/4bl4gi.jpg",
                "https://i.imgflip.com/4bl4nk.jpg", "https://i.imgflip.com/4bl4xv.jpg", "https://i.imgflip.com/4bl5e4.jpg",
                "https://i.imgflip.com/4bl5k5.jpg", "https://i.imgflip.com/4bl5vb.jpg", "https://i.imgflip.com/4bl625.jpg",
                "https://i.imgflip.com/4bnx3f.jpg", "https://i.imgflip.com/4bshon.jpg",]
        
        rndbison = random.choice(bisonmemes)
        embed=discord.Embed(title="The crying Bison",
                            url="https://dcharterbot.herokuapp.com/",
                            description="Please checkout our website!",
                            color=0x69daf1)
        embed.set_image(url=rndbison)
        embed.set_footer(text="Created by RoFlush // ParaCapone")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(bisonCog(bot))