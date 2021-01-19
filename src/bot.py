import discord
from discord.ext import commands

import sys, traceback
import psutil
import time

get_token = open('token.txt', 'r').read()

def get_prefixes(bot, message):
    prefixes = ['.', '?', 'cb.']

    if not message.guild:
        return '?'

    return commands.when_mentioned_or(*prefixes)(bot, message)


initial_extensions = [ 'cogs.nema',
                       'cogs.bison',
                       'cogs.meta', ]

bot = commands.Bot(command_prefix=get_prefixes, description='Charter Bot is the only chartered bot!')

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    while True:

        starttime = time.time

        #CPU and RAM display for game output
        mem = psutil.virtual_memory()
        cpu = psutil.cpu_percent(interval=None)
        time.sleep(60.0 - ((time.time() - starttime) % 60))


    await bot.change_presence(status=discord.Status.online,
    activity=discord.Game(f'Mem used: {mem.used}, CPU used: {cpu}'))
    print(f'Successfully logged in and booted...!')


bot.run(get_token, bot=True, reconnect=True)