import discord
from discord.ext import commands
import time


class ActionCog(commands.Cog, name="Action commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	#Hello Command    
	@commands.command(name = "hello",
					usage="",
					description = "Greets the user")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def hello(self, ctx):
		 await ctx.send("Hello " + format(ctx.author.display_name) + "!")

	#Love Command
	@commands.command(name = "love",
					aliases= ["<3"],
					usage="",
					description = "Spread the love <333")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def love(self, ctx):
		 await ctx.send("I wuv u too hehe <3 " + format(ctx.author.display_name) + " o////o")

	
def setup(bot:commands.Bot):
	bot.add_cog(ActionCog(bot))