import discord
import random
from discord.ext import commands


class NemaCogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='nema', aliases=['nema','kaylon','yeeyee'])
    async def nemamemes(self, ctx):

        memes = ["https://i.imgflip.com/3kwct4.jpg", "https://i.imgflip.com/3kwdfh.jpg", "https://i.imgflip.com/3kwckg.jpg", "https://i.imgflip.com/3kwbi1.jpg", "https://i.imgflip.com/3kwc2p.jpg", "https://i.imgflip.com/3kwal0.jpg", "https://i.imgflip.com/3kw9kf.jpg", "https://i.imgflip.com/3kw85y.jpg", "https://i.imgflip.com/3kwlpj.jpg", "https://i.imgflip.com/3kwlg4.jpg", "https://i.imgflip.com/3kwkvx.jpg", "https://i.imgflip.com/3kwk88.jpg", "https://i.imgflip.com/3kwjwk.jpg", "https://i.imgflip.com/3kwjmz.jpg", "https://i.imgflip.com/3kwj23.jpg", "https://i.imgflip.com/3kwimd.jpg", "https://i.imgflip.com/3kwins.jpg", "https://i.imgflip.com/3kwi83.jpg", "https://i.imgflip.com/3kwgrq.jpg", "https://i.imgflip.com/3kwgh3.jpg", "https://i.imgflip.com/3kwfjf.jpg", "https://i.imgflip.com/3kwegm.jpg", "https://i.imgflip.com/3kwdxr.jpg", "https://i.imgflip.com/3kwdfh.jpg", "https://i.imgflip.com/3kx2ly.jpg", "https://i.imgflip.com/3kwnph.jpg", "https://i.imgflip.com/3kwnky.jpg", "https://i.imgflip.com/3kwmrw.jpg", "https://i.imgflip.com/3kwm8i.jpg", "https://i.imgflip.com/3kwm4u.jpg", "https://i.imgflip.com/3kwlyl.jpg",]

        neme = random.choice(memes)


        await ctx.send(neme)

def setup(bot):
    bot.add_cog(NemaCogs(bot))