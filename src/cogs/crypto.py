from pycoingecko import CoinGeckoAPI as cryptoapi

from discord.ext import commands


class cryptocog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="getprice", aliases=["getcoin", "cyptoprices", "cypto"])
    async def cryptopricecheck(self, ctx, coins: list):
        """Gets crypto prices and prints them out"""

        cg = cryptoapi()
        cg_return = cg.get_price(ids=coins, vs_currencies="usd")

        await ctx.send(cg_return)

    @commands.command(name="tokeneth", aliases=["tokenprice", "tokenpricecheck"])
    async def tokenVer(self, ctx, contract: str):

        cg = cryptoapi()
        cg_return = cg.get_token_price(id="ethereum", contract_addresses=contract, vs_currencies="usd")

        await ctx.send(cg_return)


def setup(bot):
    bot.add_cog(cryptocog(bot))
