import discord
from discord.ext import commands

bot = commands.Bot(
  command_prefix='/', #any prefix you want
  case_insensitive=False,
  description=None,
  intents=discord.Intents.all(), #enable intents in discord developer portal
  help_command=None
)
 

@bot.event
async def on_ready():
    print('Bot is ready!')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

bot.run('NTE3MzM4MjMxMzQ4Mzk2MDMy.GP4F0w.dr74Yd9-FI84dZZPuqbdRLtIDYhjgitUGuQsoY')
