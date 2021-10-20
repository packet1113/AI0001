import discord
from discord.exe import commands

bot = commands.Bot(command_prefix = '.')

@bot.command()
async def hello(ctx):
    await ctx.reply('Hello!')

bot.run('ODg1MTQ1NzQyMzEyODg2MzQz.YTiyNg.hs_1aMh0uC2G9kLdi1T-MHXPR6E')