import discord
from discord.ext import commands 

bot = commands.Bot(command_prefix= '!') 

bot.remove_command("help")

@bot.command()
async def help(ctx):
    await ctx.author.send('Hello')

bot.run('Njk3NTY3MDAyMzMxNTc4NDAx.Xo975g.UVFhMAXhdFwsYaegilYVaj5dWWQ')
