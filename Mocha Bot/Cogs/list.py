import discord
from discord.ext import commands
import time

class ListCog(commands.Cog, name="list command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot


@commands.command(name="list", description="Returns all commands available")
@commands.cooldown(1, 2, commands.BucketType.member)
async def help(self, ctx):
    helptext = "```"
    for command in self.bot.commands:
        helptext+=f"{command}\n"
    helptext+="```"
    await ctx.send(helptext)           

def setup(bot:commands.Bot):
	bot.add_cog(ListCog(bot))